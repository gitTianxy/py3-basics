# coding=utf8
"""
collections是Python内建的一个集合模块，提供了许多有用的集合类。
1. namedtuple
2. deque
3a. defaultdict
3b. ordereddict
4. counter
"""
from collections import *


def namedtupledemo():
    """
    namedtuple是一个函数，
    它用来创建一个自定义的tuple对象，
    并且规定了tuple元素的个数，
    并可以用属性而不是索引来引用tuple的某个元素。
    """
    print("---define named tuple")
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(f"{type(p).__name__}: ({p.x}, {p.y})")
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    c = Circle(0, 0, 1)
    print(f"{type(c).__name__}: x={c.x}, y={c.y}, r={c.r}")


def dequedemo():
    """
    double-oriented queue: deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈.
    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
    """
    print("---deque demo")
    dq = deque(['a', 'b', 'c'])
    dq.append('r')
    dq.appendleft('l')
    print(dq)
    assert dq.pop() == 'r'
    assert dq.popleft() == 'l'


def defaultdictdemo():
    """
    使用dict时，如果引用的Key不存在，就会抛出KeyError。
    如果希望key不存在时，返回一个默认值，就可以用defaultdict
    """
    print("---define dict with default value")
    dd = defaultdict(lambda: 'N/A')
    dd['ekey'] = 'key exists'
    print(f"{'ekey'} in {dd}: {dd['ekey']}")
    print(f"{'nkey'} in {dd}: {dd['nkey']}")


def ordereddictdemo():
    """
    使用dict时，Key是无序的--在对dict做迭代时，我们无法确定Key的顺序。
    如果要保持Key的顺序，可以用OrderedDict
    """
    print("---define ordered dict")
    # d = dict([('a', 1), ('b', 2), ('c', 3)])
    # print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)


if __name__ == '__main__':
    namedtupledemo()
    dequedemo()
    defaultdictdemo()
    ordereddictdemo()
