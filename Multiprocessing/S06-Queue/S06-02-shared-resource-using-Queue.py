from multiprocessing import Process, Queue


numbers = []


def task1(queue):
    numbers = queue.get()
    numbers += [1, 2, 3]
    queue.put(numbers)
    print(numbers)


def task2(queue):
    numbers = queue.get()
    numbers += [4, 5, 6]
    queue.put(numbers)
    print(numbers)


if __name__ == "__main__":
    q = Queue()
    q.put(numbers)

    p1 = Process(target=task1, args=(q, ))
    p2 = Process(target=task2, args=(q, ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(q.get())