# coding=utf8
"""
协程，又称微线程，纤程。英文名Coroutine。
---
I. 子程序 vs 协程
- 子程序: 或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
    子程序调用是通过栈实现的，总是一个入口，一次返回，调用顺序是明确的。
- 协程: 也是存在多个子程序的调用执行, 但是子程序之间不是层级调用关系, 调用顺序不确定--一个子程序在执行过程中可被中断，
    然后转而执行别的子程序，在适当的时候再返回来接着执行。在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。

II. 协程 vs 多线程
- 协程: 单一线程被若干子程序共享, 子程序之间通过中断的方式切换;
    最大的优势就是协程极高的执行效率, 第二大优势就是不需要多线程的锁机制;
    因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是`多进程+协程`, 既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
- 多线程: 多个线程并存, 瓜分cpu时间

III. Python对协程的支持是通过generator实现的。

IV. asyncio
1. py3.4: `@asyncio.coroutine`, `yield from`
2. py3.5: `async`, `await`
---
1. A producer-consumer model
2. asyncio
3. aiohttp
"""
from time import sleep
import asyncio
import threading
from contextlib import closing
from aiohttp import web


class ProConDemo:
    """
    A producer-consumer model
    """

    def __init__(self):
        print("---producer-consumer model")
        c = self.consumer()
        self.produce(c)

    def consumer(self):
        r = ''
        while True:
            n = yield r
            if not n:
                return
            print('[CONSUMER] Consuming %s...' % n)
            r = '200 OK'

    def produce(self, c):
        c.send(None)
        n = 0
        while n < 5:
            n = n + 1
            print('[PRODUCER] Producing %s...' % n)
            sleep(1)
            r = c.send(n)
            print('[PRODUCER] Consumer return: %s' % r)
        c.close()


class AsyncioDemo:
    def __init__(self):
        with closing(asyncio.get_event_loop()) as loop:
            print("---basic asyncio demo")
            tasks = [self.hello(), self.hello2()]
            loop.run_until_complete(asyncio.wait(tasks))
            print("---async wget")
            tasks = [self.wget(host) for host in ['www.youtube.com', 'www.sina.com.cn', 'www.163.com']]
            loop.run_until_complete(asyncio.wait(tasks))

    async def hello(self):
        """
        asyncio.sleep(1)代表异步执行的耗时任务
        """
        print("hello START.", threading.currentThread())
        await self.cort_sleep(1)
        # await asyncio.sleep(1)
        print("hello RETURN.", threading.currentThread())

    async def hello2(self):
        """
        asyncio.sleep(1)代表异步执行的耗时任务
        """
        print("hello2 START.", threading.currentThread())
        await self.cort_sleep(5)
        # await asyncio.sleep(1)
        print("hello2 RETURN.", threading.currentThread())

    async def cort_sleep(self, secs):
        """
        asyncio.sleep(1)代表异步执行的耗时任务
        """
        print(f"cort sleep{secs} START. {threading.current_thread()}")
        await asyncio.sleep(secs)
        print(f"cort sleep{secs} RETURN. {threading.current_thread()}")

    async def wget(self, host):
        print('wget %s...' % host)
        connect = asyncio.open_connection(host, 80)
        reader, writer = await connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        await writer.drain()
        while True:
            line = await reader.readline()
            if line == b'\r\n':
                break
            print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()


class AioHttpDemo:
    """
    asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
    """
    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.init(loop))
        loop.run_forever()

    async def index(self):
        await asyncio.sleep(0.5)
        return web.Response(body=b'<h1>Index</h1>')

    async def hello(self, request):
        await asyncio.sleep(0.5)
        text = '<h1>hello, %s!</h1>' % request.match_info['name']
        return web.Response(body=text.encode('utf-8'))

    async def init(self, loop):
        app = web.Application(loop=loop)
        app.router.add_route('GET', '/', self.index)
        app.router.add_route('GET', '/hello/{name}', self.hello)
        srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
        print('Server started at http://127.0.0.1:8000...')
        return srv


if __name__ == '__main__':
    ProConDemo()
    AsyncioDemo()
    # AioHttpDemo()
