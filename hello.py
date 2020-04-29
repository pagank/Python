
import asyncio
import random


async def add(store, name):
    """ input queue """
    for i in range(5):
        num = '{0} - {1}'.format(name, i)
        await asyncio.sleep(random.randint(1, 3))
        await store.put(i)
        print('{0} add --- {1}, seize: {2}'.format(name, num, store.qsize()))


async def reduces(store):
    """ dequeue """
    for i in range(10):
        rest = await store.get()
        print('reduce --- {0}, size: {1}'.format(rest, store.qsize()))


if __name__ == "__main__":
    store = asyncio.Queue(maxsize=5)
    a1 = add(store, 'a1')
    a2 = add(store, 'a2')
    r1 = reduces(store)

    # add into event queue
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(a1, a2, r1))
    loop.close()
