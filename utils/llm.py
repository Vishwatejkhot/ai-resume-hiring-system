from langchain_groq import ChatGroq
import streamlit as st
import time


def get_llm():
    api_key = st.secrets["GROQ_API_KEY"]

    llm = ChatGroq(
        groq_api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=800
    )

    return llm


def safe_invoke(llm, prompt):
    while True:
        try:
            return llm.invoke(prompt)

        except Exception as e:

            if "rate_limit" in str(e):
                print("Rate limit reached. Waiting 10 seconds...")
                time.sleep(10)

            else:
                raise e