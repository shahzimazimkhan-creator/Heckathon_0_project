import streamlit as st
from utils.llm import get_llm_response

def run():
    st.title("🎤 AI Interview Coach")

    role = st.text_input("Job Role")
    answer = st.text_area("Your Answer")

    if st.button("Generate Question"):
        prompt = f"Give one interview question for {role} role."
        question = get_llm_response(prompt)
        st.write(question)

    if st.button("Evaluate My Answer"):
        prompt = f"Evaluate this interview answer and give feedback:\n{answer}"
        result = get_llm_response(prompt)
        st.write(result)