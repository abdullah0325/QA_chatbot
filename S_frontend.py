import streamlit as st 
import requests

st.title("  Simple QA Chatbot ")

question = st.text_input("Enter your question:")

if question:
    try:
        response = requests.get("http://localhost:8000/chatbot", params={"question": question})
        if response.status_code == 200:
            st.write("Q  :-->", question)
            st.write("A  :-->", response.json())
        else:
            st.write(f"Error: {response.status_code}")
            
    except Exception as e:
        st.write(f"Error: {e}")