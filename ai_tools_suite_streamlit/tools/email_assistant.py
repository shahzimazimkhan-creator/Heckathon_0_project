import streamlit as st
from utils.llm import get_llm_response

def run():
    st.title("📧 Smart Email Assistant")

    email_text = st.text_area("Paste Email Content")

    if st.button("Summarize"):
        prompt = f"Summarize this email:\n{email_text}"
        result = get_llm_response(prompt)
        st.write(result)

    if st.button("Generate Professional Reply"):
        prompt = f"Write a professional reply to this email:\n{email_text}"
        result = get_llm_response(prompt)
        st.write(result)