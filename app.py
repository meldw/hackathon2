import streamlit as st
from model import generate_response
import streamlit.components.v1 as components


# --- Baca file HTML ---
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# --- Tampilkan HTML di Streamlit ---
components.html(html_code, height=1200, scrolling=True)


