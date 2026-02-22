import streamlit as st
import fitz
from utils.llm import get_llm_response

def run():
    st.title("📄 AI Contract Simplifier")

    file = st.file_uploader("Upload PDF Contract", type=["pdf"])

    if file:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        st.subheader("Simplified Summary")
        prompt = f"Explain this contract in simple terms:\n{text[:4000]}"
        result = get_llm_response(prompt)
        st.write(result)