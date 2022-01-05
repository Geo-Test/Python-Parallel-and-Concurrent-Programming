import multiprocessing
import time

def some_task(name):
    print(f"Process {name} Started.")
    for i in range(0, 100000000):
        pass
    print(f"Process {name} Finished.")

if __name__ == "__main__":
    print(multiprocessing.cpu_count())

    start = time.perf_counter()
    p1 = multiprocessing.Process(target=some_task, args=("One", ))
    p2 = multiprocessing.Process(target=some_task, args=("Two", ))
    p3 = multiprocessing.Process(target=some_task, args=("Three", ))
    p4 = multiprocessing.Process(target=some_task, args=("Four", ))

    # start Processes 
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # join Processes 
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end = time.perf_counter()
    exe_time = end - start
    print(f"Execution Time: {exe_time} sec")

    # for example: Execution Time: 6.819241099990904 sec
