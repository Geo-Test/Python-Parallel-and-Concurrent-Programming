import threading
import time

# threading.active_count()
# threading.current_thread()
# threading.enumerate # Return a list of all Thread objects currently active
# threading.main_thread()

"""enumerate() : Return a list of all Thread objects currently alive.

    The list includes daemonic threads, dummy thread objects created by
    current_thread(), and the main thread. It excludes terminated threads and
    threads that have not yet been started.
"""

def f():
    print("current_thread : ", threading.current_thread())
    print("Thread ID: ", threading.get_ident())
    print("active count: ", threading.active_count())
    print("Main Thread Object: ", threading.main_thread())
    print("Native ID: ", threading.get_native_id()) # Return the native integral Thread ID of the current thread assigned by the kernel
    time.sleep(3)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=f, daemon=False)
        t.start()
    

    print(threading.enumerate())
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue

        print(t.name)
        t.join()