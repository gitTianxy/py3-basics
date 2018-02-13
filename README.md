this is the project records some common basics of python language and pkgs

### topics
* basic data structures
* math
* function
* process, thread
* db, dbpool
* oop & class
* file
* exceptions
* logging
* compile/decompile
* py2.x vs. py3.x
* others

### basic data structures
* number
* string
* list
* tuple
* dict

### function
* generator
    - `yield`关键字
    - 迭代器
```
在 Python 中，使用了 `yield` 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器返回一个'返回迭代器': 在调用生成器运行的过程中，
每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
并在下一次执行 next() 方法时从当前位置继续运行。
```

### process, thread
* process vs thread
```
对于操作系统来说，一个运行的程序称为一个进程(Process).
操作系统直接支持的执行单元称为线程(Thread).

由于每个进程至少要干一件事，所以，一个进程至少有一个线程。
一个进程中的任务可以划分成若干子进程来执行(多进程), 也可以划分成若干子线程来执行(多线程).

-- 进程执行
真正的并行进程只能在多核CPU上实现. 但是，由于进程数远远多于CPU的核心数，所以操作系统会自动把很多任务轮流调度到每个核心上执行。
-- 线程执行
多线程的执行方式和多进程是一样的, 也是由操作系统在多个线程之间快速切换, 让每个线程都短暂地交替运行.

-- 共享变量
多进程程序中, 各进程对变量自有一份拷贝存在于每个进程中，互不影响;
多线程程序中，各线程共享所属进程内的各变量.

并发编程的复杂性在于处理进程/线程间的依赖关系, 即需要进程/线程间的通信和协调.
```
* 进程优缺点
```
# 优点
多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。

# 缺点
1. 多进程模式的缺点是创建进程的代价大
2. 操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。
```
* 线程优缺点
```
# 优点
1. 创建代价较小
2. 多线程模式通常比多进程快一点，但是也快不到哪去

# 缺点
多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。
```
* Python既支持多进程，又支持多线程
* GIL锁
```
Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
即使100个线程跑在100核CPU上，在任一时刻也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
```
* 多任务的实现有3种方式：
    1. 多进程模式；
    2. 多线程模式；
    3. 多进程+多线程模式。
* multiprocessing
    - process
    - process pool
    - thread pool
* threading
    - thread
    - thread lock
    - thread local
```
Python的标准库提供了两个线程控制模块：_thread和threading, _thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
```
* threadpool(not recommended)
* concurrent
```
executors
1. threadpool executor
2. processpool executor

methods
1. Executor.submit(fn, *args, **kwargs)
2. Executor.map(func, *iterables, timeout=None)
3. concurrent.futures.as_completed
4. future.done()
5. future.result()
6. (completed, uncompleted) = concurrent.futures.wait(future_tasks, timeout, return-when)
```

### db
* mysql
* sqlite
* sqlalchemy

## others
### sys.path
* set by command line
```sh
# for unix
PYTHONPATH=project_path python somescript.py somecommand

# for windows
## sys_path.bat
@ECHO OFF
setlocal
set PYTHONPATH=%1
python %2 %3
endlocal
## cmd
pythonpath.bat project_path somescript.py somecommand
```
* set in .py(recommended)
```py
import sys
sys.path.append('project_path')
```
### pip升级后出现提示信息
```
DEPRECATION: The default format will switch to columns in the future. You can use –format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
```
* 这段信息的意思是说以后pip list的默认格式会采用columns了
* 解决方法: (windows)在C:\Users{用户名}\ 目录下创建名称为pip的文件夹，里面创建文本文件，内容如下所示. 然后保存文件名为pip.ini即可.
```
[list]
format=columns
```

### mouse, keyboard control
* pywin32
```sh
$ pip install pywin32
$ pip install pypiwin32
```
* pyHook
```sh
$ pip install pyhook-proper-version.whl
```


## py2.x vs. py3.x
* string
    - py2.x: 在Python2中，普通字符串是以8位ASCII码进行存储的
    - py3.x: 在Python3中，所有的字符串都是以16位unicode字符串存储

### dict relevant api
* iterate
```py
# py2.x
for k, v in dict.iteritems():
    pass

# py3.x
for k, v in dict.items():
    pass
```
* `values()` & `keys()`
```py
# py2.x: returns a list
# py3.x: returns a list iterator; use `list(...)` for transformation
```
* 'generator' object has no attribute 'next'

* mysql connector
    - py2.x: MySQL-python
    - py3.x: PyMySQL

* try-except
```py
# py2.x
try
    pass
except Exception, ex:
    print("error happens")
else:
    print("no error happens")
finally:
    pass

# py3.x
try
    pass
except Exception as ex:
    print("error happens")
else:
    print("no error happens")
finally:
    pass
```

### list relevant api
* map,reduce
```py
# py2.x
# - map(): returns a list
# - reduce(): returns a list

# py3.x
# - map(): returns a iterator
# - reduce(): removed, use `functools.reduce()` instead
```
* filter
```py
# py2.x: returns a list

# py3.x: returns a iterator, use list(filter(...)) for transformation
```
* `range(start,stop,step)`
```py
# py2.x
# - range(): returns a list
# - xrange(): returns a iterator

# py3.x
# - range(): returns a iterator
# - no xrange()
```
* iterate
```py
# py2.x
itr2 = iter(l)
itr2.next()

lgen2 = (...)
lgen2.next()

# py3.x
itr3 = iter(l)
next(itr3)

lgen3 = (...)
lgen3.__next__()
```

* input
    - py2.x: raw_input('tips')
    - py3.x: input('tips')
* metaclass definition
    - py2.x: use the `__metaclass__=...` builtin attribute to define the metaclass
    - py3.x: use `metaclass=...` in the class signature
