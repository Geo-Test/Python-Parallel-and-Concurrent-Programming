import time

start = time.perf_counter()

def count_down(n):
    while n > 0:
        n -= 1

count_down(100000000)
count_down(100000000)

end = time.perf_counter()
print(end-start)

# For Example Execution Time : 21.104917199991178