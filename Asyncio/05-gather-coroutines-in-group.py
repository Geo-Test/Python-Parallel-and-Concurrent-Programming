import time
import asyncio

start = time.time()

async def task1(name):
    print(f"{name} Started")
    await asyncio.sleep(5)
    print(f"{name} Finished")

async def task2(name):
    print(f"{name} Started")
    await asyncio.sleep(5)
    print(f"{name} Finished")

async def task3(name):
    print(f"{name} Started")
    await asyncio.sleep(1)
    print(f"{name} Finished")


async def main():
    tasks = [task1("task1"), task2("task2"), task3("task3")]
    await asyncio.gather(*tasks)


asyncio.run(main())
    
    
    
