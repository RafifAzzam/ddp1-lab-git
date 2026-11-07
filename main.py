# import streamlit as st

# # ==========================================
# # 1. SETUP HALAMAN
# # ==========================================
# st.set_page_config(page_title="CoddyKom", page_icon="🐍", layout="centered")

# # ==========================================
# # 2. STATE MANAGEMENT (SISTEM ROUTING)
# # ==========================================
# # st.session_state bertindak sebagai "ingatan sementara" browser.
# # Kita gunakan untuk mencatat user sedang berada di halaman mana.
# if 'halaman' not in st.session_state:
#     st.session_state['halaman'] = 'menu_utama'

# def pindah_halaman(nama_halaman):
#     """Fungsi dokumentasi: Dipanggil oleh tombol untuk mengubah state halaman dan me-refresh layar."""
#     st.session_state['halaman'] = nama_halaman
#     st.rerun() # Memaksa Streamlit memuat ulang halaman dengan state yang baru

# # ==========================================
# # 3. KOMPONEN UI: MENU UTAMA
# # ==========================================
# def tampilkan_menu():
#     # --- NAVIGASI ATAS ---
#     col1, col2, col3 = st.columns([1, 1.5, 1], gap="small")
#     with col1:
#         st.markdown("🏆 **4!** 🔥") # Ikon streak & trofi
#     with col2:
#         st.progress(5/6, text="Progres: 5/6") # Target penyelesaian bab
#     with col3:
#         # Dropdown pilihan mata kuliah tanpa label teks di atasnya
#         st.selectbox("Matkul", ["DDP 1", "Alpro", "Basdat"], label_visibility="collapsed")
    
#     st.divider()

#     # --- JALUR BELAJAR (GAME MAP) ---
#     # Menggunakan tombol yang membentang penuh (use_container_width=True) 
#     # agar ramah jempol dan mensimulasikan urutan vertikal.
    
#     if st.button("✅ 1. Pengenalan Python", use_container_width=True):
#         pindah_halaman("modul_1")
        
#     if st.button("✅ 2. Variabel & Tipe Data", use_container_width=True):
#         pindah_halaman("modul_2")
        
#     # Modul yang sedang aktif (Highlight)
#     if st.button("🟢 3. List & Array (Lanjut Belajar →)", use_container_width=True, type="primary"):
#         pindah_halaman("modul_3")
        
#     # --- PEMISAH BAB (MAHKOTA) ---
#     st.markdown("<h3 style='text-align: center; color: #FFD700;'>— 👑 —</h3>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; font-weight: bold;'>BAB 2: PERCABANGAN</p>", unsafe_allow_html=True)
    
#     # Tombol terkunci (disabled=True membuat tombol redup dan tidak bisa diklik)
#     st.button("🔒 4. Percabangan if/else", use_container_width=True, disabled=True)
#     st.button("🔒 5. Perulangan (Loops)", use_container_width=True, disabled=True)

#     st.divider()
    
#     # --- NAVIGASI BAWAH (BOTTOM BAR) ---
#     b_col1, b_col2, b_col3 = st.columns(3)
#     with b_col1:
#         st.button("⋮", use_container_width=True)
#     with b_col2:
#         st.button("🏠", use_container_width=True)
#     with b_col3:
#         st.button("👤", use_container_width=True)

# # ==========================================
# # 4. KOMPONEN UI: HALAMAN MATERI
# # ==========================================
# def tampilkan_modul_3():
#     # Tombol kembali ke menu utama
#     if st.button("← Kembali ke Menu"):
#         pindah_halaman("menu_utama")
        
#     st.title("CoddyKom")
#     st.progress(0.3, text="Level 3/10: List & Array")
    
#     st.subheader("Materi: Apa itu List?")
#     st.write("List digunakan untuk menyimpan banyak data dalam satu variabel. Gunakan kurung siku `[]`.")
#     st.code('buah = ["apel", "jeruk"]', language='python')
    
