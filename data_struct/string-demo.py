# encoding=utf-8
"""
OUTLINE:
1. basic string operations
2. number format
2b. string format
3. regular expression
4. string encoding(for python 2.x)
"""
# ================================================================================================
"""
I. basic string operations
"""
sql_tpl = '''
    SELECT mac.fid,mac.ekey,mac.evalue,mac.insert_time,mac.last_update_time,man.ekey,man.evalue FROM 
    fileextend_inner_0 mac LEFT JOIN
    fileextend_inner_0 man ON mac.fid=man.fid
    WHERE mac.insert_time>='2017-06-16 00:00:00' AND mac.insert_time<'2017-06-23 00:00:00' AND mac.ekey='av_scan_result'
    AND man.ekey='category' AND man.evalue='adult_video'
    '''
print(sql_tpl)

# contain substring
print("'abc' in 'abc def':", 'abc' in 'abc def')
print('__init__'.startswith('__'))
print('__init__'.endswith('__'))

# substring--string is an array of char
print('abc def'[:3])

# replace
print("replace '1' with 'one' for '12341234':", '12341234'.replace('1', 'one'))

# join
print("join %s by ',': %s" % (range(0, 5), ','.join([str(i) for i in range(0, 5)])))

# ================================================================================================
"""
II. number format
"""
import math

# 小数位数控制
print('e(3f)={:.3f}, e(6f)={:.6f}'.format(math.e, math.e))
# 总位数控制
print('12(3)={:03d}, e(6)={:06.3f}, e(8)={:08.3f}'.format(12, math.e, math.e))

# string format
in_a = 'hello'
in_b = 'py3'
fstr1 = f"{in_a}, {in_b}!"
fstr2 = "{0}, {1}!".format(in_a, in_b)
print("format 1:", fstr1)
print("format 2:", fstr2)

# ================================================================================================
"""
III. regular expression
1. re.match(pattern, string, flags=0)
    - re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
    - flag标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。多个flag用|号分隔
```
    re.I: 使匹配对大小写不敏感
    re.L: 做本地化识别（locale-aware）匹配
    re.M: 多行匹配，影响 ^ 和 $
    re.S: 使 . 匹配包括换行在内的所有字符
    re.U: 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X: 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
```
2. re.search(pattern, string, flags=0)
    - re.search 扫描整个字符串并返回第一个成功的匹配。
3. re.sub(pattern, repl, string, count=0, flags=0)
    - re.sub用于替换字符串中的匹配项。
    - repl: 替换的字符串，也可为一个函数。
    - count: 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
import re

sql = '''
INSERT INTO `gain_task` (`id`, `user_name`, `fid`, `status`, `create_Time`, `update_Time`, `review_status`) 
VALUES (1422, '88377560', 5465803, 0, '2017-1-18 10:08:26', '2017-1-18 10:24:52', 300);
'''
sql2 = '''
INSERT INTO `gain_task` (`id`, `user_name`, `fid`, `status`, `create_Time`, `update_Time`, `review_status`) VALUES (1422, 
'v-yuliu', 5465803, 0, '2017-1-18 10:08:26', '2017-1-18 10:24:52', 300);
'''
print('------- regular expression ------')
# search
m_id = re.search(r'\(\d{1,}', sql)
print('id:', m_id.group(0).replace('(', ''))
m_dy = re.search(r'\'\d{8}\'', sql)
print('douya num:', m_dy.group(0).replace(')', ''))

# sub
sql = re.sub(r'\(`id`,\s', '(', sql, 1)
sql = re.sub(r'\(\d{1,},\s', '(', sql, 1)
print('sql after truncated:', sql)
print('-----------------------')

# ================================================================================================
"""
IV. string encoding(for python 3.x)
1. 编码
- py3.x采用unicode编码字符串(py2.x用ascii编码)

2. bytes vs bytearray
- bytes是不可变的，同str;
- bytearray是可变的，同list。
"""
import sys

print("system default encoding:", sys.getdefaultencoding())
s = '中文'
# str 2 bytes/bytearray: encode(), bytes(), bytearray()
print("'utf8' bytes of %s: %s" % (s, s.encode('utf8')))
print("'gb18030' bytes of %s: %s" % (s, s.encode('gb18030')))
print("'utf8' bytes of %s: %s" % (s, bytes(s, 'utf8')))
print("'utf8' bytearray of %s: %s" % (s, bytearray(s, 'utf8')))

# bytes/bytearray 2 str: decode(), str()
print("str of 'utf8' bytes %s: %s" % (s.encode('utf8'), s.encode('utf8').decode('utf8')))
print("str of 'utf8' bytearray %s: %s" % (bytearray(s, 'utf8'), bytearray(s, 'utf8').decode('utf8')))
print("str of 'utf8' bytes %s: %s" % (s.encode('utf8'), str(s.encode('utf8'), 'utf8')))

# byte size of a string
print("byte size of '%s': %s" % ("1234", len(bytes("1234", "utf8"))))
print("byte size of '%s': %s" % ("hello", len(bytes("hello", 'utf8'))))
print("byte size of '%s': %s" % ("你好", len(bytearray("你好", 'utf-8'))))

# bytes vs bytearray
print("bytes(%s) 2 bytearray:%s" % (bytes(s, 'utf8'), bytearray(bytes(s, 'utf8'))))
print("bytearray(%s) 2 bytes:%s" % (bytearray(s, 'utf8'), bytes(bytearray(s, 'utf8'))))

# ================================================================================================
