# coding=utf-8
"""
The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously.
ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global Interpreter Lock but
also means that only picklable objects can be executed and returned.
"""
from concurrent.futures import ProcessPoolExecutor
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def square(o):
    global objs

    print("do square", o['in'])
    o['out'] = o['in'] ** 2
    for obj in objs:
        if obj['in'] == o['in']:
            print(" %s equals %s" % (obj['in'], o['in']))
            obj['out'] = o['out']
            break


def prime_task():
    print('---prime task')
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


def square_task():
    global objs
    """
    input data cannot be written in processes, or changes in process is unreadable outside
    """
    print("---square task")
    res = None
    with ProcessPoolExecutor() as executor:
        executor.map(square, objs)
        # res = zip(map(lambda o: o['input'], objs), executor.map(square, objs))
    print("square finish")
    for o in objs:
        print(f"input:{o.get('in')}, output:{o.get('out')}")
    # for inv, outv in res:
    #     print(f"input:{inv}, output:{outv}")


objs = [{
    'in': i
} for i in range(5)]
if __name__ == '__main__':
    # prime_task()
    square_task()
    print("***all finish")
