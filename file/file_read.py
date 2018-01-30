# encoding=utf-8
"""
TIPs:
1.关于python文件的close:
    A. 通过file对象的close方法关闭文件只是给该对象设置了一个状态位, 而该文件对象依然存在，但是我们无法再通过它来读取文件内容了。
因此在python中根本没有必要显式的去close()一个文件对象。
    B. 如果要在文件使用完毕关闭文件，可以用'with open(path) as file'的形式打开文件，因为file的exit方法中包含了其close操作。
"""
import json
import xlrd
import csv


def load_json(path):
    with open(path) as json_file:
        return json.load(json_file)


def read_excel():
    path = '../result/file_excel.xls'
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    nrows = sheet1.nrows
    ncols = sheet1.ncols
    # get all cell
    for rowx in range(0, nrows):
        for colx in range(0, ncols):
            print sheet1.cell(rowx, colx).value
    # get row
    for rowx in range(0, nrows):
        print sheet1.row_values(rowx)
    # get column
    for colx in range(0, ncols):
        print sheet1.col_values(colx)


def read_csv():
    path = 'path_to_csv_file'
    with open(path, 'rb') as f:
        rd = csv.reader(f)
        for row in rd:
            print 'row elements:', row


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
        python 2.x: print str,
        python 3.x: print(str,end='')
    """
    with open(path) as f:
        for l in f:
            print l.rstrip()
            # print l,


if __name__ == '__main__':
    root = "../data/"
    # load json
    data = load_json(root + 'statistic_170616-170623.json')
    for item in data:
        print "fid: ", item['fid']
    # read excel
    read_excel()
    # readlines from .txt
    lines = read_lines(root + "pgc-cid.txt")
    print lines
    print '------------------'
    print read(root + "pgc-cid.txt")
    # read line by line: return one line for each call
    print '--------- read line by line ---------'
    read_line_by_line(root + "pgc-cid.txt")
    print '--------- read by chunk ---------'
    for chk in read_chunks(root + "pgc-cid.txt"):
        print chk
