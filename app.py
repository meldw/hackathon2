import streamlit as st
from model import list_models, chat_with_sealion

# Set judul halaman
st.set_page_config(page_title="SEA-LION Chat", layout="centered")
st.title("🤖 SEA-LION Chat App")
st.write("Ketik pertanyaanmu di bawah untuk ngobrol dengan model LLM ASEAN 🇸🇬🇮🇩🇻🇳")

# Ambil daftar model
try:
    models = list_models()
    model_ids = [m["id"] for m in models.get("data", [])]
except Exception as e:
    st.error(f"Gagal mengambil model: {e}")
    st.stop()

# Pilihan model
model_name = st.selectbox("Pilih model:", model_ids, index=0)

# Kotak input pengguna
user_input = st.text_input("Pertanyaanmu:", placeholder="Misal: Apa itu kontrak kerja lintas negara?")

# Tombol kirim
if st.button("Tanya"):
    if user_input.strip() == "":
        st.warning("Silakan isi pertanyaan terlebih dahulu.")
    else:
        try:
            response = chat_with_sealion(user_input, model=model_name, max_tokens=300)
            st.markdown("### ✉️ Jawaban:")
            st.write(response)
        except Exception as err:
            st.error(f"Gagal mengambil jawaban: {err}")
