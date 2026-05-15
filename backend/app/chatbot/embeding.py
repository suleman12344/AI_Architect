from langchain_google_genai import GoogleGenerativeAIEmbeddings
from creating_database import index
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api import GOOGLE_API
print ("embeding index",index)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=GOOGLE_API
)
#vector = embeddings.embed_query("hello, this is muhammad suleman and i am learning agentic ai. and hopefully i will be able to learn it")

#vector store we can easily use other vector datastore like cromma by just changing the vectorstore

from langchain_pinecone import PineconeVectorStore

vector_store = PineconeVectorStore(index=index, embedding=embeddings)