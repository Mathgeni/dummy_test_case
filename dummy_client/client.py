import asyncio
import random
import string
from datetime import datetime

import aiohttp


async def client(urls: list[str]) -> list[dict[str, str | int | datetime]]:
    customers = [
        'Youson Clark',
        'Zink Wilson',
        'Yoder Johnson',
        'Zeis Lewis',
        'Yakley Robinson',
        'Yates Ross',
        'Yorston Olsen',
        'Zbikowski Robinson',
        'Yeomans Haugen',
        'Zillgitt Pedersen',
    ]
    responses = list()
    async with aiohttp.ClientSession() as session:
        for _ in range(100):
            data = {
                'name': random.choice(customers),
                'text': ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
            }
            response = await session.post(random.choice(urls), json=data)
            response = await response.json()
            responses.append(response)
    return responses


async def main():
    urls = ['http://127.0.0.1:8000/']
    tasks = [asyncio.create_task(client(urls)) for _ in range(50)]
    result = await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
