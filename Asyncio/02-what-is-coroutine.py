import time
import asyncio

start = time.perf_counter()


async def some_task():
    print("Task Started...")
    await asyncio.sleep(3)
    print("Task Finished...")

print(asyncio.iscoroutinefunction(some_task))

asyncio.run(some_task())
asyncio.run(some_task())
asyncio.run(some_task())

end = time.perf_counter()
print(end-start)