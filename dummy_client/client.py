import asyncio
import random
import string
import aiohttp


async def fetch(url: str, data: dict[str, str]):
    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json=data)
        response_json = await response.json()
        return response_json


async def post_api(urls: list[str]):
    customers = ['Nikita', 'Malik', 'Animus', 'Foo', 'Bar']
    tasks = [
        asyncio.create_task(
            fetch(
                random.choice(urls),
                data={
                    'name': random.choice(customers),
                    'text': ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
                }
            )
        )
        for _ in range(50)]
    response = await asyncio.gather(*tasks)
    return response


async def main():
    urls = ['http://127.0.0.1:8000/']
    for _ in range(100):
        response = await post_api(urls)
        for item in response:
            for message in item:
                print(message)
            print()


if __name__ == '__main__':
    asyncio.run(main())
