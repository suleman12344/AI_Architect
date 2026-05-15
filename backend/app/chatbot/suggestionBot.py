from langchain.chains import RetrievalQA
from retriver import retriever  # your existing retriever
import google.generativeai as genai
from dotenv import load_dotenv
import os
from langchain_core.language_models.llms import LLM
import random
load_dotenv()

# Configure Google Generative AI with the correct environment variable
api_key = os.getenv("GOOGLE_API")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable in your .env file")

genai.configure(api_key=api_key)

# Minimal LangChain wrapper for Gemini‑2‑Flash
class Gemini2Flash(LLM):
    """LangChain‑style LLM wrapper around google.generativeai GenerativeModel."""
    model_name: str = "gemini-2.0-flash-exp"  # <— change if Google renames
    temperature: float = 1.0
    top_p: float = 1.0
    max_tokens: int | None = None  # forward‑compat

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._model = genai.GenerativeModel(
            self.model_name,
            generation_config=genai.GenerationConfig(
                temperature=self.temperature,
                top_p=self.top_p,
                max_output_tokens=self.max_tokens,
            ),
        )

    @property
    def _llm_type(self) -> str:
        return "gemini_2_flash"

    def _call(self, prompt: str, stop: list[str] | None = None, **kwargs) -> str:
        response = self._model.generate_content(prompt)
        return response.text


# Build the Retrieval‑QA chain
llm = Gemini2Flash(temperature=0.1)  # tweak temp / top_p here if desired

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,  # your existing vector / BM25 retriever
)
def get_answer(query: str) -> str:
    print("inbetween")
    """Get an answer to a query using the RetrievalQA chain."""
    if not query.strip():
        raise ValueError("Query cannot be empty.")
    
    random_noise = random.choice(["", " Please be creative.", " Add a different perspective."])
    final_query = query + random_noise

    result = qa_chain.invoke({"query": final_query})
    return result['result']  # Adjust based on your RetrievalQA output structure
# Quick smoke test
if __name__ == "__main__":
    query = input("Enter your query: ")
    if not query.strip():
        print("Query cannot be empty.")
        exit(1)
    random_noise = random.choice(["", " Please be creative.", " Add a different perspective."])
    final_query = query + random_noise

    result = qa_chain.invoke({"query": final_query})
    print(result)
