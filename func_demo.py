# encoding=utf-8
"""
this package exhibits the 'functional programming' with python, which includes:
    1. embedded function
    2. function variable
    3. function decorator
    4. partial function
    5. lambda function
    6. variadic parameter
"""
import functools
from util.pipe import Pipe, force


class EmbeddedFuncDemo:
    def __init__(self):
        self.out_func()

    def out_func(self):
        """
        a func can keep and call an inner func
        :return:
        """

        def inner_func():
            """
            a func defined in another func
            :return:
            """
            print('inner_func be called')

        print('here in %s.out_func' % self.__class__.__name__)
        inner_func()


class FuncVarDemo:
    """
    the name of a function is also a function-variable: a var pointer to function-object
    :return:
    """

    def __init__(self):
        # define a function variable
        func_var = self.func
        print(func_var.__name__, 'assigned to a func_var')
        # call the function by the function variable
        func_var()

    def func(self):
        print('%s.func be called' % self.__class__.__name__)


class DecoratorDemo:
    """
    INCLUDE:
        1. add tag
        2. attach log
    NOTE: 感觉不太可取, 代码的表达结构太曲折
    """

    def __init__(self):
        def tag(t):
            """
            add tag to a function
            :param tag:
            :return:
            """

            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    print(func(*args, **kwargs), 'is tagged with', t)

                return wrapper

            return decorator

        @tag('Kevin Tian')
        def product():
            return 'product'

        def log(func):
            """
            add log to a function
            :param func:
            :return:
            """

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print("before", func.__name__)
                func(*args, **kwargs)
                print("after", func.__name__)

            return wrapper

        @log
        def job():
            print('do job')

        job()
        product()


class PartialFuncDemo:
    """
    partial-function is a customized function, with partial input para fixed
    """

    def __init__(self):
        def display(a, b):
            print('a is %s, b is %s' % (a, b))

        func_with_fixed_b = functools.partial(display, b='B')
        for i in range(0, 10):
            func_with_fixed_b('A%s' % i)


class LambdaFuncDemo:
    """
    lambda-expression returns a non-name function
    NOTE:
        1. 'map' requires a func with one input para
        2. 'reduce' requires a function with two input para
    """

    def __init__(self):
        def square(x):
            return x * x

        def sum(x, y):
            return x + y

        list_in = range(0, 10)
        print('input: ', list_in)
        print('list-square: ', list(map(lambda x: square(x), list_in)))
        print('list-sum: ', functools.reduce(lambda x, y: sum(x, y), list_in))


class VarParaDemo:
    """
    1. 可变参数
    2. 关键字参数
    """

    def __init__(self):
        name = 'kevin'
        age = 28
        VarParaDemo.args_func(name, age)
        VarParaDemo.kwargs_func(name=name, age=age)

    @staticmethod
    def args_func(*args):
        """
        可变参数在函数调用时自动组装为一个tuple
        :param args:
        :param kwargs:
        :return:
        """
        for arg in args:
            print(arg)

    @staticmethod
    def kwargs_func(**kwargs):
        """
        关键字参数在函数内部自动组装为一个dict
        :param kwargs:
        :return:
        """
        for k, v in kwargs.items():
            print('%s: %s' % (k, v))


class PipelineDemo:
    def __init__(self):
        res = self.pip_exec(range(10), [
            PipelineDemo.even_filter,
            PipelineDemo.square,
            PipelineDemo.to_view
        ])
        for r in res:
            print(r)

    @staticmethod
    def even_filter(nums):
        return filter(lambda n: n % 2 == 0, nums)

    @staticmethod
    def square(nums):
        return map(lambda n: n * n, nums)

    @staticmethod
    def to_view(nums):
        return map(lambda n: f"number:{n}", nums)

    def pip_exec(self, data, fns):
        return functools.reduce(lambda d, f: f(d), fns, data)


class ForcePipeDemo:
    def __init__(self):
        force(range(10) | even_filter | square | to_view | echo)

@Pipe
def even_filter(num):
    return num if num % 2 == 0 else None

@Pipe
def square(num):
    return num * num

@Pipe
def to_view(num):
    return f"Number:{num}"

@Pipe
def echo(item):
    print(item)
    return item


if __name__ == '__main__':
    print('--------- 1. embedded function ---------')
    EmbeddedFuncDemo()
    print('--------- 2. function variable ---------')
    FuncVarDemo()
    print('--------- 3. function decorator ---------')
    DecoratorDemo()
    print('--------- 4. partial function ---------')
    PartialFuncDemo()
    print('--------- 5. lambda function ---------')
    LambdaFuncDemo()
    print('--------- 6. variadic parameter demo ---------')
    VarParaDemo()
    print('--------- 7. pipeline demo ---------')
    PipelineDemo()
    print('--------- 8. force demo ---------')
    ForcePipeDemo()
