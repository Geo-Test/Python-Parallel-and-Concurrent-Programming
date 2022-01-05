import threading
import time

# global variable x
x = 0
  
def thread_task(n):
    global x
    for _ in range(n):
        x += 1 # critical section : Gil Can Stop Race Condition(Only one thread can run at a time)
        time.sleep(0.0001)

  
def main_task():
    global x
    # setting global variable x as 0
    x = 0
  
    # creating threads
    t1 = threading.Thread(target=thread_task, args=(100, ))
    t2 = threading.Thread(target=thread_task, args=(100, ))
  
    # start threads
    t1.start()
    t2.start()
  
    # wait until threads finish their job
    t1.join()
    t2.join()
  
if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))