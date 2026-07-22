import json
import os

def save_conversation(messages, filename="chat_history.json"):
    with open(filename, "w") as f:
        json.dump(messages, f, indent=2)
    print(f"\n💾 Conversation saved to {filename}")

def load_conversation(filename="chat_history.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def print_welcome():
    print("=" * 40)
    print("   🤖 CLI Chatbot — Powered by Groq")
    print("=" * 40)
    print("Type 'exit' or 'quit' to end the chat")
    print("=" * 40 + "\n")