# import streamlit as st
# from model import generate_response

# st.set_page_config(page_title="SEA-LION Chatbot", page_icon="🤖")
# st.title("🤖 SEA-LION v3.5 Chatbot")

# if "history" not in st.session_state:
#     st.session_state.history = []

# for role, text in st.session_state.history:
#     with st.chat_message(role):
#         st.write(text)

# if prompt := st.chat_input("Tulis pesan..."):
#     st.session_state.history.append(("user", prompt))
#     with st.chat_message("assistant"):
#         with st.spinner("Metode berpikir model sedang aktif..."):
#             reply = generate_response(prompt)
#             st.write(reply)
#     st.session_state.history.append(("assistant", reply))

import streamlit as st
from model import generate_response

st.set_page_config(page_title="SEA-LION Chatbot", page_icon="🤖")
st.title("🤖 SEA-LION v3.5 Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

# tampilkan history lama
for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

# input baru
if prompt := st.chat_input("Tulis pesan..."):
    # tampilkan pesan user
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.write(prompt)

    # proses balasan
    with st.chat_message("assistant"):
        with st.spinner("Metode berpikir model sedang aktif..."):
            try:
                reply = generate_response(prompt)
            except Exception as e:
                reply = f"Error: {e}"
            st.write(reply)
    st.session_state.history.append(("assistant", reply))
