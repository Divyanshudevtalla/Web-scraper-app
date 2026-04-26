import asyncio
import aiohttp
from bs4 import BeautifulSoup  # for parsing HTML

urls = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com",
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_title(session, url):
    html = await fetch(session, url)
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.string if soup.title else "No title found"

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_title(session, url) for url in urls]
        titles = await asyncio.gather(*tasks)
        for url, title in zip(urls, titles):
            print(f"{url} → {title}")

asyncio.run(main())
