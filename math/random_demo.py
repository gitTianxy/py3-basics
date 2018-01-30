# encoding=utf-8
"""
random choice from list
random generation within a range
shuffle/disorderordered list
"""
import random
import numpy

# random choice from list
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print "randomly choice an element from %s: %s" % (nums, random.choice(nums))
print "randomly choice 3 elements from %s: %s" % (nums, random.sample(nums, 3))
print "randomly choice an element from %s: %s" % (range(0, 10), random.randrange(0, 10))
print "randomly choice an element from %s: %s" % (range(0, 10, 2), random.randrange(0, 10, 2))

"""
random generation within a range
"""
# numpy.random.uniform([low, high, size])/random.uniform(low, high)       均匀分布随机变量
print "randomly generate a number within [0, 1):", random.random()
print "randomly generate a number within [0, 1):", numpy.random.uniform(0, 1)
print "randomly generate a number within [0, 1):", random.uniform(0, 1)

# numpy.random.beta(a, b[, size])                  Beta分布随机变量

# numpy.random.binomial(n, p[, size])            二项分布随机变量

# numpy.random.chisquare(df[, size])            卡方分布随机变量

# numpy.random.dirichlet(alpha[, size])           狄利克雷分布随机变量

# numpy.random.exponential([scale, size])/random.expovariate(lambd)     指数分布随机变量

# numpy.random.geometric(p[, size])               几何分布随机变量

# numpy.random.normal([loc, scale, size])/random.gauss(mu, sigma)/random.normalvariate(mu, sigma)       正态分布随机变量

# numpy.random.poisson([lam, size])                泊松分布随机变量

# numpy.random.wald(mean, scale[, size])        Wald分布随机变量

# shuffle ordered list
nums = range(0, 10)
print "shuffle an array. before:", nums
random.shuffle(nums)
print "shuffle an array. after:", nums
