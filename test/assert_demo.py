# encoding=utf-8
"""
The assert statement exists in almost every programming language. When you do...
```
assert condition
```
... you're telling the program to test that condition, and trigger an error if the condition is false.

In Python, it's roughly equivalent to this:
```
if not condition:
    raise AssertionError()
```
"""

if __name__ == '__main__':
    assert 1 == 1
    assert 1 != 1
