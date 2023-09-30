import asyncio
import random
import string
from datetime import datetime
from time import time

import aiohttp


async def fetch_url(session: aiohttp.ClientSession, url: str, data: dict[str, str]) -> time:
    response_time = time()
    await session.post(url, json=data)
    return time() - response_time


async def client(urls: list[str]) -> list[dict[str, str | int | datetime]]:
    # customers = [
    #     'USER#1',
    #     'USER#2',
    #     'USER#3',
    #     'USER#4',
    #     'USER#5',
    #     'USER#6',
    #     'USER#7',
    #     'USER#8',
    #     'USER#9',
    #     'USER#10',
    # ]
    customers = ['User']
    async with aiohttp.ClientSession() as session:
        response = None
        for _ in range(5):
            data = {
                'name': random.choice(customers),
                'text': ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
            }
            response = await fetch_url(session, random.choice(urls), data)
    return response


async def main():
    start = time()
    urls = ['http://127.0.0.1:8000/']
    tasks = [asyncio.create_task(client(urls)) for _ in range(10)]
    result = await asyncio.gather(*tasks)
    process_time = time() - start
    print(process_time)
    print(random.choice(result))
    print(1 / (process_time / 5_000))

if __name__ == '__main__':
    asyncio.run(main())
