import streamlit as st
from predict import predict_genre_rf

st.title("🎵 Music Genre Classifier")
uploaded_file = st.file_uploader("Upload a music file", type=["wav"])

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    genre = predict_genre_rf("temp.wav")
    st.success(f"🎶 Predicted Genre: {genre}")
