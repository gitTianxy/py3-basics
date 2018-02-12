# coding=utf8
"""
'Pipe' decorator & 'force' executor
---
e.g. ForcePipeDemo in 'func_demo'
"""


class Pipe(object):
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.func(obj)

        return generator()


def force(sqs):
    for item in sqs: pass
