# encoding=utf-8

from memory_profiler import memory_usage
import time

FILE_PATH = "/Users/kevin/Dropbox/work/fid_dec.txt"


def count_lines():
    """
    WORST: with relatively lowest time- and memory-efficiency
    :return:
    """
    start = time.time()
    with open(FILE_PATH) as f:
        return len(f.readlines()), time.time() - start


def count_line_by_line():
    """
    most memory efficient, but with least time efficiency
    :return:
    """
    start = time.time()
    with open(FILE_PATH) as f:
        return sum(1 for l in f if l.rstrip()), time.time() - start


def count_by_buffer():
    """
    BEST: with relatively highest memory- and time-efficiency
    :return:
    """
    start = time.time()
    c = 0
    with open(FILE_PATH) as f:
        while True:
            buf = f.read(1024 * 1024)
            if not buf:
                break
            c += buf.count("\n")
    return c, time.time() - start


if __name__ == "__main__":
    print("`count_lines` result, time-costs, memory-usage:", count_lines(), max(memory_usage(count_lines)))
    print("`count_line_by_line` result, time-costs, memory-usage", count_line_by_line(), max(memory_usage(count_line_by_line)))
    print("`count_by_buffer` result, time-costs, memory-usage", count_by_buffer(), max(memory_usage(count_by_buffer)))
