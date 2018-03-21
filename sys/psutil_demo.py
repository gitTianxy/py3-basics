# coding=utf8
"""
psutil, process and system utilities: 一个获取系统信息的第三方包. 可以跨平台使用, 支持Linux／UNIX／OSX／Windows等.
---
1. 获取CPU信息
2. 获取内存信息
3. 获取磁盘信息
4. 获取网络信息
5. 获取进程信息
"""
import psutil
from pprint import pprint


def cpu_info():
    print("logical cpu count:", psutil.cpu_count())
    print("real cpu count:", psutil.cpu_count(logical=False))
    print("cpu times:", psutil.cpu_times())
    print("cpu percents:")
    for i in range(5):
        print(psutil.cpu_percent(interval=1, percpu=True))


def memory_info():
    print("virtual m:", psutil.virtual_memory())
    print("swap m:", psutil.swap_memory())


def disk_info():
    print("disk partitions:", psutil.disk_partitions())
    print("disk usage:", psutil.disk_usage('/'))
    print("disk io:", psutil.disk_io_counters())


def net_info():
    print("net io:", psutil.net_io_counters())
    print("net address:", psutil.net_if_addrs())
    print("net status:", psutil.net_if_stats())


def process_info():
    pids = psutil.pids()
    print("pids:", pids)
    p0 = psutil.Process(pids[0])
    print(f"process {pids[0]}: {p0}")
    p0_info = {
        'pid': p0.pid,
        'name': p0.name(),
        'status': p0.status(),
        'username': p0.username(),
        'exe': p0.exe(),
        'cwd': p0.cwd(),
        'crt_time': p0.create_time(),
        'cpu_times': p0.cpu_times(),
        'm_info': p0.memory_info(),
        'parent': p0.parent(),
        'ppid': p0.ppid(),
        'children': p0.children(),
        'threads': p0.threads(),
        'connections': p0.connections(),
        'open_files': p0.open_files(),
        'environ': p0.environ()
    }
    pprint(p0_info)
    # print("ps:")
    # print(psutil.test())


if __name__ == '__main__':
    cpu_info()
    memory_info()
    disk_info()
    net_info()
    process_info()
