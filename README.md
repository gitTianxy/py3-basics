this is the project records some common basics of python language and pkgs

### topics
* basic data structures
* math
* function
* thread, threadpool
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
