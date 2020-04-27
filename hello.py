import os
import time
from multiprocessing import Process

def do_sth(name):
    """ proccess do """
    print('Proccess name: {0}; pid: {1}'.format(name, os.getpid()))
    time.sleep(112)
    print('proccess do')


if __name__ == "__main__":
    p = Process(target=do_sth, args=('my proccess',))
    p.start()
    p.join()