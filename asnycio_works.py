import threading
import time
import requests
import asyncio
import aiohttp

urls = ['https://postman-echo.com/delay/3'] * 10

async def get_data_async_but_as_wrapper(urls):
    st = time.time()
    json_array = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                json_array.append(await resp.json())
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return json_array

asyncio.run(get_data_async_but_as_wrapper(urls))

