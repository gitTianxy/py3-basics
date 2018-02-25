# coding=utf8
"""
如果列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素, 而不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器（Generator）
---
two ways to define a generator:
    1. generator-expression: (...)
    2. function-with-yield
NOTE:
    1. generator是'惰性的'--只有在调用next()方法时才生成下一个元素; 这样的好处是, 我们不需要存储空间就可以拥有一个很大的序列
    2. 虽然generator以函数的形式定义, 但是generator和函数的执行流程不一样:
        a. 函数是顺序执行，遇到return语句或者最后一行函数语句就返回;
        b. generator函数在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""


def num_generator(limit):
    return (num for num in range(0, limit))


def odd_generator(limit):
    for num in range(0, limit):
        if num % 2 == 1:
            yield num


def fib_generator(count):
    idx, a, b = 0, 0, 1
    while idx < count:
        yield a
        a, b = b, a + b
        idx += 1


if __name__ == '__main__':
    print('--- num_generator:')
    ng = num_generator(limit=5)
    while True:
        n = next(ng, None)
        if n is None:
            break
        print(n)

    print('--- odd_generator:')
    for odd in odd_generator(limit=10):
        print(' ', odd)

    print('--- fib_generator:')
    fg = fib_generator(count=10)
    while True:
        try:
            print(next(fg))
        except StopIteration:
            break
