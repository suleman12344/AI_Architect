import getpass
import os
import sys
import time
from pinecone import Pinecone, ServerlessSpec

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api import PINECONE_API


# Connect to Pinecone
pc = Pinecone(api_key=PINECONE_API)
print("Successfully connected to Pinecone API")

index_name = "2d-floorplan-suggestions"  # Change if desired

# Check if index already exists
existing_indexes = [index.name for index in pc.list_indexes()]
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Index '{index_name}' already exists. Skipping creation.")

# Connect to the index
index = pc.Index(index_name)
print("Index ready to use.")
print("Index name:", index_name)