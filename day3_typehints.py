from typing import List, Dict

def calculate_stats(numbers: List[float]) -> Dict[str, float]:
    minimum = min(numbers)
    maximum = max(numbers)
    s = sum(numbers)
    mean = s/len(numbers)
    return {"min": minimum, "max": maximum, "mean": mean}

print(calculate_stats([7.8, 9, 5.5]))


def search_models(models: List[Dict], min_context: int) -> List[Dict]:
    filtered = [model for model in models if model["context_window"] >= min_context]
    return filtered

models = [
    {"name": "claude", "context_window": 200000},
    {"name": "gpt4", "context_window": 128000},
    {"name": "tiny", "context_window": 4000}
]
print(search_models(models, 100000))