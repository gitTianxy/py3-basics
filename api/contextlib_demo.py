# encoding=utf-8
"""
3 demos exhibited:
    1. with-demo
    2. contextmanager-demo
    3. closing demo
"""
from contextlib import closing
from contextlib import contextmanager


class WithDemo:
    """
    with用法实例. 包含:
        1. 一个实现上下文的内部类: WithDemo.ObjWithContext(实现了__enter__, __exit__方法的类)
        2. 一个展示with功能的方法: WithDemo.perform()
    """

    def __init__(self):
        pass

    @staticmethod
    def perform():
        """
        with作用于实现了上下文的对象, 执行顺序为:
            1. return obj_with_context
            2. obj_with_context.__enter__()
            3. obj_with_context.do_job()
            4. obj_with_context.__exit__()
        """
        with WithDemo.ret_obj_with_context() as o:
            o.do_job()

    @staticmethod
    def ret_obj_with_context():
        o = WithDemo.ObjWithContext()
        print 'return an', o.__class__.__name__
        return o

    class ObjWithContext:
        """
        object with context: the 'enter' and 'exit' functions
        """

        def __init__(self):
            pass

        def do_job(self):
            print self.__class__.__name__, "do job"

        def __enter__(self):
            """
            __enter__函数必须返回一个包含__exit__方法的对象
            :return:
            """
            print self.__class__.__name__, 'enter'
            return self

        def __exit__(self, *exc_info):
            print self.__class__.__name__, 'exit'


class ContextManagerDemo:
    """
    contextmanager使用实例. 包含:
        1. 一个没有实现上下文的类: ContextManagerDemo.ObjWithoutContext
        2. 一个展示contextmanager用法的方法: ContextManagerDemo.perform()
    """

    def __init__(self):
        pass

    @staticmethod
    def perform():
        with ContextManagerDemo.make_context('A') as a, ContextManagerDemo.make_context('B') as b:
            a.do_job()
            b.do_job()

    @staticmethod
    @contextmanager
    def make_context(name):
        """
        contextmanager用于: 给一个对象'添加上下文'.
        这样做的好处是: 上下文逻辑独立于被修饰对象
        """
        print 'before', name, 'do job'
        yield ContextManagerDemo.ObjWithoutContext(name)
        print 'after', name, 'do job'

    class ObjWithoutContext:
        """
        obj without context
        """

        def __init__(self, name):
            self.name = name

        def do_job(self):
            print self.name, 'do job'


class ClosingDemo:
    """
    closing用法实例. 包含:
        1. 一个实现了close方法的内部类: ClosingDemo.ObjWithClose
        2. 一个展示closing使用方法的方法: ClosingDemo.perform()
    """

    def __init__(self):
        pass

    @staticmethod
    def perform():
        """
        closing方法的作用:
            1. 将一个包含close方法的对像自动包装__enter__和__exit__
            2. 在__exit__内部执行对象的close方法
        :return:
        """
        with closing(ClosingDemo.ret_obj_with_close()) as o:
            o.do_job()

    @staticmethod
    def ret_obj_with_close():
        return ClosingDemo.ObjWithClose()

    class ObjWithClose:
        """
        obj with close
        """

        def __init__(self):
            self.name = self.__class__.__name__

        def do_job(self):
            print self.name, 'do job'

        def close(self):
            print self.name, 'is closed'


if __name__ == "__main__":
    print '----------- WithDemo ------------'
    WithDemo.perform()
    print '----------- ContextManagerDemo ------------'
    ContextManagerDemo.perform()
    print '----------- ClosingDemo ------------'
    ClosingDemo.perform()
