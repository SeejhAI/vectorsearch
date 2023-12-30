from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms.google_palm import GooglePalm
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import os
from dotenv import load_dotenv
load_dotenv()

DB_URI: str = os.getenv("DB_URI")
API_KEY: str = os.getenv("API_KEY")