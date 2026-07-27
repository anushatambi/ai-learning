import asyncio
from typing import List, Dict
import random

async def fetch_price(item: str) -> dict:
    await asyncio.sleep(0.3)
    return {'item': item, 'price': random.uniform(10, 100)}

def check_price_change(old_price: float, new_price: float, threshold: float = 10.0) -> bool:
    percent_change=abs(new_price - old_price) / old_price * 100
    if percent_change>threshold:
        return True
    else:
        return False

async def monitor_prices(items: List[str]) -> None:
    previous_prices = {}
    i=0
    
    while i<3:
        tasks = [fetch_price(item) for item in items]
        results = await asyncio.gather(*tasks)
        for result in results:
            item = result['item']
            price = result['price']
            if item in previous_prices:
                if check_price_change(previous_prices[item], price):
                    print(f"Price of {item} changed by more than 10%")
            previous_prices[item] = price
        i+=1

asyncio.run(monitor_prices(['item1', 'item2', 'item3']))
