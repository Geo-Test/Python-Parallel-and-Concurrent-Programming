import time
import asyncio

start = time.perf_counter()


async def some_task():
    print("Task Started...")
    await asyncio.sleep(1)
    print("Task Finished...")

async def main():
    await some_task()
    await some_task()

asyncio.run(main())

end = time.perf_counter()
print(end-start)