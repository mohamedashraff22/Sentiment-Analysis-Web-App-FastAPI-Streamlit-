import streamlit as st
import requests

st.title("Sentiment Analysis App")
st.write("Enter text to analyze sentiment:")

user_input = st.text_area("Your text here:")

if st.button("Analyze"):
    response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
    result = response.json()
    st.subheader("Result")
    st.write(f"Sentiment: {result['sentiment']}")
    st.write(f"Polarity Score: {result['polarity']}")
