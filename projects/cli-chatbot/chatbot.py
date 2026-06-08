"""
CLI Chatbot — Day 10 Capstone Project
AI Engineer Learning Journey | Week 3-5

Uses: Groq API (llama-3.3-70b-versatile), dotenv, utils.py
Run: python chatbot.py
"""

import os
from groq import Groq
from dotenv import load_dotenv
from utils import save_conversation, load_conversation, print_welcome

# ── Load environment variables ──────────────────────────────────────────────
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ Error: GROQ_API_KEY not found in .env file.")
    print("   Add this line to your .env:  GROQ_API_KEY=your_key_here")
    exit(1)

# ── Groq client ──────────────────────────────────────────────────────────────
client = Groq(api_key=api_key)  #client=Groq() also works but it's better to always specify the api key as well

# ── System prompt — customise this to change the chatbot's personality ───────
SYSTEM_PROMPT = """You are a helpful AI learning assistant for Anusha, 
who is an AI Engineering student. You explain concepts clearly, 
use simple analogies, and keep answers concise unless asked for more detail.
When you give code examples, keep them short and focused."""

# ── Core chat function ────────────────────────────────────────────────────────
def chat(conversation_history: list, user_message: str) -> str:
    """
    Send a message to the Groq API and return the assistant's reply.
    conversation_history is updated in-place with both the user and assistant messages.
    """
    # Add the user's message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + conversation_history,
            max_tokens=1024,
            temperature=0.7
        )

        assistant_message = response.choices[0].message.content

        # Add the assistant's reply to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    except Exception as e:
        # Remove the user message we just added — so history stays clean
        conversation_history.pop()
        raise e


# ── Main loop ─────────────────────────────────────────────────────────────────
def main():
    print_welcome()

    conversation_history = []

    print("Commands:  'exit' or 'quit' to end  |  'history' to see past chats\n")

    while True:
        try:
            user_input = input("You: ").strip()

            # Skip empty input
            if not user_input:
                continue

            # Exit commands
            if user_input.lower() in ("exit", "quit"):
                print("\n💾 Saving conversation...")
                save_conversation(conversation_history)
                print("✅ Saved to chat_history.json")
                print("👋 Goodbye! Keep building!")
                break

            # Show past history command
            if user_input.lower() == "history":
                past = load_conversation()
                if past:
                    print(f"\n📂 Loaded {len(past)} messages from last session.\n")
                    conversation_history = past
                    print("✅ Previous conversation restored. Continue chatting!\n")
                else:
                    print("📭 No previous conversation found.\n")
                continue

            # Send message to API
            print("\nAssistant: ", end="", flush=True)
            reply = chat(conversation_history, user_input)
            print(reply)
            print()

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n⚠️  Interrupted! Saving conversation before exit...")
            if conversation_history:
                save_conversation(conversation_history)
                print("✅ Saved to chat_history.json")
            print("👋 Goodbye!")
            break

        except Exception as e:
            print(f"\n❌ API Error: {e}")
            print("   Check your API key and internet connection.\n")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()