import time


def some_task(name):
    print(f"Process {name} Started.")
    for i in range(0, 100000000):
        pass
    print(f"Process {name} Finished.")


start = time.perf_counter()
some_task("One")
some_task("Two")
some_task("Three")
some_task("Four")
end = time.perf_counter()
exe_time = end - start
print(f"Execution Time: {exe_time} sec")

# for example: Execution Time: 14.556302800003323 sec
