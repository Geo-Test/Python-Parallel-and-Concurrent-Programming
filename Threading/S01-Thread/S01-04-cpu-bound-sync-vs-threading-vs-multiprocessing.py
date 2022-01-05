from time import time

start = time()

def count_down(n):
    while n > 0:
        n -= 1

###############################################################
# Sync : Execution time for example : 17.773974657058716 sec
count_down(100000000)
count_down(100000000)
end = time()
print(f"Sequential: {end-start}") 

###############################################################
# Threading : Execution time for example : 20.466705083847046 sec
from threading import Thread

thread1 = Thread(target=count_down, args=(100000000,))
thread2 = Thread(target=count_down, args=(100000000,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time()
print(f"Threading: {end-start}")

###############################################################
# Multiprocessing : Execution time for example : 12.150790929794312 sec
from multiprocessing import Process

if __name__ == "__main__":
    p1 = Process(target=count_down, args=(100000000, ))
    p2 = Process(target=count_down, args=(100000000, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time()
    print(f"Multiprocessing: {end-start}")


