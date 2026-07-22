import json

def get_large_context_models(filename):
    with open(filename,"r") as f:
        models=json.load(f)

    filtered = [model for model in models if model["context_window"] > 100000]
    
    sorted_models = sorted(filtered, key=lambda m: m["context_window"], reverse=True)
    return sorted_models

result=get_large_context_models("ai_models.json")
for model in result:
    print(f"{model['name']} — {model['context_window']:,} tokens")
