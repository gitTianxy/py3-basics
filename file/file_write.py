# coding=utf-8
import xlwt
from xlutils.copy import copy
from xlrd import open_workbook
import os.path


def crt_file(path, lines):
    with open(path, "w") as f:
        f.write(line)
        f.writelines(lines)


def append_file(path, lines):
    with open(path, "a") as f:
        f.writelines(lines)


def crt_excel(path, lines):
    workbook = xlwt.Workbook(encoding='utf-8') # ascii
    worksheet = workbook.add_sheet('My Worksheet')
    for idx in range(0, len(lines)):
        worksheet.write(idx, 0, label=lines[idx])
    workbook.save(path)


def append_excel(path):
    """
    append column or row
    :param path:
    :return:
    """
    if not os.path.isfile(path):
        wb = xlwt.Workbook(encoding='utf-8')
        wb.add_sheet('my sheet')
        wb.save(path)
    # open file
    wb = open_workbook(path)
    sheet = wb.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    # creates a writeable copy
    book = copy(wb)
    sheet1 = book.get_sheet(0)
    # append column
    for colx in range(ncols, ncols+2):
        for rowx in range(0, nrows):
            sheet1.write(rowx, colx, 'new colume %s' % colx)
    # append row
    for rowx in range(nrows, nrows+10):
        sheet1.write(rowx, 0, 'new row %s' % rowx)
    # save
    book.save(path)


line = None
lines = []
if __name__ == "__main__":
    # init content
    root = "../result"
    line = "hello, this is a write-line\n"
    for i in range(0, 10):
        lines.append("this is line %s\n" % i)
    append_lines = [l.replace("\n", "") + " new\n" for l in lines]

    crt_file(root + '/file.txt', lines)
    append_file(root + '/file.txt', append_lines)
    crt_excel(root + '/excel.xls', lines)
    append_excel(root + '/excel.xls')
