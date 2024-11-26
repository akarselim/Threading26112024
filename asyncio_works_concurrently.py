import time
import asyncio
import aiohttp


urls = ['https://postman-echo.com/delay/3'] * 10

async def get_data(session, url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
        await asyncio.gather(*tasks)
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return json_array

asyncio.run(get_data_async_concurrently(urls))