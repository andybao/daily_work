import datetime
import time
from multiprocessing import Process

def f(x):
    time.sleep(1)
    print ('{0}: {1}'.format(x, datetime.datetime.now()))

if __name__ == "__main__":
    for i in range(2):
        p = Process(target=f(i))
        p.start()