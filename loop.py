# coding=utf8
"""
loops:
1. for-loop
2. while-loop

iterators:
1. self-defined iterator
2. self-defined list
3. itertools demo
"""
import itertools

# for-loop
print('FOR-LOOP')
for letter in 'Python':  # 第一个实例
    if letter == 't':
        print("I'm 't'")
    else:
        print(letter)

# while-loop
print('WHILE-LOOP')
idx = 0
while idx < 10:
    print('idx=%s' % idx)
    idx += 1
else:
    print('idx=%s, escape from the loop' % idx)


class SelfItr:
    """
    iterable conditions in python:
    1. __iter__(): returns the iterable object
    2. __next__(): return next iteration value, or raise StopIteration if meeting the stop condition
    """

    def __init__(self, loop_num):
        self.loop_num = loop_num
        self.tmp = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.tmp > self.loop_num:
            raise StopIteration()
        else:
            self.tmp += 1
            return self.tmp - 1


class SelfList:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.list = list(range(start, stop))

    def __iter__(self):
        return self.list.__iter__()

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            return self.list[n]
        elif isinstance(n, slice):
            start = n.start if n.start else 0
            stop = n.stop
            return self.list[start:stop]
        else:
            raise TypeError(f'input type error. val:{n}')


class ItertoolsDemo:
    def __init__(self):
        print("---demos for 'itertools'")
        self.infinite_itrs(10)
        self.finite_itrs(5)
        self.chain('abc', 'def')
        self.groupby('AAABBBCCAAA')

    def infinite_itrs(self, limit):
        counts = []
        for i in itertools.count(0, 2):
            if i > limit:
                break
            counts.append(str(i))
        counts.append('...')
        print("infinite counts:", counts)

        repeats = []
        for i in itertools.repeat('a'):
            if len(repeats) > limit:
                break
            repeats.append(i)
        repeats.append('...')
        print("infinite repeats:", repeats)

        cycles = []
        for i in itertools.cycle('abc'):
            if len(cycles) > limit:
                break
            cycles.append(i)
        cycles.append('...')
        print("infinite cycles:", cycles)

    def finite_itrs(self, limit):
        counts = list(itertools.takewhile(lambda i: i < limit, itertools.count(0, 2)))
        print("finite counts:", counts)

        repeats = list(itertools.repeat('a', limit))
        print("finite repeats:", repeats)

        cycles = []
        for i in itertools.cycle('abc'):
            if len(cycles) >= limit:
                break
            cycles.append(i)
        print("finite cycles:", cycles)

    def chain(self, c1, c2):
        print(f"chain {c1} and {c2} together: {list(itertools.chain(c1, c2))}")

    def groupby(self, content):
        print(f"group {content} by adjacent keys:")
        for k, gp in itertools.groupby(content):
            print(f"{k}: {list(gp)}")


if __name__ == '__main__':
    print("---self defined 'iterator'")
    for num in SelfItr(10):
        print(num)
    print("---self defined 'list'")
    sl = SelfList(0, 10)
    for item in sl:
        print(item)
    print("item %s in list: %s" % (5, sl[5]))
    print("items range between %s to %s: %s" % (1, 5, sl[1:5]))
    ItertoolsDemo()
