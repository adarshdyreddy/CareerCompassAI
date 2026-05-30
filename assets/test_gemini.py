import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

st.title("Gemini API Test")

st.write("API Key Loaded:")
st.code(api_key)

if api_key:
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)

        # Create model
        model = genai.GenerativeModel("gemini-2.0-flash")

        if st.button("Test Gemini API"):
            response = model.generate_content("What is Python?")

            st.success("Gemini Connected Successfully!")
            st.subheader("Response:")
            st.write(response.text)

    except Exception as e:
        st.error(f"Gemini Error: {e}")

else:
    st.error("API Key Not Found in .env file")