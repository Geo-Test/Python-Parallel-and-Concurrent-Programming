from threading import Thread
import time


start = time.perf_counter()

def some_task(name, delay):
    print(f"Thread {name} Started.")
    time.sleep(delay)
    print(f"Thread {name} Finished.")


t1 = Thread(target=some_task, args=("One", 3, ), daemon=True) # daemon = False (by default)
t2 = Thread(target=some_task, args=("Two", 3, ), daemon=True) # daemon = False (by default)

t1.start()
t2.start()

# t1.join()
# t2.join()

end = time.perf_counter()
exe_time = end - start
print(f"Execution Time: {exe_time} sec")