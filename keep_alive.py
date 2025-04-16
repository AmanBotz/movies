# keep_alive.py
import asyncio
import aiohttp
from info import URL

async def visit_url():
    if not URL:
        print("Error: URL not set")
        return
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(URL, timeout=10) as resp:
                print(f"Visited {URL} - Status Code: {resp.status}")
        except Exception as e:
            print(f"Error visiting {URL}: {e}")

async def keep_alive():
    while True:
        await visit_url()
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(keep_alive())