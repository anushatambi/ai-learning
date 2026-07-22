import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pathlib import Path

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(api_key=groq_api_key,model="openai/gpt-oss-20b")
response=llm.invoke("What is the capital of france?")
print(response)

