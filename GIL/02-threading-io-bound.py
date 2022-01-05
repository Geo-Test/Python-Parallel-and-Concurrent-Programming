from threading import Thread
import time

start = time.perf_counter()

def count_down(n):
    while n > 0:
        n -= 1

thread1 = Thread(target=count_down, args=(100000000,))
thread2 = Thread(target=count_down, args=(100000000,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.perf_counter()
print(end-start)

# For Example Execution Time : 37.43200210001669