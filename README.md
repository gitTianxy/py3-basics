this is the project records some common basics of python language and pkgs

### topics
* math
* thread, threadpool
* db, dbpool
* oop & class
* file
* exceptions
* logging
* compile/decompile
* others

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


### differences between py2.x & py3.x
* string
    - py2.x: 在Python2中，普通字符串是以8位ASCII码进行存储的
    - py3.x: 在Python3中，所有的字符串都是以16位unicode字符串存储
* dict iterate
```py
# py2.x
for k, v in dict.iteritems():
    pass

# py3.x
for k, v in dict.items():
    pass
```
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
* list api 4 py3.x
    - map() and filter() return iterators instead of list, use list(...) for transformation.
    - removed builtin `reduce()`, use `functools.reduce()` instead.
* input
    - py2.x: raw_input('tips')
    - py3.x: input('tips')
* metaclass definition
    - py2.x: use the `__metaclass__=...` builtin attribute to define the metaclass
    - py3.x: use `metaclass=...` in the class signature
