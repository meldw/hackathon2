# app.py
import streamlit as st
from model import generate_response

st.set_page_config(page_title="SEA-LION Chat", layout="centered")
st.title("🦁 SEA-LION Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat_history.append(("user", user_input))
    try:
        reply = generate_response(user_input, max_tokens=200)
    except Exception as e:
        reply = f"❌ Error: {e}"
    st.session_state.chat_history.append(("bot", reply))

for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"🧑‍💻 **You:** {msg}")
    else:
        st.markdown(f"🤖 **SEA-LION:** {msg}")
