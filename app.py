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
kota = st.text_input(" ", "Malang").strip().title()

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

        folium.Circle(
            radius=400000,
            location=[lat, lon],
            color="cyan",
            fill=True,
            fill_opacity=0.05,
            popup="Zona pengaruh atmosfer",
        ).add_to(m)

        st_folium(m, width=700, height=450)

        # ==================== SKALA GLOBAL: MJO ====================
        fase_mjo = 4
        mjo_aktif = True
        start_date = datetime(2025, 7, 3)
        end_date = datetime(2025, 7, 11)
        wilayah_dipengaruhi_mjo = ["Malang", "Surabaya", "Sidoarjo", "Jember", "Kediri", "Blitar", "Lumajang"]
        pengaruh_mjo = kota in wilayah_dipengaruhi_mjo and fase_mjo in [2, 3, 4, 5]

        with st.expander("🌐 Skala Global: Madden-Julian Oscillation (MJO)", expanded=True):
            if mjo_aktif and pengaruh_mjo:
                st.success(f"✅ MJO aktif di fase {fase_mjo} dan **memengaruhi wilayah {kota}**.")
                st.markdown(f"""
                - 🗓️ **Durasi:** {start_date.strftime('%d %b %Y')} – {end_date.strftime('%d %b %Y')}
                - 🌧️ **Dampak:** Potensi hujan konvektif & badai lokal meningkat.
                """)
            elif mjo_aktif:
                st.info(f"MJO aktif (fase {fase_mjo}) namun belum berdampak langsung pada wilayah {kota}.")
            else:
                st.warning("MJO tidak aktif saat ini.")

        # ==================== SKALA GLOBAL: ITCZ ====================
        with st.expander("🌐 Skala Global: Intertropical Convergence Zone (ITCZ)", expanded=True):
            lat_itcz = -7
            pengaruh_itcz = kota in wilayah_dipengaruhi_mjo

            if pengaruh_itcz:
                st.success(f"✅ ITCZ berada di sekitar {lat_itcz}° dan **berpotensi memengaruhi wilayah {kota}**.")
                st.markdown(f"""
                - ☁️ Zona pertemuan angin utara-selatan → awan hujan terbentuk.
                - 🌧️ Cuaca menjadi lebih lembap & hujan ringan–lebat.
                """)
            else:
                st.info(f"ITCZ tidak aktif di atas wilayah {kota} saat ini.")

        # ==================== SKALA REGIONAL: KELVIN/ROSSBY ====================
        with st.expander("🌊 Skala Regional: Gelombang Kelvin & Rossby", expanded=True):
            kelvin_aktif = True
            rossby_aktif = False
            wilayah_kelvin = ["Malang", "Jember", "Banyuwangi"]
            wilayah_rossby = ["Padang", "Pontianak"]

            if kota in wilayah_kelvin:
                st.success("✅ Gelombang Kelvin aktif dan memengaruhi wilayah ini.")
                st.markdown("""
                - 🔁 Gelombang tropis cepat dari barat ke timur.
                - 🌧️ Pemicu hujan konvektif cepat, khususnya sore–malam.
                """)
            elif kota in wilayah_rossby:
                st.success("✅ Gelombang Rossby aktif di wilayah ini.")
                st.markdown("""
                - 🌀 Gelombang lambat dari timur ke barat.
                - 🕒 Durasinya panjang, meningkatkan kelembapan dalam beberapa hari.
                """)
            else:
                st.info("Belum ada pengaruh langsung dari Gelombang Kelvin/Rossby di wilayah ini.")

        # ==================== SKALA REGIONAL: MONSOON SURGE ====================
        with st.expander("🌬️ Skala Regional: Southerly Surge (Seruak Selatan)", expanded=True):
            surge_aktif = True
            wilayah_surge = ["Surabaya", "Sidoarjo", "Malang", "Bali", "Kupang"]

            if kota in wilayah_surge:
                st.success("✅ Terjadi southerly surge di wilayah ini.")
                st.markdown("""
                - 💨 Angin kuat dari arah selatan membawa uap air dari Samudera Hindia.
                - 🌧️ Menyebabkan hujan mendadak, bahkan di musim kemarau.
                """)
            else:
                st.info("Wilayah ini tidak sedang dipengaruhi oleh seruak angin selatan (surge).")

        st.markdown("---")
        st.caption("📡 Semua data bersifat simulasi. Akan ditautkan ke sumber data BMKG/NOAA pada versi mendatang.")

    else:
        st.error("❗ Kota tidak ditemukan. Mohon cek kembali ejaannya.")
else:
    st.warning("Silakan masukkan nama kota terlebih dahulu.")
