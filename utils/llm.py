from langchain_groq import ChatGroq
import time
import streamlit as st
#import os
#from dotenv import load_dotenv

#load_dotenv()

def get_llm():

    llm = ChatGroq(
        #groq_api_key=os.getenv("GROQ_API_KEY"),
        api_key = st.secrets["GROQ_API_KEY"]
        model="openai/gpt-oss-120b",
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