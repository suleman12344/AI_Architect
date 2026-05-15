from pinecone import Pinecone as PineconeClient
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API = os.getenv("GOOGLE_API")
PINECONE_API = os.getenv("PINECONE_API")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")

# Initialize Pinecone client
pc = PineconeClient(api_key=PINECONE_API, environment=PINECONE_ENV)

# Get index client
pinecone_index = pc.Index("2d-floorplan-suggestions")

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=GOOGLE_API
)

# Initialize LangChain Pinecone vectorstore with new package
vectorstore = LangchainPinecone(pinecone_index, embeddings)

# Use retriever
retriever = vectorstore.as_retriever()

