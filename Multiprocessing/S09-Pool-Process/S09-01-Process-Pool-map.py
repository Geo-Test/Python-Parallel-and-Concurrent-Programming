from multiprocessing import Pool
import time


start = time.perf_counter()

def show(name):

    print(f"Starting {name}...")
    for i in range(0, 100000000):pass
    print(f"Ending {name}...")

if __name__ == "__main__":
    names = ["Task1", "Task2", "Task3", "Task4"]

    pool = Pool(processes=2)
    pool.map(show, names)

    pool.close()
    pool.join()

    end = time.perf_counter()
    print(end - start)