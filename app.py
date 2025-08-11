# app.py
import streamlit as st
from model import generate_response

st.set_page_config(page_title="SEA-LION Chatbot", page_icon="🦁")

st.title("🦁 SEA-LION v3.5 Chatbot")
st.write("Model LLaMA SEA-LION yang dioptimalkan untuk Asia Tenggara.")

if "history" not in st.session_state:
    st.session_state.history = []

for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

if prompt := st.chat_input("Tulis pesan Anda..."):
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Sedang mengetik..."):
            reply = generate_response(prompt)
            st.write(reply)
    st.session_state.history.append(("assistant", reply))
