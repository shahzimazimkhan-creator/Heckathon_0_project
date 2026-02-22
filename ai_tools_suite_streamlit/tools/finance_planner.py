import streamlit as st
from utils.llm import get_llm_response

def run():
    st.title("💰 AI Personal Finance Planner")

    income = st.number_input("Monthly Income")
    expenses = st.number_input("Monthly Expenses")

    if st.button("Generate Financial Advice"):
        prompt = f"My income is {income} and expenses are {expenses}. Give budgeting advice."
        result = get_llm_response(prompt)
        st.write(result)