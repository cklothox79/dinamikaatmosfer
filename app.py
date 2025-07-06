# ... semua import tetap sama ...
import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
from geopy.geocoders import Nominatim

# ==================== CONFIG ====================
st.set_page_config(page_title="Skala Atmosfer Aktif", layout="wide")
st.title("🌀 SKALA ATMOSFER AKTIF SAAT INI")
st.markdown("*Pantau skala atmosfer global, regional, dan lokal yang sedang memengaruhi kota pilihanmu.*")
st.markdown("**Editor: Ferri Kusuma (STMKG/M8TB_14.22.0003)**")

# ==================== RIWAYAT KOTA ====================
if "riwayat_kota" not in st.session_state:
    st.session_state.riwayat_kota = []

st.markdown("### 🏙️ Masukkan Nama Kota")

# Tombol cepat dari riwayat sebelumnya
for kota_riwayat in reversed(st.session_state.riwayat_kota[-5:]):
    if st.button(f"📍 {kota_riwayat}"):
        st.session_state.kota_terpilih = kota_riwayat

# Input teks manual
kota_input = st.text_input(" ", "Malang").strip().title()

# Prioritaskan tombol, lalu input manual
kota = st.session_state.get("kota_terpilih", kota_input)

# Simpan ke riwayat
if kota and kota not in st.session_state.riwayat_kota:
    st.session_state.riwayat_kota.append(kota)

if kota:
    st.markdown(f"📍 **Kota yang dipilih:** `{kota}`")

    # ==================== GEOCODING ====================
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

        # ==================== SEMUA SKALA ====================
        # 💡 Bagian MJO, ITCZ, Kelvin, Rossby, Surge, ENSO, dan IOD tetap sama
        # 🔁 Tidak dituliskan ulang di sini karena kamu sudah punya script lengkap sebelumnya
        # Silakan salin semua bagian skala atmosfer setelah peta tadi, lalu tempel di sini

        # 📝 Contoh ringkas:
        # st.expander("🌐 MJO ...")
        # st.expander("🌐 ITCZ ...")
        # st.expander("🌊 Kelvin/Rossby ...")
        # st.expander("🌬️ Southerly Surge ...")
        # st.expander("🌐 ENSO + Index ...")
        # st.expander("🌐 IOD + Index ...")

    else:
        st.error("❗ Kota tidak ditemukan. Mohon cek kembali ejaannya.")
else:
    st.warning("Silakan masukkan nama kota terlebih dahulu.")
