from typing import Dict, List
import asyncio
import time

# async def fetch_mock_api(url: str) -> Dict:
#     await asyncio.sleep(0.5)
#     return {"url": url, "status": "ok"}

# async def fetch_all_apis(urls: List[str]) -> List[Dict]:
#     tasks = [fetch_mock_api(url) for url in urls]
#     results = await asyncio.gather(*tasks)
#     return list(results)

# async def main():
#     urls = ["https://api.example.com/1", "https://api.example.com/2", "https://api.example.com/3", "https://api.example.com/4", "https://api.example.com/5"]
#     start_time = time.time()
#     results = await fetch_all_apis(urls)
#     end_time = time.time()
#     print(f"Time taken(concurrent): {end_time - start_time} seconds")
#     print(results)

#     start = time.time()
#     url1 = await fetch_mock_api("https://api.example.com/1")
#     url2 = await fetch_mock_api("https://api.example.com/2")
#     url3 = await fetch_mock_api("https://api.example.com/3")
#     url4 = await fetch_mock_api("https://api.example.com/4")
#     url5 = await fetch_mock_api("https://api.example.com/5")
#     end = time.time()
#     print(f"Time taken(sequential): {end - start} seconds")

# asyncio.run(main())


async def fetch_llm_response(model: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{model} responded"

async def main():
    tasks = {asyncio.create_task(fetch_llm_response("Claude", 0.3)), asyncio.create_task(fetch_llm_response("GPT-4", 0.7)), asyncio.create_task(fetch_llm_response("Gemini", 1.2))}
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first_task = done.pop().result()
    print(f"First task: {first_task}")
    done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
    second_task = done.pop().result()
    print(f"Second task: {second_task}")  
    done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
    third_task = done.pop().result()
    print(f"Third task: {third_task}")

asyncio.run(main())