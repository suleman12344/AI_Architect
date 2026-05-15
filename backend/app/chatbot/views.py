from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.chains import RetrievalQA
from langchain_core.language_models.llms import LLM
from .retriver import retriever  # relative import

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API")
if not api_key:
    raise ValueError("Please set the GOOGLE_API environment variable in your .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Define LangChain wrapper for Gemini 2 Flash
class Gemini2Flash(LLM):
    model_name: str = "gemini-2.0-flash-exp"
    temperature: float = 1.0
    top_p: float = 1.0
    max_tokens: int | None = None

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

# Initialize LLM and QA chain once
llm = Gemini2Flash(temperature=0.1)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# DRF API View
class ChatbotAnswerView(APIView):
    def post(self, request):
        query = request.data.get("query", "").strip()

        if not query:
            return Response({"error": "Query cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        # Optional random tone to make responses more dynamic
        random_noise = random.choice(["", " Please be creative.", " Add a different perspective."])
        final_query = query + random_noise

        try:
            result = qa_chain.invoke({"query": final_query})
            answer = result['result']

            # ✅ Remove leading phrases like “Based on the provided context,”
            cleaned_answer = re.sub(
                r"^(Based on the provided context,|According to the information provided,|According to the context,)\s*",
                "", 
                answer.strip(),
                flags=re.IGNORECASE
            )

            return Response({"answer": cleaned_answer})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
