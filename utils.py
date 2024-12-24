import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("Answer the following question: {question}")

output_parser = StrOutputParser()

qa_chain = prompt |model | output_parser

def get_response(question):
    if question:
        try:
            response = qa_chain.invoke({"question":question})
            return response
        except Exception as e:
            return str(e)
        else:
            return "Please ask a question."


