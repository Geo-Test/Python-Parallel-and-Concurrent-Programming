import asyncio
import time
import urllib
import aiohttp

URL = "https://www.python.org/"
COUNTER_REQUEST = 10

def get_site_data_syn(request_number):
    print(f"Synchronous request {request_number}")
    start = time.perf_counter()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader('Date')
    print(f"Synchronous request {request_number} Finished ==> {datetime}, {time.perf_counter()-start}")
    return datetime


async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


async def get_site_data_async(request_number):
    print(f"Asynchronous request {request_number}")
    start = time.perf_counter()
    response = await aiohttp_get(URL)
    datetime = response.headers.get('Date')
    print(f"Asynchronous request {request_number} Finished ==> {datetime}, {time.perf_counter()-start}")
    response.close()
    return datetime


def synchronous():
    start = time.perf_counter()
    for i in range(COUNTER_REQUEST):
        get_site_data_syn(i)
    print(f"Execution time (synchronous) : {time.perf_counter()-start}")


async def asynchronous():
    start = time.perf_counter()
    tasks = [asyncio.create_task(get_site_data_async(i)) for i in range(COUNTER_REQUEST)]
    for task in tasks:
        await task
    print(f"Execution time (asynchronous) : {time.perf_counter()-start}")


synchronous()
asyncio.run(asynchronous())