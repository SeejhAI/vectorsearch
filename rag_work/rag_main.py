import google.generativeai as genai
import os
import os
from dotenv import load_dotenv
import requests
load_dotenv()


DB_URI: str = os.getenv("DB_URI")
API_KEY: str = os.getenv("API_KEY")
genai.configure(
    api_key=API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-pro')

response = model.generate_content(
          'Can I use retrieval-augmented generation using makersuit of gemini pro using python and how?')
print(response.text)
    #  The opposite of hot is cold.'
        