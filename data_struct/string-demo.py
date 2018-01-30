# encoding=utf-8
"""
OUTLINE:
1. basic string operations
2. number format
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
print sql_tpl

# contain substring
print "'abc' in 'abc def':", 'abc' in 'abc def'
print ('__init__'.startswith('__'))
print ('__init__'.endswith('__'))

# substring--string is an array of char
print 'abc def'[:3]

# replace
print "replace '1' with 'one' for '12341234':", '12341234'.replace('1', 'one')

# join
print "join %s by ',': %s" % (range(0, 5), ','.join([str(i) for i in range(0, 5)]))

# ================================================================================================
"""
II. number format
"""
import math

# 小数位数控制
print 'e(3f)={:.3f}, e(6f)={:.6f}'.format(math.e, math.e)
# 总位数控制
print '12(3)={:03d}, e(6)={:06.3f}, e(8)={:08.3f}'.format(12, math.e, math.e)

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
print '------- regular expression ------'
# search
m_id = re.search(r'\(\d{1,}', sql)
print 'id:', m_id.group(0).replace('(', '')
m_dy = re.search(r'\'\d{8}\'', sql)
print 'douya num:', m_dy.group(0).replace(')', '')

# sub
sql = re.sub(r'\(`id`,\s', '(', sql, 1)
sql = re.sub(r'\(\d{1,},\s', '(', sql, 1)
print 'sql after truncated:', sql
print '-----------------------'

# ================================================================================================
"""
IV. string encoding(for python 2.x)
# 关于编码(unicode vs utf8):
- unicode是给各种不同的符号划分了编码序号范围,比如: 数字0-9占了[30,39]; 英文字符占了[41-7a],中文占了[4E00-9FCB].
- 而utf-8是基于unicode的一种存储方案, 它是一种变长存储方案: 比如数字/英文通常用一个字节存储, 而中文通常用3个字节存储; 
可想而知, 在unicode序列中越靠后的字符存储所需的字长越长。

字符串在Python内部的表示是unicode编码, 因此，在做编码转换时，通常需要以unicode作为中间编码:
    即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。

系统默认编码通常是ascii

str.decode:将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
str.encode:先将str转成unicode编码字符(系统默认操作--用ascii方式解码, 所以当str为非ascii编码字符时,将会报错--
    除非写成str.decode('src-encode').encode('dest-encode')), 然后将unicode编码字符转换成指定编码的字符串;
    如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
"""
tuple1 = (1, '\xe5\x88\x98')
print tuple1
# 下面三句话是等价的: 注意它们都不会改变原字符串, 而是在原字符串基础上生成一个新字符串
print '%s: %s' % (tuple1[0], tuple1[1])
print '%s: %s' % (tuple1[0], unicode(tuple1[1], encoding='utf8'))
print '%s: %s' % (tuple1[0], tuple1[1].decode('utf8'))

import sys

print sys.getdefaultencoding()
s = '中文'
s.decode('utf8').encode('gb18030')

# 如下代码将报错
# s.encode('gb18030')

# byte number in a string
print "bytes of '1234': %s" % len(bytearray("1234"))
print "bytes of 'hello': %s" % len(bytearray("hello"))
print "bytes of '你好': %s" % len(bytearray("你好"))

# ================================================================================================
