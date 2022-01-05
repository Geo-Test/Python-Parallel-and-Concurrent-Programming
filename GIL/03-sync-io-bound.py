from threading import Thread
import time
import requests

start = time.perf_counter()


def get_site_data(url):
    response = requests.get(url)
    return response.text

get_site_data('https://www.python.org/')
get_site_data('https://www.python.org/')
get_site_data('https://www.python.org/')
get_site_data('https://www.python.org/')

end = time.perf_counter()
print(end-start)

# For Example Execution Time : 2.6516358999942895