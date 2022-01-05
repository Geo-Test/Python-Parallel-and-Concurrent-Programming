from concurrent.futures import ProcessPoolExecutor
import time


start = time.perf_counter()

def some_task(name):
    print(f"Process {name} Started.")
    time.sleep(3)
    print(f"Process {name} Finished.")


if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=4) as executor:
        process_names = ["Process1", "Process2", "Process3", "Process4"]
        executor.map(some_task, process_names)

    end = time.perf_counter()
    exe_time = end - start
    print(f"Execution Time: {exe_time} sec")
