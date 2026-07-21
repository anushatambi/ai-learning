import asyncio
import time
import random

async def call_llm_api(semaphore: asyncio.Semaphore, call_id: int) -> str:
    async with semaphore:
        await asyncio.sleep(random.uniform(0.1, 1.0))
        if random.random() < 0.3:
            raise ValueError(f"Call {call_id}: Failed")
        return f"Call {call_id}: Success"

async def main():
    call_ids = list(range(10))
    semaphore = asyncio.Semaphore(3)
    start=time.time()
    tasks = [call_llm_api(semaphore,c) for c in call_ids]
    results=await asyncio.gather(*tasks, return_exceptions=True)
    elapsed = time.time() - start
    print(f"Processed 10 apis in {elapsed:.2f}s")
    fail_count=0
    success_count = 0
    for c, result in enumerate(results):
        if isinstance(result, Exception):
            fail_count += 1
        else:
            success_count+=1
    print(f"failed_count={fail_count}")
    print(f"success_count={success_count}")
    return list(results)

asyncio.run(main())