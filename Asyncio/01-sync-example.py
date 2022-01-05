import time

start = time.perf_counter()


def some_task():
    print("Task Started...")
    time.sleep(3)
    print("Task Finished...")


some_task()
some_task()
some_task()

end = time.perf_counter()
print(end-start)