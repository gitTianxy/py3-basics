# coding=utf-8
"""
This file exhibits the compile and decompile of .py file
"""

import dis, imp, sys


def do_compile(py_path):
    py_f = open(py_path).read()
    code_obj = compile(py_f, py_path, 'exec')
    return code_obj


def generate_pyc(py_path):
    fp, pathname, description = imp.find_module(py_path)
    try:
        imp.load_module(py_path, fp, pathname, description)
    finally:
        if fp:
            fp.close()


def generate_bytecode(pyc_path):
    pyc_f = open(pyc_path).read()
    return dis.dis(pyc_f)


if __name__ == "__main__":
    print 'compile----------'
    compile_res = do_compile('hello_world.py')
    print compile_res
    print 'generate_pyc---------'
    generate_pyc('hello_world')
    print 'generate_bytecode---------'
    decompile_res = generate_bytecode("hello_world.pyc")
    print decompile_res
