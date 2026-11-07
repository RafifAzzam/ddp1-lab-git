import streamlit as st

# ==========================================
# 1. SETUP & CSS (BERSIH & STABIL)
# ==========================================
st.set_page_config(page_title="CoddyKom", page_icon="🐍", layout="centered")

st.markdown("""
<style>
/* 1. MENCEGAH KOLOM MENUMPUK VERTIKAL DI LAYAR HP */
[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    gap: 5px !important;
}
[data-testid="column"] { 
    min-width: 0 !important; 
}

/* 2. GAYA TOMBOL MAP (Primary & Secondary) */
button[kind="primary"], button[kind="secondary"] {
    width: 70px !important;
    height: 70px !important;
    border-radius: 50% !important;
    margin: 0 auto !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    font-size: 24px !important;
    font-weight: bold !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
}
button[kind="primary"] { background-color: #4CAF50 !important; color: white !important; border: 3px solid #388E3C !important; }
button[kind="secondary"] { background-color: #A5D6A7 !important; color: white !important; border: none !important; }

/* 3. GAYA TOMBOL NAVIGASI BAWAH (Tertiary) */
button[kind="tertiary"] {
    border-radius: 12px !important;
    height: 50px !important;
    width: 100% !important;
    background-color: #1E3A8A !important;
    color: white !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. STATE MANAGEMENT (ROUTING)
# ==========================================
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'menu_utama'

def pindah_halaman(nama_halaman):
    st.session_state['halaman'] = nama_halaman
    st.rerun()

# ==========================================
# 3. UI: MENU UTAMA (VERTIKAL LURUS)
# ==========================================
def tampilkan_menu():
    # --- NAVIGASI ATAS ---
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.2, 2, 1.5], gap="small")
    with c1: st.markdown("<h4 style='margin:0; text-align:center;'>🏆4!🔥</h4>", unsafe_allow_html=True)
    with c2: st.progress(5/6)
    with c3: st.selectbox("Matkul", ["DDP 1", "Alpro"], label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- JALUR BELAJAR VERTIKAL ---
    # Menggunakan 3 kolom simetris [1, 1, 1] murni untuk mengunci tombol tepat di tengah
    def buat_tombol_tengah(label, key, btype, disabled=False):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            return st.button(label, key=key, type=btype, disabled=disabled)

    def buat_titik_tengah():
        st.markdown("<div style='text-align: center; color: #A5D6A7; font-size: 24px; line-height: 0.8; padding: 10px 0;'>•<br>•<br>•</div>", unsafe_allow_html=True)

    # Stage 1
    buat_tombol_tengah("1", "b1", "secondary")
    buat_titik_tengah()

    # Stage 2
    buat_tombol_tengah("2", "b2", "secondary")
    buat_titik_tengah()

    # Stage 3 (Aktif)
    if buat_tombol_tengah("3", "b3", "primary"):
        pindah_halaman("modul_3")
    buat_titik_tengah()

    # Stage 4 (Terkunci)
    buat_tombol_tengah("🔒", "b4", "secondary", disabled=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PEMISAH BAB (MAHKOTA) ---
    st.markdown("<h2 style='text-align: center; color: #FFD700; margin: 0; line-height: 0.5;'>— 👑 —</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 1px;'>BAB 2: PERCABANGAN</p>", unsafe_allow_html=True)
    
    st.divider()

    # --- NAVIGASI BAWAH ---
    b1, b2, b3 = st.columns(3)
    with b1: st.button("⋮", key="nav1", type="tertiary")
    with b2: st.button("🏠", key="nav2", type="tertiary")
    with b3: st.button("👤", key="nav3", type="tertiary")

# ==========================================
# 4. UI: HALAMAN MATERI
# ==========================================
def tampilkan_modul_3():
    # Mengembalikan tombol ke bentuk normal khusus untuk halaman materi
    st.markdown("""
    <style>
    button[kind="secondary"] { border-radius: 8px !important; height: 40px !important; width: auto !important; margin: 0 !important; }
    button[kind="primary"] {
        border-radius: 8px !important; height: 50px !important; width: 100% !important; font-size: 18px !important;
        font-weight: bold !important; background-color: #4CAF50 !important; color: white !important; margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Kembali", type="secondary"):
        pindah_halaman("menu_utama")
        
    st.title("CoddyKom")
    st.progress(0.3, text="Level 3/10: List & Array")
    st.subheader("Materi: Apa itu List?")
    st.write("List digunakan untuk menyimpan banyak data. Gunakan kurung siku `[]`.")
    st.code('buah = ["apel", "jeruk"]', language='python')
    
    jawaban = st.text_input("Tantangan: Buat list kosong bernama `data_mahasiswa`:")
    
    if st.button("▶ JALANKAN KODE", type="primary"):
        if jawaban.replace(" ", "") == "data_mahasiswa=[]":
            st.success("Tepat sekali!")
        else:
            st.error("Coba lagi, perhatikan tanda kurung sikunya.")

# ==========================================
# 5. ROUTER
# ==========================================
if st.session_state['halaman'] == 'menu_utama':
    tampilkan_menu()
elif st.session_state['halaman'] == 'modul_3':
    tampilkan_modul_3()