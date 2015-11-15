def returnTwo():
    return 20,30

x,y = returnTwo()
print x,y

def mul(x,y):
    return x*y

print reduce(mul, range(1,5))

def cubeFunc(x):
    """
    Return the cube value
    """
    return x*x*x

print map(cubeFunc, range(1,11))

def myAdd(var1, var2 = 10):
    return var1 + var2

print myAdd(7)
print myAdd(8,5)
