import pymongo
import os
from dotenv import load_dotenv
import requests
load_dotenv()


DB_URI: str = os.getenv("DB_URI")
client = pymongo.MongoClient(DB_URI)
db = client.sample_mflix
collection = db.movies

hf_token: str = os.getenv("HF_TOKEN")
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json= {"inputs": text, "options": {"wait_for_model": True}}
    )
    
    if response.status_code != 200:
        raise ValueError(f"Request failed with status {response.status_code}: {response.text}")
    
    return response.json()


# print(generate_embedding("freecodecamo is awesome"))

if __name__ == "__main__":
    for doc in collection.find({"plot": {"$exists": True}}):
        print(f"Working on {doc['_id']}")
        plot = doc["plot"]
        embedding = generate_embedding(plot)
        collection.update_one({"_id": doc["_id"]}, {"$set": {"embedding": embedding}})