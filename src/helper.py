import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
import google.generativeai as genai
from apify_client import ApifyClient


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_gemini(prompt, max_tokens=500):
    """
    Sends a prompt to the Gemini API and returns the response.
    
    Args:
        prompt (str): The prompt to send to Gemini.
        max_tokens (int): The maximum number of tokens in the response.
        
    Returns:
        str: The response from the Gemini API.
    """ 
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.5,
            "max_output_tokens": max_tokens
        }
    )
    return response.text
