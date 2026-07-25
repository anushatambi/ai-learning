import asyncio
from typing import List, Dict
import random
import time

async def fetch_model_info(model_name: str) -> dict:
    await asyncio.sleep(0.3)
    if model_name.startswith('bad_'):
        raise ValueError(f"Bad model name: {model_name}")
    else:
        return {'name': model_name, 'response_time': random.uniform(0.1, 0.5), 'status': 'ok'}

async def batch_fetch(models: List[str], max_concurrent: int) -> List[dict]:
    semaphore = asyncio.Semaphore(max_concurrent)

    async def fetch_with_limit(model_name: str) -> dict:
        async with semaphore:
            return await fetch_model_info(model_name)

    tasks = [fetch_with_limit(m) for m in models]
    return list(await asyncio.gather(*tasks, return_exceptions=True))

async def main():
    models = ["gpt-4", "bad_model1", "llama-3", "claude-3", "bad_model2", "gemini", "mistral", "phi-3"]
    start = time.time()
    results = await batch_fetch(models, max_concurrent=3)
    elapsed = time.time() - start
    print(f"Processed {len(results)} models in {elapsed:.2f}s") 
    print(results)
    fail_count=0
    for result in results:
        if isinstance(result, Exception):
            fail_count += 1
    print(f"Failed to fetch {fail_count} models")

asyncio.run(main())