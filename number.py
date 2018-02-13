# there are 4 number types in python
types = ['float', 'int', 'long', 'complex']
txt = "There're %s number types in python: %s, %s, %s, %s" % (len(types), types[0], types[1], types[2], types[3])
print(txt)

# type transform function
print("transform '2' to int: ", int('2'))
# print("transform '2' to long: ", long('2'))
print("transform '2' to float: ", float('2'))
print("create a complex: ", complex(2, ))
print("transform object to str: str(obj)")

# number stored in memory cannot be changed, so its better to 'delete' them after usage
num = 1
del num
try:
    print('num after del: ', num)
except:
    print('num is del after use')
