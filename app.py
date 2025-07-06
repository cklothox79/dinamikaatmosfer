import streamlit as st
from datetime import datetime, timedelta

# ==================== CONFIG ====================
st.set_page_config(page_title="Skala Atmosfer Aktif", layout="wide")
st.title("🌀 SKALA ATMOSFER AKTIF SAAT INI")
st.markdown("Pantau skala atmosfer global, regional, dan lokal yang sedang memengaruhi kota pilihanmu.")

# ==================== INPUT KOTA ====================
kota = st.text_input("Masukkan nama kota", "Malang").strip().title()

if kota:
    st.markdown(f"📍 **Kota yang dipilih:** `{kota}`")

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
            st.info(f"MJO sedang aktif di fase {fase_mjo}, tetapi **belum berdampak langsung** pada wilayah {kota}.")
        else:
            st.warning("MJO tidak aktif saat ini.")

    # ==================== SKALA ITCZ ====================
    with st.expander("🌐 Skala Global: Intertropical Convergence Zone (ITCZ)", expanded=True):
        # Simulasi posisi ITCZ (akan diganti dengan data real di versi lanjut)
        lat_itcz = -7  # ITCZ melintasi sekitar Jawa
        pengaruh_itcz = kota in wilayah_dipengaruhi_mjo  # Kita asumsikan list yang sama dulu

        if pengaruh_itcz:
            st.success(f"✅ ITCZ saat ini berada dekat lintang {lat_itcz}° dan **berpotensi memengaruhi wilayah {kota}**.")
            st.markdown(f"""
            - ☁️ **ITCZ** adalah zona pertemuan angin dari belahan utara dan selatan, tempat terbentuknya awan-awan hujan.
            - 🌧️ **Dampak:** Peningkatan curah hujan, pertumbuhan awan konvektif, cuaca lembap.
            """)
        else:
            st.info(f"Saat ini ITCZ tidak berada di atas wilayah {kota}.")

    st.markdown("---")
    st.caption("📡 Data simulasi. Akan terhubung ke data real-time dari BMKG, NOAA, dan satelit cuaca pada versi berikutnya.")

else:
    st.warning("Silakan masukkan nama kota terlebih dahulu.")
