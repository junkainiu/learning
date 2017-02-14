from Queue import Queue
import time
import threading


def producer(q):
    for i in range(10000):
        q.put('a')
        time.sleep(0.1)
        if i % 100 == 0 and i != 0:
            q.put('finish')
            break


def comsumer(q):
    while True:
        data = q.get()
        print data
        if data == 'finish':
            break
q = Queue()
pro = threading.Thread(target=producer, args=(q,))
com = threading.Thread(target=comsumer, args=(q,))
com.start()
pro.start()
