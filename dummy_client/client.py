import asyncio
import random
import string
from datetime import datetime

import aiohttp


async def client(urls: list[str]) -> list[dict[str, str | int | datetime]]:
    customers = [
        'Abigail',
        'Alexandra',
        'Alison',
        'Amanda',
        'Amelia',
        'Amy',
        'Andrea',
        'Angela',
        'Anna',
        'Anne'
    ]
    responses = list()
    async with aiohttp.ClientSession() as session:
        for _ in range(20):
            data = {
                'name': random.choice(customers),
                'text': ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
            }
            response = await session.post(random.choice(urls), json=data)
            response = await response.json()
            responses.append(response)
    return responses


async def main():
    urls = ['http://127.0.0.1:9000/', 'http://127.0.0.1:9001/']
    tasks = [asyncio.create_task(client(urls)) for _ in range(10)]
    result = await asyncio.gather(*tasks)
    for item in result:
        for messanger in item:
            for message in messanger:
                print(message)
            print()


if __name__ == '__main__':
    asyncio.run(main())
