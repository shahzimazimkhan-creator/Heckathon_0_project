import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.llm import get_llm_response

def run():
    st.title("📊 AI Data Insight Generator")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.write(df.head())

        st.subheader("Basic Statistics")
        st.write(df.describe())

        if st.button("Generate AI Insights"):
            prompt = f"Analyze this dataset summary and give insights:\n{df.describe().to_string()}"
            result = get_llm_response(prompt)
            st.write(result)

        numeric_cols = df.select_dtypes(include=["number"]).columns
        if len(numeric_cols) > 0:
            st.subheader("Quick Chart")
            fig, ax = plt.subplots()
            df[numeric_cols[0]].plot(kind="hist", ax=ax)
            st.pyplot(fig)