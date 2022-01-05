from asyncio.tasks import create_task
import time
import asyncio

start = time.perf_counter()


async def some_task(name):
    print(f"Task {name} Started...")
    # print(asyncio.current_task())
    # print(asyncio.all_tasks())
    await asyncio.sleep(3)
    print(f"Task {name} Finished...")

async def main():
    t1 = asyncio.create_task(some_task("1"))
    t2 = asyncio.create_task(some_task("2"))
    t3 = asyncio.create_task(some_task("3"))

    await t1
    await t2
    await t3

asyncio.run(main())

end = time.perf_counter()
print(end-start)