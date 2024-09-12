# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="AIzaSyCKgoKI_62-I-IiLZc_3RxZjwSP6Q8_M8g")

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

import streamlit as st
import time

# Initialize our Streamlit app with a custom page title and icon
st.set_page_config(page_title="Gemini Application", page_icon="🌟", layout="centered")

# Add custom CSS for animations and styling, including dark theme adjustments
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #f0f0f0;
    }
    .stButton > button {
        background-color: #6c63ff;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #574bff;
        transform: scale(1.05);
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #6c63ff;
        animation: fadeIn 2s ease;
    }
    .response-box {
        margin-top: 20px;
        background-color: #2b2b2b;
        color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        animation: fadeInUp 1s ease;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    @keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page header with an animation
st.markdown('<h1 class="title">Gemini Application 🚀</h1>', unsafe_allow_html=True)

# Input field for user to enter a question
input_text = st.text_input("Ask your question:", key="input", placeholder="Type your question here...")

# Button for submitting the question
submit = st.button("Ask the Question")

# If the submit button is clicked
if submit:
    with st.spinner('Generating response...'):
        time.sleep(2)  # Simulating a delay for response generation
        response = get_gemini_response(input_text)

    # Display the response in a styled container with improved readability for dark theme
    st.markdown(
        f"""
        <div class="response-box">
            <h3>Response:</h3>
            <p>{response}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
