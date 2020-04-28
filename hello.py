
import time
import random
from multiprocessing import Process,Lock


class WriteProcess(Process):
    """ Write file """

    def __init__(self, file_name, num, lock, *args, **kwargs):
        self.file_name = file_name
        self.num = num
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        try:
            self.lock.acquire()
            for i in range(5):
                with open(self.file_name, 'a+') as f:
                    content = 'current name: {0}, pid:{1}  --- {2} \n'.format(
                        self.name, self.pid, self.num)
                    f.write(content)
                    time.sleep(random.randint(1,3))
                    print(content)
        finally:
            self.lock.release()


if __name__ == "__main__":
    file_name = 'test.txt'
    lock = Lock()
    for n in range(5):
        p = WriteProcess(file_name, n, lock)
        p.start()