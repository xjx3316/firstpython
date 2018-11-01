import threading
from threading import current_thread
import time


class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        time.sleep(1)
        print(current_thread().getName(), 'stop')


t1 = Mythread()
t1.start()
t1.join()
print(current_thread().getName(), 'end')
