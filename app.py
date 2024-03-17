import streamlit as st
from transformers import pipeline

# Membuat pipeline untuk analisis sentimen
nlp = pipeline('sentiment-analysis')

st.title('Analisis Sentimen dengan Streamlit dan Transformers')

# Membuat input teks
text = st.text_input('Masukkan teks di sini')

if text:
    # Melakukan analisis sentimen
    result = nlp(text)[0]
    st.write(f"Sentimen: {result['label']}, Skor: {result['score']}")
