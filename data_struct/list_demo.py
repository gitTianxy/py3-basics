# coding=utf-8

"""
OPERATIONS on sequence(list, tuple, dict)
    1. sort
    2. filter
    3. map
    4. reduce: functools.reduce
    5. list-generator
    6. iteration
"""
import random
import functools


class SortDemo:
    """
    排序有两种:
        1. list内禀的sort方法
        2. 外部sorter将list作为输入进行排序
    NOTE: 内禀的sort方法会改变原序列--依情况选用两种方法中的一种
    """

    def __init__(self, nums, dicts):
        self.nums = nums
        self.dicts = dicts
        print('do sorts --------------')
        self.sort_nums()
        self.sort_nums_buildin()
        self.sort_dicts()
        self.sort_dicts_buildin()

    def sort_nums(self):
        print('nums_ori:', self.nums)
        print('nums_sorted:', sorted(self.nums))

    def sort_nums_buildin(self):
        print('nums_before_sort: ', self.nums)
        self.nums.sort(key=lambda n: n)
        print('nums_after_sort: ', self.nums)

    def sort_dicts(self):
        def get_val(dic):
            return list(dic.values())[0]

        print('dicts_ori:', self.dicts)
        print('dicts_sorted:', sorted(self.dicts, key=get_val))

    def sort_dicts_buildin(self):
        print('dicts_before_sort: ', self.dicts)
        self.dicts.sort(key=lambda d: list(d.values())[0])
        print('dicts_after_sort: ', self.dicts)


class FilterDemo:
    """
    NOTE: filter是基于原序列产生一个新的序列
    """

    def __init__(self, nums, dicts, threshold):
        self.nums = nums
        self.dicts = dicts
        self.threshold = threshold
        print('filter item>%s --------------' % threshold)
        self.filter_nums()
        self.filter_dicts()

    def filter_nums(self):
        print('nums_ori:', self.nums)
        print('nums_filtered:', list(filter(lambda s: s > self.threshold, self.nums)))

    def filter_dicts(self):
        print('dicts_ori:', self.dicts)
        print('dicts_filtered:', list(filter(lambda s: list(s.values())[0] > self.threshold, self.dicts)))


class MapDemo:
    """
    TIP: map() is a list transformer, which can also be treated as part of list generator
    """

    def __init__(self, nums, dicts, foot):
        self.nums = nums
        self.dicts = dicts
        self.foot = foot
        print('item mod %s --------------' % foot)
        self.map_nums()
        self.map_dicts()

    def map_nums(self):
        print('nums_ori:', self.nums)
        print('nums_mapped:', list(map(lambda num: num % self.foot, self.nums)))

    def map_dicts(self):
        print('dicts_ori:', self.dicts)
        print('dicts_mapped:', list(map(lambda d: {list(d.keys())[0]: list(d.values())[0] % self.foot}, self.dicts)))


class ReduceDemo:
    def __init__(self, nums, dicts):
        self.nums = nums
        self.dicts = dicts
        print('reduce --------------')
        self.reduce_nums()
        self.reduce_dicts()

    def reduce_nums(self):
        print('nums_ori:', self.nums)
        print('nums_reduced(sum):', functools.reduce(lambda s1, s2: s1 + s2, self.nums))

    def reduce_dicts(self):
        """
        NOTE: reduce的要求以下几者类型一致:
            1. 操作函数的两个入参
            2. 输入序列元素类型
            3. 操作函数输出
        :return:
        """
        print('dicts_ori:', self.dicts)
        print('dicts_reduced(value-sum):', functools.reduce(lambda s1, s2: s1 + s2, map(lambda d: list(d.values())[0], self.dicts)))


class ListGenerator:
    """
    two requirements:
        1. seeds
        2. an item-generator
    """

    def __init__(self):
        print('generate list --------------')
        self.seeds = list(range(0, 10))
        print('seeds:', self.seeds)
        self.generate_square()
        self.generate_square_with_filter(5)

    def generate_square(self):
        def generate_item(s):
            return s * s

        print('square_list:', [generate_item(s) for s in self.seeds])

    def generate_square_with_filter(self, threshold):
        def generate_item(s):
            return s * s

        print('square_list(>%s):%s' % (threshold, [generate_item(s) for s in self.seeds if s > threshold]))


