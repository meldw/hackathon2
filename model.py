# model.py
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Ambil token dari secrets
HF_TOKEN = st.secrets["HUGGINGFACE_TOKEN"]

# Nama model
MODEL_NAME = "aisingapore/Llama-SEA-LION-v3.5-8B-R"

# Load tokenizer
@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)

# Load model
@st.cache_resource
def load_model():
    return AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        token=HF_TOKEN,
        torch_dtype=torch.float16,
        device_map="auto"
    )

tokenizer = load_tokenizer()
model = load_model()

def generate_response(user_input, max_new_tokens=256):
    # Encode input
    inputs = tokenizer(user_input, return_tensors="pt").to(model.device)

    # Generate output
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=0.7,
        do_sample=True,
        top_p=0.9
    )

    # Decode hasil
    return tokenizer.decode(outputs[0], skip_special_tokens=True)



