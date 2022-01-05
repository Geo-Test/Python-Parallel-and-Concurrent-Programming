from threading import Thread
import time
import requests

start = time.perf_counter()


def get_site_data(url):
    response = requests.get(url)
    return response.text


thread1 = Thread(target=get_site_data, args=('https://www.python.org/',))
thread2 = Thread(target=get_site_data, args=('https://www.python.org/',))
thread3 = Thread(target=get_site_data, args=('https://www.python.org/',))
thread4 = Thread(target=get_site_data, args=('https://www.python.org/',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end = time.perf_counter()
print(end-start)

# For Example Execution Time : 0.6352682999859098