# coding=utf-8
# __author__='kevintian'

# for-loop
print 'FOR-LOOP'
for letter in 'Python':  # 第一个实例
    if letter == 't':
        print "i am t"
    else:
        print letter

# while-loop
print 'WHILE-LOOP'
idx = 0
while idx < 10:
    print 'idx=%s' % idx
    idx += 1
else:
    print 'idx=%s, escape from the loop' % idx

