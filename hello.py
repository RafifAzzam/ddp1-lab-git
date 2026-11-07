import streamlit as st

# Membuat judul halaman web
st.title("Aplikasi Pertama Saya! 🎉")

# Membuat teks biasa
st.write("Halo! Ini adalah aplikasi web pertama saya menggunakan Streamlit.")

# Membuat tombol interaktif
if st.button("Klik di sini"):
    st.balloons()  # Efek animasi balon terbang!
    st.success("Terima kasih sudah mengklik!")

# Tambahkan kode ini di bawah kode tombol balon yang tadi:
nama = st.text_input("Masukkan nama Anda:")

if nama:
    st.write(f"Halo **{nama}**, selamat belajar Python dan Streamlitascsa! 🚀")

