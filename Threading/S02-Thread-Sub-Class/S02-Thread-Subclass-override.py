from threading import Thread
import time


start = time.perf_counter()

def some_task(name, delay):
    print(f"Thread {name} Started.")
    time.sleep(delay)
    print(f"Thread {name} Finished.")


class MyThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        some_task(self.name, self.delay)


t1 = MyThread(name="One", delay=3)
t2 = MyThread(name="Two", delay=3)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.perf_counter()
exe_time = end - start
print(f"Execution Time: {exe_time} sec")