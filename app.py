import streamlit as st
from datetime import datetime, timedelta

# ==================== CONFIG ====================
st.set_page_config(page_title="Skala Atmosfer Aktif", layout="wide")
st.title("🌀 SKALA ATMOSFER AKTIF SAAT INI")
st.markdown("Pantau skala atmosfer global, regional, dan lokal yang sedang memengaruhi kota pilihanmu.")

# ==================== INPUT KOTA BEBAS ====================
kota = st.text_input("Masukkan nama kota", "Malang").strip().title()

if kota:
    st.markdown(f"📍 **Kota yang dipilih:** `{kota}`")

    # ========== SIMULASI DATA MJO ==========
    fase_mjo = 4  # bisa diganti dengan input API nantinya
    mjo_aktif = True
    start_date = datetime(2025, 7, 3)
    end_date = datetime(2025, 7, 11)

    # Kota-kota di Indonesia yang dipengaruhi fase 2–5
    wilayah_dipengaruhi_mjo = ["Malang", "Surabaya", "Sidoarjo", "Jember", "Kediri", "Blitar", "Lumajang"]
    pengaruh = kota in wilayah_dipengaruhi_mjo and fase_mjo in [2, 3, 4, 5]

    # ========== OUTPUT MJO ==========
    with st.expander("🌐 Skala Global: Madden-Julian Oscillation (MJO)", expanded=True):
        if mjo_aktif and pengaruh:
            st.success(f"✅ MJO sedang aktif di fase {fase_mjo} dan **memengaruhi wilayah {kota}**.")
            st.markdown(f"""
            - 🗓️ **Durasi aktif:** {start_date.strftime('%d %b %Y')} hingga {end_date.strftime('%d %b %Y')}
            - ☁️ **Dampak umum:** Meningkatkan peluang hujan, pembentukan awan konvektif, potensi cuaca ekstrem lokal.
            """)
        elif mjo_aktif:
            st.info(f"MJO sedang aktif di fase {fase_mjo}, tetapi **belum berdampak langsung** pada wilayah {kota}.")
        else:
            st.warning("MJO tidak aktif saat ini.")

    st.markdown("---")
    st.caption("📡 Data simulasi. Akan terhubung ke data real-time dari BMKG atau NOAA di versi berikutnya.")
else:
    st.warning("Silakan masukkan nama kota terlebih dahulu.")
