tools=["cursor","vscode","pycharm","git","github"]
tools.sort()
print(tools)

model={"name":"intellijidea", "company":"jetbrains", "release_year":2001, "context_window":100000}
for key, value in model.items():
    print(f"{key}: {value}")

numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)

tools=["cursor","vscode","pycharm","git","github"]
ntools=[t for t in tools if len(t)>5]
print(ntools)