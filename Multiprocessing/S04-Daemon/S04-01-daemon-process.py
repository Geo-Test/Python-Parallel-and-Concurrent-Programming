from multiprocessing.context import Process
import time
import sys


start = time.perf_counter()

def some_task(name):
    print(f"Process {name} Started.")
    time.sleep(3)
    print(f"Process {name} Finished.")


if __name__ == "__main__":
    p1 = Process(target=some_task, args=("One", ), daemon=True)
    p2 = Process(target=some_task, args=("Two", ), daemon=True)
    p1.start()
    p2.start()

    # p1.join()
    # p2.join()

    end = time.perf_counter()
    exe_time = end - start
    print(f"Execution Time: {exe_time} sec")

    sys.exit()