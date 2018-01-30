# encoding=utf-8
"""
int/long
float
math constants

"""
import math


# int/long

# float
print 'float abs of -5 and -5.00: %s, %s' % (math.fabs(-5), math.fabs(-5.00))
print 'ceil of 1.05: %s' % math.ceil(1.05)
print 'floor of 1.05: %s' % math.floor(1.05)
print 'round(1.05)=%s, round(1.05, 1)=%s, round(1.05, 3)=%s' % (round(1.05), round(1.05, 1), round(1.05, 3))

# math constants
print "PI: ", math.pi
print "e: ", math.e
