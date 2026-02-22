import streamlit as st
from tools import email_assistant, data_insight, contract_simplifier, interview_coach, finance_planner

st.set_page_config(page_title="5 AI Tools Suite", layout="wide")

st.title("🚀 5 AI Tools & Apps - Agentic Productivity Suite")

menu = st.sidebar.radio(
    "Select Tool",
    [
        "Smart Email Assistant",
        "AI Data Insight Generator",
        "AI Contract Simplifier",
        "AI Interview Coach",
        "AI Personal Finance Planner"
    ]
)

if menu == "Smart Email Assistant":
    email_assistant.run()

elif menu == "AI Data Insight Generator":
    data_insight.run()

elif menu == "AI Contract Simplifier":
    contract_simplifier.run()

elif menu == "AI Interview Coach":
    interview_coach.run()

elif menu == "AI Personal Finance Planner":
    finance_planner.run()