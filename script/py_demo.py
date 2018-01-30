# encoding=utf-8
"""
execute string cmd
------------------------
INCLUDE:
    1. eval(): 执行表达式并返回表达式的值
    2. execute: 执行表达式(不返回表达式的值)
CONCEPTS:
    globals, locals: 表达式中变量的域/作用范围
"""


class EvalDemo:
    """
    def:
        eval通常用来执行一个字符串表达式，并返回表达式的值
    expr:
        eval(str_expr[, globals[, locals]])
    ref:
        http://code.activestate.com/recipes/496746-restricted-safe-/
    """

    def __init__(self):
        print 'eval demo -------------------------'
        self.str_2_code("[[1,2], [3,4], [5,6], [7,8], [9,0]]")
        self.str_2_code("{1: 'a', 2: 'b'}")
        self.str_2_code("([1,2], [3,4], [5,6], [7,8], (9,0))")
        self.code_2_str(code=(1, 2, 3))
        self.eval_in_domain(code_str='a+b+c', g={'a': 1, 'b': 2, 'c': 3})
        self.eval_in_domain(code_str='a+b+c', g={'a': 1, 'b': 2, 'c': 3}, l={'a': 4, 'b': 5, 'c': 6})

    def str_2_code(self, src):
        dest = eval(src)
        print 'transform %s to %s' % (type(src), type(dest))

    def code_2_str(self, code):
        print 'transform %s to %s' % (type(code), type(`code`))

    def eval_in_domain(self, code_str, g={}, l={}):
        '''
        优先级: eval()外的变量 < global域变量 < local域变量F
        :param code_str:
        :param g:
        :param l:
        :return:
        '''
        a = 0
        print "outers: 'a':%s, globals: %s, locals: %s" % (a, g, l)
        print '%s=%s' % (code_str, eval(code_str, g, l))


class ExecDemo:
    """
    def:
        a statement supports dynamic execution of Python code. exec是一个语法声明，不是一个函数
    expr--两种等价的表达形式:
        1. exec str_expr [in globals[, locals]]
        2. exec(str_expr[, globals[, locals]])
    """

    def __init__(self):
        print 'exec demo -------------------------'
        self.follow_with_str(expr='print a+b+c', g={'a': 1, 'b': 2, 'c': 3}, l={'a': 4, 'b': 5, 'c': 6})
        self.follow_with_tuple(expr='print a+b+c', g={'a': 1, 'b': 2, 'c': 3}, l={'a': 4, 'b': 5, 'c': 6})

    def follow_with_str(self, expr, g={}, l={}):
        a = 0
        print "outers: 'a':%s, globals: %s, locals: %s" % (a, g, l)
        exec expr in g, l

    def follow_with_tuple(self, expr, g={}, l={}):
        a = 0
        print "outers: 'a':%s, globals: %s, locals: %s" % (a, g, l)
        exec (expr, g, l)


if __name__ == '__main__':
    EvalDemo()
    ExecDemo()
