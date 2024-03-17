import streamlit as st
from transformers import pipeline

# Membuat pipeline transformer
generator = pipeline('text-generation', model='gpt2')

# Membuat input teks
input_text = st.text_input("Masukkan teks di sini")

# Menghasilkan teks
if st.button("Generate"):
    output_text = generator(input_text, max_length=100, do_sample=True)[0]
    st.write(output_text['generated_text'])
