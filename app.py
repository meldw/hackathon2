# app.py
import streamlit as st
from model import generate_response

st.set_page_config(page_title="SEA-LION Chatbot", page_icon="🦁")

st.title("🦁 SEA-LION v3.5 Chatbot")
st.write("Chatbot sederhana menggunakan model SEA-LION dari AI Singapore.")

# Input dari user
user_input = st.text_area("Ketik pertanyaan atau pesan Anda:", height=100)

if st.button("Kirim"):
    if user_input.strip():
        with st.spinner("Sedang memproses..."):
            reply = generate_response(user_input)
        st.markdown(f"**Bot:** {reply}")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")
