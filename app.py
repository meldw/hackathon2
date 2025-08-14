import streamlit as st
from model import generate_response

with open("style.css") as f:
    css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    
with open("index.html") as f:
    html_content = f.read()
    st.markdown(html_content, unsafe_allow_html=True)


st.set_page_config(page_title="SEA-LION Chatbot", page_icon="🤖")


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ketik pesan…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        with st.spinner("Generating…"):
            try:
                response = generate_response(prompt)
            except Exception as e:
                response = f"⚠️ {e}"
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
