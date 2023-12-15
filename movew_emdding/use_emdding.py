import pymongo
import os
from dotenv import load_dotenv
import requests
from movie_recs import generate_embedding
load_dotenv()


DB_URI: str = os.getenv("DB_URI")
client = pymongo.MongoClient(DB_URI)
db = client.sample_mflix
collection = db.movies

hf_token: str = os.getenv("HF_TOKEN")
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


query = "imaginary characters from outer space at war"

results =collection.aggregate([
    {
        "$vectorSearch": {
            "queryVector": generate_embedding(query),
            "path": "embedding",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch"
    }
    }
])

for document in results:
    print(f"movie name: {document['title']}, \nMovie Plot: {document['plot']}\n")

