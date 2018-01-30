# encoding=utf-8
"""
add/subtract
multiply/divide
exponent/logarithm
powers/roots
bitwise operations(boolean logic operations)
absolute
modulus
comparisons
"""
import math

# add/subtract...

# multiply
print '0.1*55=', 0.1 * 55
# divide
print '2/3=%s, float(2)/float(3)=%s, 2//3=%s' % (2 / 3, float(2) / float(3), 2 // 3)
print '10/4=%s, float(10)/float(4)=%s, 10//4=%s' % (10 / 4, float(10) / float(4), 10 // 4)

# exponent
print 'exp(1): ', math.exp(1)
# logarithm
for i in range(1, 10):
    print 'ln(%s): %s, 2^ln(%s): %s, 2.5^ln(%s): %s, 3^ln(%s): %s' % (
    i, math.log(i), i, math.pow(2, math.log(i)), i, math.pow(2.5, math.log(i)), i, math.pow(3, math.log(i)))
print 'ln(e): ', math.log(math.e)
print 'log10(100): ', math.log(100, 10)

# powers
print "2^3, 2.0^3.0--use '**': %s, %s" % (2 ** 3, 2.0 ** 3.0)
print "2^3, 2.0^3.0--use 'math.pow()': %s, %s" % (math.pow(2, 3), math.pow(2.0, 3.0))
# roots
print "sqrt(4):%s, math.pow(4, 0.5):%s" % (math.sqrt(4), math.pow(4, 0.5))

# bitwise operations
print("2 >> 2 = " + str(2 >> 2))  # 右移
print("2 << 2 = " + str(2 << 2))  # 左移
print("2 & 3 = " + str(2 & 3))  # 0010 & 0011 = 0010
print("2 | 3 = " + str(2 | 3))  # 0010 | 0011 = 0011
print("2 ^ 3 = " + str(2 ^ 3))  # 异或(不同返回1,相同返回0); 0010 ^ 0011 = 0001
print "~2 =", ~2 # 按位取反; 10 -> 01 = -(2+1)=-3

# absolute
print 'abs of -5 and -5.00: %s, %s' % (abs(-5), abs(-5.00))
print 'float abs of -5 and -5.00: %s, %s' % (math.fabs(-5), math.fabs(-5.00))

# modulus
print "%s mod %s: %s" % (122, 2, 122 % 2)

# comparisons
print '2 is less than 3: ', cmp(2, 3) == -1
print 'max in {1,2,3,4} is: ', max(1, 2, 3, 4)
print 'min in {1,2,3,4} is: ', min(1, 2, 3, 4)
