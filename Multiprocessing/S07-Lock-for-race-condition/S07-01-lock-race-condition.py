import multiprocessing
import time

def desposit(balance):
    for i in range(500):
        time.sleep(0.001)
        balance.value += 1


def withdraw(balance):
    for i in range(500):
        time.sleep(0.001)
        balance.value -= 1

if __name__ == "__main__":
    balance = multiprocessing.Value("i", 500)
    p1 = multiprocessing.Process(target=desposit, args=(balance, ))
    p2 = multiprocessing.Process(target=withdraw, args=(balance, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(balance.value)