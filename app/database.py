import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Get Mongo URI and Database Name from .env file
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "dynamic_api_db")  # Default to 'dynamic_api_db' if not set in .env

client = MongoClient(MONGO_URI)
db = client[DB_NAME]  # Set the database to 'dynamic_api_db'

def get_collection(collection_name: str):
    return db[collection_name]
