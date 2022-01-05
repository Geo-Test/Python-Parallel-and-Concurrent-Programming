from multiprocessing import Pool, cpu_count, Manager
import time, os


start = time.perf_counter()
done_tasks = []


def on_task_done(results):
    done_tasks.append(results)


def show(name, procs):
    pid = os.getpid()
    procs[pid] = True

    print(f"Starting {name}...")
    for i in range(0, 100000000):pass
    print(f"Ending {name}...")


    procs[pid] = False
    return f"{name}"

if __name__ == "__main__":
    names = ["Task1", "Task2", "Task3", "Task4"]

    m = Manager()
    procs = m.dict()
    pool = Pool(processes=2)
    print(cpu_count())
    # pool.map(show, names)
    for name in names:
        pool.apply_async(show, args=(name, procs), callback=on_task_done)

    while len(done_tasks) < len(names):
        pids = [pid for pid, running in procs.items() if running]
        print('running jobs:', pids)
        time.sleep(1)

    print('results:', done_tasks)

    pool.close()
    pool.join()

    end = time.perf_counter()
    print(end - start)