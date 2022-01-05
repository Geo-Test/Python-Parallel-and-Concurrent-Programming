from concurrent.futures import ThreadPoolExecutor
import time


start = time.perf_counter()

def some_task(name, delay):
    print(f"Thread {name} Started.")
    time.sleep(delay)
    print(f"Thread {name} Finished.")


names = ["One", "Two", "Three", "Four"]
delay = [3, 3, 3, 3]

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(some_task, names, delay)


end = time.perf_counter()
exe_time = end - start
print(f"Execution Time: {exe_time} sec")