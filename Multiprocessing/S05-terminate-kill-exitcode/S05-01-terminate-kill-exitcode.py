from multiprocessing import Process
import time


start = time.perf_counter()

def some_task(name):
    print(f"Process {name} Started.")
    time.sleep(3)
    print(f"Process {name} Finished.")
    raise Exception("Oops!!!")


if __name__ == "__main__":
    p1 = Process(target=some_task, args=("One", ), daemon=True)
    p2 = Process(target=some_task, args=("Two", ), daemon=True)
    
    p1.start()
    p2.start()

    print(p1.is_alive())
    print(p2.is_alive())

    p1.terminate() # SIGTERM
    p2.kill() # SIGKILL
    
    p1.join()
    p2.join()

    print(p1.is_alive())
    print(p2.is_alive())

    print(p1.exitcode)
    print(p2.exitcode)

    end = time.perf_counter()
    exe_time = end - start
    print(f"Execution Time: {exe_time} sec")


# terminate()
# kill()
# exitcode = {
#     "0": "Exit Without Any Erorr",
#     ">0": "Exit for Some Erorr",
#     "<0": "Exit By Signal (terminate or kill)",
# }
