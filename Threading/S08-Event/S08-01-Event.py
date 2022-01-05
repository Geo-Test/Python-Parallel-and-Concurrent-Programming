# For Example : (Event Trigger)
# 1) Task-main (Thread-Main) : define event as e 
# 2) Task1 (Thread1) : wait for e (blocking)
# 3) Task2 (Thread2) : wait for e (non block)
# 4) Task-main : e.set()
# 5) Task1: trigger  process 
# 6) Task2: trigger process 

import threading
import time

start = time.perf_counter()


def task1(e):
    print(f'Task1 : Started ({round(time.perf_counter()-start)} Sec)')
    event_is_set = e.wait()
    print(f'Task1 : Resume => Event set: {event_is_set} ({round(time.perf_counter()-start)} Sec)')


def task2(e, t):
    while not e.is_set():
        print(f'Task2 : Started ({round(time.perf_counter()-start)} Sec)')
        event_is_set = e.wait(t)
        print(f'Task2 : Resume (Non Blocking) => Event set: {event_is_set} ({round(time.perf_counter()-start)} Sec)')
        
        if event_is_set: print(f'Task2 : Resume (Processing Event) ({round(time.perf_counter()-start)} Sec)')
        else: print(f'Task2 : Doing Somethings... ({round(time.perf_counter()-start)} Sec)')


if __name__ == '__main__':
    e = threading.Event()

    t1 = threading.Thread(name='Blocking', target=task1, args=(e,))
    t1.start()

    t2 = threading.Thread(name='Non-blocking', target=task2, args=(e, 5))
    t2.start()

    # t1.join()
    # t2.join()

    print(f'Main Thread : Waiting before calling Event.set() ({round(time.perf_counter()-start)} Sec)')
    time.sleep(20)
    e.set()
    print(f'Main Thread : Event.set() ({round(time.perf_counter()-start)} Sec)')
