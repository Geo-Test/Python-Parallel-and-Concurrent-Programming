from multiprocessing import Process


numbers = []


def task1():
    global numbers
    numbers += [1, 2, 3]
    print(numbers)


def task2():
    global numbers
    numbers += [4, 5, 6]
    print(numbers)


if __name__ == "__main__":
    p1 = Process(target=task1, )
    p2 = Process(target=task2, )

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(numbers)