# encoding=utf-8
"""
user input demo
--------------------------
1. mouse click
2. key down
3. accept content
"""

import time
from pyHook import HookManager
from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard
import pythoncom
import win32gui

m = PyMouse()
k = PyKeyboard()


def click_to_keepscreenalive():
    """
    others:
        1. get screen size:  x_dim, y_dim = m.screen_size()
        2. get cursor info: flags, hcursor, (x, y) = win32gui.GetCursorInfo()
    :return:
    """
    global m
    while True:
        time.sleep(60)
        m_x, m_y = m.position()
        print 'click (%s, %s)' % (m_x, m_y)
        # m.click(x_dim / 2, y_dim / 2, 1)
        # m.click(x, y)
        m.click(m_x, m_y, 1)


def type_and_del(content, sleep_time):
    global k
    k.type_string(content)
    time.sleep(sleep_time)
    idx = len(content)
    while idx > 0:
        k.press_key(k.backspace_key)
        idx -= 1
        time.sleep(1)


def fibo():
    """
    function for generating Fibonacci numbers
    :return:
    """
    a = 0
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a + b
        yield b


class ClickFibo(PyMouseEvent):
    """
    mouse left-click for printing Fibonacci numbers
    """

    def __init__(self):
        PyMouseEvent.__init__(self)
        self.fibo = fibo()

    def click(self, x, y, button, press):
        '''
        Print Fibonacci numbers when the left click is pressed.
        '''
        if button == 1:
            if press:
                print self.fibo.next()
        else:
            self.stop()


class KeyFilter:
    """
    key hook
    """

    def __init__(self, keys):
        self.keys = [ord(k) for k in keys]
        # create a hook manager
        hm = HookManager()
        # watch for all mouse events
        hm.KeyDown = self.FilterKeys
        # set the hook
        hm.HookKeyboard()
        # wait forever
        pythoncom.PumpMessages()

    def FilterKeys(self, event):
        res = event.Ascii in self.keys
        print '%s is in %s: %s' % (event.Ascii, self.keys, res)
        return res


def accept_content():
    input = raw_input('please input:')
    print 'user input:', input


if __name__ == "__main__":
    click_to_keepscreenalive()
    # type_and_del('Hello, World!', 5)
    # ClickFibo().run()
    # KeyFilter(['A', 'B', 'C'])
    # accept_content()
