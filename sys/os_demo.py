# encoding=utf-8
"""
1. os.getcwd(): current work directory
2. os.mkdir(),os.rmdir()
3. os.path.join(), os.path.split()
4. os.environ
"""
import os

print('current work directory:', os.getcwd())
print("change work directory to '../':", os.chdir('../'))
print('current work directory:', os.getcwd())

# print("file path relative to 'cwd':", __file__)

fpath = os.path.realpath(__file__)
print("file pull path:", fpath)

print(os.path.split(fpath))
print(os.path.join('folder', 'fname'))

dir_path = './testdir'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
if os.path.exists(dir_path):
    os.rmdir(dir_path)

print(os.environ)
print("java home:", os.environ.get('JAVA_HOME'))
