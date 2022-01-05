import multiprocessing
import time


def some_task(name, delay):
    print(f"Process {name} Started.")
    time.sleep(delay)
    print(f"Process {name} Finished.")


# Customize Process
class SomeTaskProcess(multiprocessing.Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay


    def run(self):
        some_task(self.name, self.delay)


if __name__ == "__main__":
    
    start = time.perf_counter()
    print("CPU Count: ", multiprocessing.cpu_count())

    # p1 = multiprocessing.Process(target=some_task, args=("One", ))
    # p2 = multiprocessing.Process(target=some_task, args=("Two", ))
    p1 = SomeTaskProcess("One", 3)
    p2 = SomeTaskProcess("Two", 8)

    # start Processes 
    p1.start()
    p2.start()

    # join Processes 
    p1.join()
    p2.join()

    end = time.perf_counter()
    exe_time = end - start
    print(f"Execution Time: {exe_time} sec")
