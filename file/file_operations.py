# encoding=utf-8
"""
file operations other than w/r
---
1. list file in folder: os.walk, os.listdir
2. check exist: os.path.isfile
3. del file: os.remove
4. compress/uncompress file: gzip

"""
import os
import errno
import gzip, shutil


def list_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


def list_files_recursively(root):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(root):
        for fn in filenames:
            f = os.path.join(dirpath, fn)
            if os.path.isfile(f):
                files.append(f)
    return files


def check_exist(fpath):
    return os.path.isfile(fpath)


def del_file(fpath):
    # check before del
    if os.path.isfile(fpath):
        os.remove(fpath)
    else:
        print 'file not exist'
    # without check -- py2
    try:
        os.remove(fpath)
    except OSError as e:
        if e.errno == errno.ENOENT: # errno.ENOENT = no such file or directory
            print 'file not exist'
        else:
            raise
    # without check -- py3
    # with contextlib.suppress(FileNotFoundError):
    #     os.remove(fpath)


def gzip_content(c, dest):
    '''
    compress content & write it into a destination file
    '''
    with gzip.open(dest, 'wb') as f:
        f.write(c)


def gzip_file(src, dest):
    '''
    compress source file into destination files
    '''
    with open(src, 'rb') as f_src, gzip.open(dest, 'wb') as f_dest:
        shutil.copyfileobj(f_src, f_dest)


def ungzip_file(src, dest):
    '''
    uncompress src zip file into destination file
    '''
    with gzip.open(src, 'rb') as f_in, open(dest, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    # list file (recursively)
    print '---list file'
    fs = list_files("../data")
    for i in range(0, len(fs)):
        print "%s: %s" % (i, fs[i])
    print '---list file recursively'
    fs = list_files_recursively("../data")
    for i in range(0, len(fs)):
        print "%s: %s" % (i, fs[i])
    # check exist
    print '---check file existence'
    print "is 'data/hello.sh' exist:", check_exist('../data/hello.sh')
    print "is 'data/hello.txt' exist:", check_exist('../data/hello.txt')
    # del file
    print '---delete file'
    del_file('../data/2010.01.01.log')
    # compress
    gzip_content('hello, gzip', '../data/hello.gz')
    gzip_file('../data/fileinfo_445792.json', '../data/fileinfo_445792.json.gz')
    # uncompress
    ungzip_file('../data/hello.gz', '../data/hello-gzip.txt')