#     st.subheader("Tantangan")
#     jawaban = st.text_input("Buat list kosong bernama `data_mahasiswa`:")
#     if st.button("▶ JALANKAN KODE", use_container_width=True):
#         if jawaban.replace(" ", "") == "data_mahasiswa=[]":
#             st.success("Tepat sekali!")
#         else:
#             st.error("Coba lagi, perhatikan tanda kurung sikunya.")

# # ==========================================
# # 5. ROUTER (PENGENDALI LALU LINTAS)
# # ==========================================
# # Bagian ini yang membaca 'ingatan' browser dan menentukan fungsi mana yang dipanggil
# if st.session_state['halaman'] == 'menu_utama':
#     tampilkan_menu()
# elif st.session_state['halaman'] == 'modul_1':
#     st.warning("Halaman Modul 1 belum dibangun.")
#     if st.button("← Kembali"): pindah_halaman("menu_utama")
# elif st.session_state['halaman'] == 'modul_2':
#     st.warning("Halaman Modul 2 belum dibangun.")
#     if st.button("← Kembali"): pindah_halaman("menu_utama")
# elif st.session_state['halaman'] == 'modul_3':
#     tampilkan_modul_3()

import streamlit as st

# ==========================================
# 1. SETUP & CSS KUSTOM (ANTI-RUNTUH DI HP)
# ==========================================
st.set_page_config(page_title="CoddyKom", page_icon="🐍", layout="centered")

