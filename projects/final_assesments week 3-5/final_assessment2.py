from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()

def ask_groq(question, system_prompt):
    try:
        client=Groq(api_key=os.getenv("GROQ_API_KEY"))
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1000,
        )
        return response.choices[0].message.content
        
    except Exception as e:
        error_message = str(e)
        if "rate_limit" in error_message.lower() or "429" in error_message:
            return "Error: Rate limit reached. Please wait and try again."
        elif "authentication" in error_message.lower() or "401" in error_message:
            return "Error: Invalid API key. Check your .env file."
        elif "connection" in error_message.lower():
            return "Error: Connection failed. Check your internet."
        else:
            return f"Error: {error_message}"

system_prompt="You are a helpful assistant that can answer questions and help with tasks."
question="What is the capital of France?"
response=ask_groq(question, system_prompt)
print(response)