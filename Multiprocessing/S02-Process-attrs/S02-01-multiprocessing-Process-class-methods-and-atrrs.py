import multiprocessing
import os
import time


def some_task(name):
    print(f"Process {name} Started.")
    print("Current Process: ", multiprocessing.current_process())
    print("Process ID : ", os.getpid())
    print("Process Parent ID: ", os.getppid())
    
    time.sleep(4)
    print(f"Process {name} Finished.")


if __name__ == "__main__":
    
    start = time.perf_counter()
    print("CPU Count: ", multiprocessing.cpu_count())

    p1 = multiprocessing.Process(target=some_task, args=("One", ))
    p2 = multiprocessing.Process(target=some_task, args=("Two", ))
    
    # start Processes 
    p1.start()
    p2.start()

    # join Processes 
    p1.join()
    p2.join()

    end = time.perf_counter()
    exe_time = end - start
    print(f"Execution Time: {exe_time} sec")


# Process.is_alive() : check Process is alive or not
# Process.exitcode : return exit code (3 states: 0 or >0 or <0) 
# Process.ident : return ProcessID 
# Process.pid : return ProcessID 

# multiprocessing.current_process()  
# multiprocessing.active_children()

# os.getpid() : return ProcessID 
# os.getppid() : return Parent ProcessID 