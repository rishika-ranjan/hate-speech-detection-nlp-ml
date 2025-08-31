import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load dataset (optional if you need it)
tweet_df = pd.read_csv('hateDetection_train.csv')

# App title
st.title("Hate Speech Detection on Twitter")

# Input from user
user_input = st.text_area("Enter a tweet to check:")

# Simple ML model prediction simulation
def predict_hate(text):
    # Replace this with your trained ML model prediction
    if "hate" in text.lower():
        return 1
    else:
        return 0

if st.button("Predict"):
    result = predict_hate(user_input)
    if result == 1:
        st.error("⚠️ Hate Speech Detected!")
    else:
        st.success("✅ Not Hate Speech")
