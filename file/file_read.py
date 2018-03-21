# encoding=utf-8
"""
read file demos:
1. load json
2. read excel
3. read csv
4. read as a whole, by lines, by line, by chunk
---
TIPs:
1.关于python文件的close:
    A. 通过file对象的close方法关闭文件只是给该对象设置了一个状态位, 而该文件对象依然存在，但是我们无法再通过它来读取文件内容了。
因此在python中根本没有必要显式的去close()一个文件对象。
    B. 如果要在文件使用完毕关闭文件，可以用'with open(path) as file'的形式打开文件，因为file的exit方法中包含了其close操作。
2. 磁盘r/w
在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘.
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
3. 读文件方式: as a whole, by lines, by line, by chunk
4. 文件类型: 文本文件(不同编码'utf8-default','gbk',...), 二进制文件
    要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
"""
import json
import xlrd
import csv


def load_json(path):
    with open(path) as json_file:
        return json.load(json_file)


def read_excel():
    path = '../data/av_screenshot_src.xlsx'
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    nrows = sheet1.nrows
    ncols = sheet1.ncols
    # get all cell
    for rowx in range(0, 10 if nrows > 10 else nrows):
        for colx in range(0, ncols):
            print("cell(%s,%s):%s" % (rowx, colx, sheet1.cell(rowx, colx).value))
    print("...")
    # get row
    for rowx in range(0, 10 if nrows > 10 else nrows):
        print("row %s: %s" % (rowx, sheet1.row_values(rowx)))
    print("...")
    # get column
    for colx in range(0, ncols):
        print("col %s: %s" % (colx, sheet1.col_values(colx)[0:10]))


def read_csv():
    path = 'path_to_csv_file'
    with open(path, 'rb') as f:
        rd = csv.reader(f)
        for row in rd:
            print('row elements:', row)


def read(path):
    with open(path, 'r') as f:
        return f.read()


def read_lines(path):
    with open(path) as f:
        return [l.rstrip() for l in f.readlines()]


def read_chunks(path, size=1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1K
    """
    with open(path) as f:
        while True:
            chunk_data = f.read(size)
            if not chunk_data:
                break
            yield chunk_data


def read_line_by_line(path):
    """
    由open(path)得到的file对象就是一个line iterator.
    print不换行的小trick:
        python 2.x: print(str,)
        python 3.x: print(str,end='')
    """
    with open(path) as f:
        c = 1
        for l in f:
            if c > 10:
                break
            print(l.rstrip())
            c += 1
        print("...")


if __name__ == '__main__':
    root = "../data/"
    # load json
    print("---load json")
    data = load_json(root + 'statistic_170616-170623.json')
    for i in range(0, 10 if len(data) > 10 else len(data)):
        print(data[i])
    print("...")
    # read excel
    print("---read excel")
    read_excel()
    # readlines from .txt
    print("---read lines")
    lines = read_lines(root + "pgc-cid.txt")
    print(lines[0:10])
    print("---read(all)")
    print(read(root + "pgc-cid.txt"))
    # read line by line: return one line for each call
    print('---read line by line')
    read_line_by_line(root + "pgc-cid.txt")
    print('---read by chunk')
    c = 1
    for chk in read_chunks(root + "pgc-cid.txt", size=64):
        if c > 10:
            break
        print("chunk %s:\n %s" % (c, chk))
        c += 1
