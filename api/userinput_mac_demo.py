# encoding=utf-8
"""
input control for mac OS X
--------------------
1. month click--PyUserInput(https://github.com/SavinaRoja/PyUserInput)
"""
from pymouse import PyMouse
import time


def pymouse_demo():
    # instantiate an mouse object
    m = PyMouse()

    # move the mouse to int x and int y (these are absolute positions)
    print 'move mouse to (100,100)'
    m.move(200, 200)

    # click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
    print 'mouse left-click at (500, 300)'
    m.click(500, 300, 1)

    # get the screen size
    # print 'screen size: ', m.screen_size()

    # get the mouse position
    print 'the mouse position:', m.position()


def click_to_keepscreenalive():
    m = PyMouse()
    while True:
        (x, y) = m.position()
        m.click(x, y, 1)
        time.sleep(60)


if __name__ == '__main__':
    # pymouse_demo()
    click_to_keepscreenalive()
