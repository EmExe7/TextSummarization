import streamlit as st
from transformers import pipeline

# Load the sentiment model and summarization pipeline
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

# Sentiment analysis section (your existing code)
# ...

# Text Summarization Section
st.header("Text Summarization")
input_text = st.text_area("Enter the text you want to summarize:")

if st.button("Generate Summary"):
    if input_text:  # Check if input_text is not empty
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.write("Summary:")
        st.write(summary[0]['summary_text'])  # Display the summary
    else:
        st.write("Please enter some text to summarize.")