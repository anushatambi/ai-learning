# 🤖 CLI Chatbot

A command-line AI chatbot built with Python and the Groq API.  
This is my Week 3–5 capstone project from my AI Engineer learning journey.

---

## 📌 What It Does

- Accepts your messages in the terminal
- Sends them to an LLM (Llama 3.3 70B via Groq)
- Prints the assistant's reply
- Remembers the full conversation (multi-turn memory)
- Saves the conversation to `chat_history.json` when you exit
- Handles errors gracefully (missing API key, network issues, Ctrl+C)

---

## 🗂️ Project Structure

```
cli-chatbot/
├── chatbot.py       # Main app — run this
├── utils.py         # Helper functions (save, load, welcome)
├── .env             # Your API key (never commit this!)
├── .gitignore       # Ensures .env is not pushed to GitHub
└── README.md        # This file
```

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/anushatambi/ai-learning
cd projects/cli-chatbot
```

**2. Install dependencies**
```bash
pip install groq python-dotenv
```

**3. Add your API key**

Create a `.env` file in the project folder:
```
GROQ_API_KEY=your_key_here
```
Get a free key at: https://console.groq.com

**4. Run the chatbot**
```bash
python chatbot.py
```

---

## 💬 Usage

```
You: What is a Python decorator?
Assistant: A decorator is a function that wraps another function...

You: Give me a simple example.
Assistant: Sure! Here's the simplest decorator...

You: exit
💾 Saving conversation...
✅ Saved to chat_history.json
👋 Goodbye! Keep building!
```

**Commands:**
| Command | What it does |
|---------|-------------|
| `exit` or `quit` | Saves and exits |
| `history` | Loads your previous conversation |
| `Ctrl+C` | Emergency exit — still saves |

---

## 🧠 Concepts Used

| Concept | Where |
|---------|-------|
| `os` + `dotenv` | Loading API key securely |
| `try/except` | Graceful error handling |
| Functions + type hints | `chat()`, `save_conversation()` |
| JSON file I/O | Saving/loading chat history |
| OOP-style thinking | Conversation history as a list of dicts |
| while loop | Main chat loop |
| `if __name__ == "__main__"` | Entry point guard |

---

## 🔧 Customisation

Change the chatbot's personality by editing `SYSTEM_PROMPT` in `chatbot.py`:

```python
SYSTEM_PROMPT = """You are a strict Python teacher who gives 
short, no-nonsense answers only."""
```

---

## 📚 Part of My AI Engineer Journey

This project is part of my structured AI Engineer learning plan.  
Built across Week 3–5 covering Python Core for AI.

**Skills practised:** Python · Groq API · JSON · Error Handling · Modules · OOP

🔗 [View my full learning journey repo](https://github.com/anushatambi/ai-learning)