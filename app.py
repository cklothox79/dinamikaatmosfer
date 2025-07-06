import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim

# ==================== CONFIG ====================
st.set_page_config(page_title="Skala Atmosfer Aktif", layout="wide")
st.title("🌀 SKALA ATMOSFER AKTIF SAAT INI")
st.markdown("*Pantau skala atmosfer global, regional, dan lokal yang sedang memengaruhi kota pilihanmu.*")
st.markdown("**Editor: Ferri Kusuma (STMKG/M8TB_14.22.0003)**")

# ==================== INPUT KOTA ====================
st.markdown("### 🏙️ Masukkan Nama Kota")
kota = st.text_input(" ", "Malang").strip().title()  # Label kosong agar custom markdown tetap terlihat

if kota:
    st.markdown(f"📍 **Kota yang dipilih:** `{kota}`")

    # ==================== GEOCODE ====================
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(kota)

    if location:
        lat, lon = location.latitude, location.longitude

        # ==================== PETA ====================
        st.markdown("### 🗺️ Lokasi Kota di Peta")
        m = folium.Map(location=[lat, lon], zoom_start=6)
        folium.Marker([lat, lon], tooltip=kota, icon=folium.Icon(color='blue')).add_to(m)

        # (Opsional) Simulasi ilustrasi arah sirkulasi besar
        folium.Circle(
            radius=400000,
            location=[lat, lon],
            color="cyan",
            fill=True,
            fill_opacity=0.05,
            popup="Zona pengaruh atmosfer",
        ).add_to(m)

        st_folium(m, width=700, height=450)

        # ==================== SKALA MJO ====================
        fase_mjo = 4  # Simulasi fase MJO saat ini
        mjo_aktif = True
        start_date = datetime(2025, 7, 3)
        end_date = datetime(2025, 7, 11)

        wilayah_dipengaruhi_mjo = ["Malang", "Surabaya", "Sidoarjo", "Jember", "Kediri", "Blitar", "Lumajang"]
        pengaruh_mjo = kota in wilayah_dipengaruhi_mjo and fase_mjo in [2, 3, 4, 5]

        with st.expander("🌐 Skala Global: Madden-Julian Oscillation (MJO)", expanded=True):
            if mjo_aktif and pengaruh_mjo:
                st.success(f"✅ MJO sedang aktif di fase {fase_mjo} dan **memengaruhi wilayah {kota}**.")
                st.markdown(f"""
                - 🗓️ **Durasi aktif:** {start_date.strftime('%d %b %Y')} hingga {end_date.strftime('%d %b %Y')}
                - ☁️ **Dampak umum:** Meningkatkan peluang hujan, pembentukan awan konvektif, potensi cuaca ekstrem lokal.
                """)
            elif mjo_aktif:
                st.info(f"MJO aktif di fase {fase_mjo}, tetapi **belum berdampak langsung** pada wilayah {kota}.")
            else:
                st.warning("MJO tidak aktif saat ini.")

        # ==================== SKALA ITCZ ====================
        with st.expander("🌐 Skala Global: Intertropical Convergence Zone (ITCZ)", expanded=True):
            lat_itcz = -7
            pengaruh_itcz = kota in wilayah_dipengaruhi_mjo

            if pengaruh_itcz:
                st.success(f"✅ ITCZ saat ini berada dekat lintang {lat_itcz}° dan **berpotensi memengaruhi wilayah {kota}**.")
                st.markdown(f"""
                - ☁️ **ITCZ** adalah zona pertemuan angin dari utara dan selatan, tempat terbentuknya awan-awan hujan.
                - 🌧️ **Dampak:** Peningkatan curah hujan, pertumbuhan awan konvektif, cuaca lembap.
                """)
            else:
                st.info(f"Saat ini ITCZ tidak berada di atas wilayah {kota}.")

        st.markdown("---")
        st.caption("📡 Data simulasi. Akan terhubung ke data real-time dari BMKG, NOAA, dan satelit cuaca pada versi berikutnya.")

    else:
        st.error("❗ Kota tidak ditemukan. Mohon cek kembali ejaannya.")
else:
    st.warning("Silakan masukkan nama kota terlebih dahulu.")
