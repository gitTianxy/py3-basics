# coding=utf-8

"""
I. 一个生产者和一个消费者的情形
假设:
    1. 生产速度明显大于消费速度
    2. 队列有上界
结果:
    一开始生产者占优势, 队列迅速被塞满;
    之后由于队列满了, 虽然生产者速度快,但是要等消费者消费掉一个才能继续塞进去一个, 所以变成生产一个消费一个的模式
    最后生产结束,等待消费者消费完成
建议:
    增加消费者, 从而加速消费效率
II. 多个生产者和消费者的情形
如上所诉, 需要调配好生产速度和消费速度, 从而使进程高效推进
"""
import queue
import threading
from time import sleep


class Consumer(threading.Thread):
    def __init__(self, name, slp_sec):
        threading.Thread.__init__(self)
        self.name = name
        self.slp_sec = slp_sec

    def run(self):
        global finish_flag
        global q
        global mutex
        while True:
            if finish_flag is True:
                if q.empty() is True:
                    break
            ele = q.get()
            mutex.acquire()
            print(self.name, ' take: ', ele)
            mutex.release()
            sleep(self.slp_sec)
        print('consume ALL')


class Producer(threading.Thread):
    def __init__(self, name, count):
        threading.Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        global finish_flag
        global q
        global mutex
        for i in range(0, self.count):
            mutex.acquire()
            print(self.name, ' give: ', i)
            mutex.release()
            q.put(i)
            sleep(0.5)
        finish_flag = True
        print('produce ALL')


def single_give_take():
    producer = Producer('producer', 10)
    producer.start()
    consumer = Consumer('consumer', 2)
    consumer.start()
    producer.join()
    consumer.join()
    print('single_give_take FINISH')


def multi_give_take():
    producer = Producer('producer', 20)
    producer.start()
    c1 = Consumer('consumer01', 2)
    c1.start()
    c2 = Consumer('consumer02', 1)
    c2.start()
    producer.join()
    c1.join()
    c2.join()
    print('multi_give_take FINISH')


finish_flag = False
q = queue.Queue(10)
mutex = threading.Lock()
if __name__ == "__main__":
    single_give_take()
    # multi_give_take()
