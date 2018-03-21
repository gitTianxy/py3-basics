# coding=utf8
"""
I. io模块的3种I/O
1. 原始I/O，即RawIOBase及其子类, 也被称为无缓存I/O:
    操作底层块，既可以用于文本I/O，也可以用于字节I/O。不推荐使用。
2. 文本I/O，即TextIOBase及其子类:
    读取一个str对象，得到一个str对象。
3. 字节I/O，即BufferedIOBase及其子类, 也称为缓存I/O:
    读取一个bytes-like对象，得到一个bytes对象

II. thread-safe

III. CPU高速 vs IO设备的龟速
解决CPU高速执行能力和IO设备的龟速严重不匹配, 有多种不同的方案:
1. 并发(多进程/多线程): 同时处理多个(同步)io操作
2. 异步io: 当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码;当IO返回结果时，再通知CPU进行处理。
"""
from io import StringIO
from io import BytesIO


class StringIODemo:
    """
    StringIO经常被用来作为字符串的缓存, 可以理解为"内存文件对象",
    包含read, readline, readlines, write, writelines等api方法
    ---
    Tips:
        0. 游标控制
            A. 初始化后游标位于起始位置
            B. write(): 从游标开始写入, 每写入一个字符游标往后移动一位
            C. read()/readlines(): 从游标开始读到末尾, 读完后游标置于尾部
            D. getvalue(): 从头读到尾, 读完后游标返回到读之前的位置
    """

    def __init__(self):
        sio = StringIO("==='StringIO' demo===\n")
        # 不seek到末尾, 初始化内容将被覆盖
        sio.seek(len(sio.getvalue()))
        sio.write('line\n')
        print("round 1:", sio.getvalue())
        lines = [f"line{i}\n" for i in range(10)]
        sio.writelines(lines)
        print("round 2:", sio.getvalue())
        # 跳转到开头
        sio.seek(0)
        print("round 3:", sio.readlines())
        sio.close()


class BytesIODemo:
    def __init__(self):
        bio = BytesIO()
        bio.write("==='ByteIO' demo===\n".encode('utf8'))
        print("round 1:", bio.getvalue().decode('utf8'))
        bio.writelines([f"line{i}\n".encode('utf8') for i in range(10)])
        print("round 2:", bio.getvalue().decode('utf8'))
        bio.close()


if __name__ == "__main__":
    StringIODemo()
    BytesIODemo()
