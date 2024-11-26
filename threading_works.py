import threading
import time
import requests

urls = ['https://postman-echo.com/delay/3'] * 10

class ThreadingDownloader(threading.Thread): # inheritance
    json_array = []
    def __init__(self,url):
        super().__init__()
        self.url = url
    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
        print(t)
    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, "seconds")

get_data_threading(urls)