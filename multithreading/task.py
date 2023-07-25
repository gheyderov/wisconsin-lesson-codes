import time
import threading
import requests

def do_something(index):
    print('Process Start...')
    res = requests.get('https://picsum.photos/200/300')
    with open(f'images/image_{index}.png', 'wb') as file:
        file.write(res.content)
    print('Process End...')

t1 = time.time()

threads = []

for i in range(100):
    th1 = threading.Thread(target=do_something(i))
    th1.start()
    threads.append(th1)

for i in threads:
    i.join()

t2 = time.time()

print(t2 - t1)