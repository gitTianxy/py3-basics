# coding=utf-8
"""
ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.
"""
import time
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import urllib.request


def load_url(url, timeout):
    """
    Retrieve a single page and report the URL and contents
    :param url:
    :param timeout:
    :return:
    """
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def download_job():
    print("---download job")
    urls = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'http://some-made-up-domain.com/']
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


class DeadLockDemo:
    def __init__(self):
        # self.wait_each_other()
        self.wait_on_noresult()

    def wait_each_other(self):
        print("---dead lock:wait each other")
        executor = ThreadPoolExecutor(max_workers=2)
        self.a = executor.submit(self.wait_on_b)
        self.b = executor.submit(self.wait_on_a)

    def wait_on_b(self):
        time.sleep(1)
        print("wait on b...")
        print(self.b.result())  # b will never complete because it is waiting on a.
        return 1

    def wait_on_a(self):
        time.sleep(2)
        print("wait on a...")
        print(self.a.result())  # a will never complete because it is waiting on b.
        return 2

    def wait_on_noresult(self):
        """
        cannot complete because no free worker
        :return:
        """
        print("---deadlock: wait on no result")
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.executor.submit(self.wait_on_future)

    def wait_on_future(self):
        f = self.executor.submit(pow, 5, 2)
        print("wait for pow(5, 2)...")
        print(f.result())


if __name__ == '__main__':
    download_job()
    DeadLockDemo()
