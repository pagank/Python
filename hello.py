
import time
import random
from multiprocessing import current_process, Pool


def run(file_name, num):

    with open(file_name, 'a+') as f:
        curr_proc = current_process()
        content = '{0} - {1} --- {2} \n'.format(curr_proc.name,
                                                curr_proc.pid, num)
        f.write(content)
        time.sleep(random.randint(1, 3))
        print(content)

    return 'ok'


if __name__ == "__main__":
    file_name = 'test_pool.txt'
    pool = Pool(2)
    for i in range(20):
        # # sycnc
        # rest = pool.apply(run, args=(file_name, i))
        # async
        rest = pool.apply_async(run, args=(file_name, i))
        print('{0}----- {1}'.format(i, rest.get()))
    pool.close()
    pool.join()