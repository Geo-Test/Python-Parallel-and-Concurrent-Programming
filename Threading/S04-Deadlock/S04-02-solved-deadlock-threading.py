import threading
import time

l1 = threading.Lock()
l2 = threading.Lock()

start = time.perf_counter()

def f1(name):
    print('thread',name,'about to lock l1')
    l1.acquire()
    print('thread',name,'has lock l1')
    time.sleep(3)
    l1.release()

    print('thread',name,'about to lock l2')
    l2.acquire()
    print('thread',name,'run without deadlock')
    l2.release()

def f2(name):
    print('thread',name,'about to lock l2')
    
    l2.acquire()
    print('thread',name,'has lock l2')
    time.sleep(3)
    l2.release()

    print('thread',name,'about to lock l1')
    l1.acquire()
    print('thread',name,'run without deadlock')
    l1.release()

if __name__ == '__main__':
    t1=threading.Thread(target=f1, args=['t1',])
    t2=threading.Thread(target=f2, args=['t2',])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()
    print(end-start)
