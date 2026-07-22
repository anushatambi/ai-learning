from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from .env

client = Groq()  # auto-reads the key

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Explain what a Python function is in 2 sentences"}
    ]
)

# Extract the actual text
print(response.choices[0].message.content)

# Also print token usage
print(f"\nTokens used — Input: {response.usage.prompt_tokens}, Output: {response.usage.completion_tokens}")


print(response.id)                          # unique ID for this call
print(response.model)                       # which model responded
print(response.choices[0].finish_reason)    # why it stopped ("stop" = normal)
print(response.usage.prompt_tokens)         # input tokens
print(response.usage.completion_tokens)     # output tokens
print(response.usage.total_tokens)          # total


#conversation loop
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

conversation_history = []  # this is the "memory"

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a strict Python teacher. Give short, direct answers only. No small talk."},
            *conversation_history   # unpack the rest of the history after system
        ]
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

print(chat("What is a Python list?"))
print("---")
print(chat("Can you give me an example?"))