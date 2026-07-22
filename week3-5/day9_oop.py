import json

class Conversation:
    def __init__(self, model_name):
        self.model_name = model_name
        self.messages = []        # list of dicts
        self.total_tokens = 0     # int

    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_history(self):
        return self.messages

    def summarise(self):
        print(f"Model: {self.model_name}")
        print(f"Messages: {len(self.messages)}")
        print(f"Total tokens used: {self.total_tokens}")

    def __str__(self):
        return f"Conversation({self.model_name}, {len(self.messages)} messages)"


class SavedConversation(Conversation):
    def __init__(self, model_name, filename):
        super().__init__(model_name)   # run Conversation's __init__
        self.filename = filename

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump(self.messages, f, indent=2)
        print(f"Saved to {self.filename}")


# Use it
convo = SavedConversation("llama-3.3-70b-versatile", "chat_history.json")

convo.add_message("user", "What is a Python class?")
convo.add_message("assistant", "A class is a blueprint for creating objects.")
convo.add_message("user", "Can you give an example?")
convo.add_message("assistant", "Sure! class Dog: def __init__(self, name): self.name = name")

convo.total_tokens = 120

print(convo)           # __str__
convo.summarise()      # prints stats
convo.save_to_file()   # saves to JSON