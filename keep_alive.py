import asyncio
import aiohttp
from info import URL

async def visit_url():
    if URL:
        try:
            async with aiohttp.ClientSession() as s, s.get(URL, timeout=10) as _: pass
        except: pass

async def keep_alive():
    while True:
        await visit_url()
        await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(keep_alive())