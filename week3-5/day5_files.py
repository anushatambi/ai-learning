def safe_convert(value):
    try:
        result = int(value)
    except ValueError:
        return None
    return result
print(safe_convert(42))
print(safe_convert("abc"))
print(safe_convert(3.9))


with open("day5_learning.txt", "w") as f:
    f.write("I learned variables and data types\n")
    f.write("I learned functions and args\n")
    f.write("I learned error handling\n")

with open("day5_learning.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}. {line.strip()}")


import json
tools = {"Claude": "AI assistant for learning and coding", "Cursor":"AI assisted coding", "GitHub":"place to store data on the internet"}
with open("tools.json","w") as f:
    json.dump(tools, f, indent=2)

with open("tools.json","r") as f:
    loaded=json.load(f)
    print(loaded)