st.markdown("""
<style>
/* 1. PAKSA KOLOM TETAP SEJAJAR DI HP (Mencegah numpuk ke kiri) */
div[data-testid="column"] {
    min-width: 0 !important;
}
div[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    align-items: center !important;
}

/* 2. GAYA TOMBOL BULAT ZIGZAG */
div.stButton > button {
    border-radius: 50%;
    width: 70px;
    height: 70px;
    margin: 0 auto;
    display: block;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
}
/* Stage Aktif */
div.stButton > button[kind="primary"] {
    background-color: #4CAF50;
    color: white;
    border: 3px solid #388E3C;
}
/* Stage Selesai/Terkunci */
div.stButton > button[kind="secondary"] {
    background-color: #A5D6A7;
    color: white;
    border: none;
}

/* 3. KEMBALIKAN TOMBOL NAVIGASI BAWAH JADI KOTAK */
div[data-testid="stHorizontalBlock"]:last-of-type div.stButton > button {
    border-radius: 10px;
    height: 50px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. STATE MANAGEMENT
# ==========================================
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'menu_utama'

def pindah_halaman(nama_halaman):
    st.session_state['halaman'] = nama_halaman
    st.rerun()

import streamlit as st

# ==========================================
# 1. SETUP & CSS KUSTOM (ANTI-SCROLL HORIZONTAL)
# ==========================================
st.set_page_config(page_title="CoddyKom", page_icon="🐍", layout="centered")

st.markdown("""
<style>
/* 1. MENCEGAH SCROLL HORIZONTAL DI HP */
div[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    gap: 0 !important; /* Hapus jarak renggang antar kolom */
    width: 100% !important;
}
div[data-testid="column"] {
    min-width: 0 !important;
    flex: 1 1 0% !important; /* Paksa 3 kolom berbagi lebar persis 33.3% */
    padding: 0 !important; /* Hapus padding bawaan penyebab layar menjebol */
}

/* 2. GAYA TOMBOL BULAT (Khusus Stage di Map) */
/* Kita targetkan hanya tombol Primary & Secondary agar tombol lain aman */
div.stButton > button[kind="primary"], 
div.stButton > button[kind="secondary"] {
    border-radius: 50% !important;
    width: 65px !important; /* Sedikit dikecilkan agar sangat aman di HP */
    height: 65px !important;
    margin: 0 auto !important;
    display: block !important;
    font-size: 22px !important;
    font-weight: bold !important;
    box-shadow: 0px 4px 6px rgba(0,0,0,0.1) !important;
}

/* Warna Stage Aktif */
div.stButton > button[kind="primary"] {
    background-color: #4CAF50 !important;
    color: white !important;
    border: 3px solid #388E3C !important;
}
/* Warna Stage Selesai/Terkunci */
div.stButton > button[kind="secondary"] {
    background-color: #A5D6A7 !important;
    color: white !important;
    border: none !important;
}

/* 3. GAYA TOMBOL NAVIGASI (Tertiary) */
div.stButton > button[kind="tertiary"] {
    border-radius: 8px !important;
    height: 45px !important;
    width: 90% !important;
    margin: 0 auto !important;
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. STATE MANAGEMENT
# ==========================================
if 'halaman' not in st.session_state:
    st.session_state['halaman'] = 'menu_utama'

def pindah_halaman(nama_halaman):
    st.session_state['halaman'] = nama_halaman
    st.rerun()

# ==========================================
# 3. UI: MENU UTAMA ZIGZAG (FIXED)
# ==========================================
def tampilkan_menu():
    # --- NAVIGASI ATAS ---
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col1: st.markdown("<h3 style='margin:0; text-align:center;'>🏆4!🔥</h3>", unsafe_allow_html=True)
    with col2: st.progress(5/6)
    with col3: st.selectbox("Matkul", ["DDP 1", "Alpro"], label_visibility="collapsed")
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- JALUR BELAJAR ZIGZAG ---
    
    # Stage 1 (Kiri)
    c1, c2, c3 = st.columns(3)
    with c1: st.button("1", key="btn1", type="secondary")
    
    # Titik penghubung 1 -> 2
    c1, c2, c3 = st.columns(3)
    with c2: st.markdown("<div style='text-align: center; color: #A5D6A7; font-size: 20px; line-height: 1;'>•<br>•</div>", unsafe_allow_html=True)

    # Stage 2 (Kanan)
    c1, c2, c3 = st.columns(3)
    with c3: st.button("2", key="btn2", type="secondary")
    
    # Titik penghubung 2 -> 3
    c1, c2, c3 = st.columns(3)
    with c2: st.markdown("<div style='text-align: center; color: #A5D6A7; font-size: 20px; line-height: 1;'>•<br>•</div>", unsafe_allow_html=True)

    # Stage 3 (Tengah - Aktif)
    c1, c2, c3 = st.columns(3)
    with c2: 
        if st.button("3", key="btn3", type="primary"):
            pindah_halaman("modul_3")
            
    # Titik penghubung 3 -> 4
    c1, c2, c3 = st.columns(3)
    with c2: st.markdown("<div style='text-align: center; color: #E0E0E0; font-size: 20px; line-height: 1;'>•<br>•</div>", unsafe_allow_html=True)

    # Stage 4 (Kiri - Terkunci)
    c1, c2, c3 = st.columns(3)
    with c1: st.button("🔒", key="btn4", disabled=True, type="secondary")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PEMISAH BAB (MAHKOTA) ---
    st.markdown("<h3 style='text-align: center; color: #FFD700; margin-bottom: 0;'>— 👑 —</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>BAB 2: PERCABANGAN</p>", unsafe_allow_html=True)
    
    st.divider()

    # --- NAVIGASI BAWAH ---
    b_col1, b_col2, b_col3 = st.columns(3)
    # Gunakan type="tertiary" agar tidak ikut berubah jadi bulat!
    with b_col1: st.button("⋮", key="nav_menu", type="tertiary")
    with b_col2: st.button("🏠", key="nav_home", type="tertiary")
    with b_col3: st.button("👤", key="nav_profile", type="tertiary")

# ==========================================
# 4. UI: HALAMAN MATERI
# ==========================================
def tampilkan_modul_3():
    if st.button("← Kembali ke Map", type="tertiary"):
        pindah_halaman("menu_utama")
        
    st.title("CoddyKom")
    st.progress(0.3, text="Level 3/10: List & Array")
    st.subheader("Materi: Apa itu List?")
    st.write("List digunakan untuk menyimpan banyak data. Gunakan `[]`.")
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