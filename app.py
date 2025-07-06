import streamlit as st
from datetime import datetime, timedelta

# ==================== CONFIG ====================
st.set_page_config(page_title="Skala Atmosfer Aktif", layout="wide")
st.title("🌀 SKALA ATMOSFER AKTIF SAAT INI")
st.markdown("Pantau skala atmosfer global, regional, dan lokal yang sedang memengaruhi kota pilihanmu.")

# ==================== INPUT KOTA ====================
kota = st.selectbox("Pilih kota", ["Malang", "Surabaya", "Sidoarjo", "Jakarta", "Bandung", "Semarang"])

st.markdown(f"📍 **Kota yang dipilih:** `{kota}`")

# ==================== MJO SIMULASI ====================
# Simulasi data MJO (nantinya ini bisa diganti dari API BMKG atau NOAA)
fase_mjo = 4  # fase 4 = pengaruh ke Jawa
mjo_aktif = True
start_date = datetime.today() - timedelta(days=3)
end_date = datetime.today() + timedelta(days=5)

# ==================== LOGIKA ====================
mjo_pengaruh_jawa = [2, 3, 4, 5]  # fase yang memengaruhi Jawa
pengaruh = kota.lower() in ["malang", "surabaya", "sidoarjo"] and fase_mjo in mjo_pengaruh_jawa

# ==================== TAMPILKAN HASIL ====================
with st.expander("🌐 Skala Global: Madden-Julian Oscillation (MJO)"):
    if mjo_aktif and pengaruh:
        st.success(f"✅ MJO sedang aktif di fase {fase_mjo} dan **memengaruhi wilayah {kota}**.")
        st.markdown(f"""
        - 🗓️ **Durasi aktif:** {start_date.strftime('%d %b %Y')} hingga {end_date.strftime('%d %b %Y')}
        - ☁️ **Dampak umum:** Meningkatkan peluang hujan, pembentukan awan konvektif, potensi cuaca ekstrem lokal.
        """)
    elif mjo_aktif:
        st.info(f"MJO aktif di fase {fase_mjo}, namun belum langsung memengaruhi wilayah {kota}.")
    else:
        st.warning("MJO tidak aktif saat ini.")

# ==================== PENGEMBANGAN ====================
st.markdown("---")
st.caption("📡 Data simulasi. Ke depan akan dihubungkan dengan data BMKG/NOAA secara langsung.")

