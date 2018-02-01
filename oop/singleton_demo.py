# coding=utf-8
"""
The singleton pattern is a design pattern that restricts the instantiation of a class to one object. It is used in
cases where exactly one object is needed. The concept can be generalized to restrict the instantiation to a certain or
fixed number of objects. The term stems from mathematics, where a singleton, - also called a unit set -, is used for
sets with exactly one element.
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonCls(metaclass=Singleton):
    pass


if __name__ == '__main__':
    sgl1 = SingletonCls()
    sgl2 = SingletonCls()

    print("instance 1 equals to instance 2:", sgl1 == sgl2)
