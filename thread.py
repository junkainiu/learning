import threading
import multiprocessing
import time


def calc(n):
    for i in range(n):
        print i
        time.sleep(0.1)
_thread = threading.Thread(target=calc, args=(50,))
_thread.daemon = True
_thread.start()
print 'a'
print 'b'
if _thread.is_alive():
    print 'hello'
else:
    print "no"


class StoppableThread(object):

    def __init__(self):
        self.running = True

    def terminate(self):
        self.running = False

    def run(self, n):
        while self.running and n > 0:
            n -= 5
            print self.running
            print "minus time"
            time.sleep(1)


sc = StoppableThread()

t = threading.Thread(target=sc.run, args=(30,))
p = multiprocessing.Process(target=sc.run, args=(30,))
p.start()
time.sleep(2)
sc.terminate()
t.start()
time.sleep(2)
t.terminate()
sc.terminate()
t.join()
