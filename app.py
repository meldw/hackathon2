
# streamlit_app.py
import streamlit as st
from model import load_modelll, generate_responseee

st.set_page_config(page_title="SEA-LION Chatbot", page_icon="🤖")

st.title("🤖 SEA-LION Chatbot")
st.write("Model: `aisingapore/Llama-SEA-LION-v3.5-8B-R`")

# Load model (cached biar nggak reload tiap kali)
@st.cache_resource
def get_model():
    load_modelll()

get_model()

# State untuk menyimpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input user
if prompt := st.chat_input("Tulis pesan..."):
    # Simpan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate jawaban
    with st.chat_message("assistant"):
        with st.spinner("Sedang mengetik..."):
            response = generate_response(prompt)
            st.write(response)

    # Simpan jawaban ke riwayat
    st.session_state.messages.append({"role": "assistant", "content": response})



