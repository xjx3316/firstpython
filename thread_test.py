import threading
import time


def mythread(arg1, arg2):
   print(threading.current_thread().getName(),'start')
   print('%s %s'%(arg1,arg2))
   time.sleep(1)
   print(threading.current_thread().getName(),'stop')

for i in range(1,6,1):
    t1 = threading.Thread(target=mythread,args=(i,i+1))
    t1.start()
    #t1.join()#此方法可以让线程全部走完后，主线程才会结束

print(threading.current_thread().getName(),'end')