class IterateDemo:
    """
    two ways to iterate over a list:
        1. for-loop: list is instance of 'iterable'
        2. list-iterator: use iter(list) to get it
    TIPS:
        1. in addition to list, tuple/dict/set/str are also iterable
        2. we use iter() to get the iterator corresponding to an iterable collection
        3. a novel type of obj -- 'generator': for generation of collection;
           not only iterable, but is also an iterator by itself
    """

    def __init__(self, nums):
        self.nums = nums
        print('list iteration --------------')
        self.itr_by_forloop()
        self.itr_by_listiterator()
        self.itr_over_listgenerator()

    def itr_by_forloop(self):
        print('iterate by for-loop:')
        for num in self.nums:
            print(' ', num)

    def itr_by_listiterator(self):
        print('iterate by list-iterator:')
        liter = iter(self.nums)
        while True:
            try:
                print(' ', next(liter))
            except StopIteration:
                break

    def itr_over_listgenerator(self):
        print('\niterate over a generator --------------')
        list_gen = (num for num in self.nums)
        print('*** with for-loop(recommended)')
        for num in list_gen:
            print(num)
        list_gen = (num for num in self.nums)
        print('*** with .next()')
        while True:
            try:
                print(list_gen.__next__())
            except StopIteration:
                break


class GeneratorDemo:
    """
    two ways to define a generator:
        1. generator-expression: (...)
        2. function-with-yield
    NOTE:
        1. generator是'惰性的'--只有在调用next()方法时才生成下一个元素; 这样的好处是, 我们不需要存储空间就可以拥有一个很大的序列
        2. 虽然generator以函数的形式定义, 但是generator和函数的执行流程不一样:
            a. 函数是顺序执行，遇到return语句或者最后一行函数语句就返回;
            b. generator函数在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    """

    def __init__(self):
        print('generator demos --------------')
        print('*** num_generator:')
        for num in self.num_generator(limit=5):
            print(' ', num)
        print('*** odd_generator:')
        for odd in self.odd_generator(limit=5):
            print(' ', odd)
        print('*** fib_generator:')
        for fib in self.fib_generator(count=10):
            print(' ', fib)

    def num_generator(self, limit):
        return (num for num in range(0, limit))

    def odd_generator(self, limit):
        for num in range(0, limit):
            if num % 2 == 1:
                yield num

    def fib_generator(self, count):
        idx, a, b = 0, 0, 1
        while idx < count:
            yield a
            a, b = b, a + b
            idx += 1


class RemoveDemo:
    def __init__(self):
        print('------------- REMOVE demo ---------------')
        self.rm_obj()
        self.rm_by_idx()

    def rm_obj(self):
        """
        remove the 1st occurrence
        :return:
        """
        l1 = list(range(0, 10))
        l1.extend(range(0, 10))
        print("list ori:", l1)
        for obj in range(0, 10):
            if obj % 2 == 0:
                l1.remove(obj)
        print("list removed by obj:", l1)

    def rm_by_idx(self):
        """
        remove by idx
        :return:
        """
        l = list(range(0, 10))
        print("list ori:", l)
        i = 0
        llen = len(l)
        while i < llen:
            if l[i] % 2 == 0:
                l.pop(i)
                llen -= 1
            else:
                i += 1
        print("list removed by idx:", l)


def range_demo():
    """
    range(start, end, step)
    :return:
    """
    print("--- range demo ---")
    rg = range(0, 10, 2)
    print("type of %s: %s" % (rg, type(rg)))
    for num in rg:
        print(num)


if __name__ == "__main__":
    # prepare data
    num_list = []
    dict_list = []
    for i in range(0, 10):
        val = random.randrange(0, 100)
        num_list.append(val)
        dict_list.append({'key%s' % i: val})
    # show demos
    SortDemo(num_list, dict_list)
    FilterDemo(num_list, dict_list, threshold=50)
    MapDemo(num_list, dict_list, foot=10)
    ReduceDemo(num_list, dict_list)
    ListGenerator()
    IterateDemo(num_list)
    GeneratorDemo()
    RemoveDemo()
    range_demo()
