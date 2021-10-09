from math import sqrt
def op_fib(num):
    return ((1+sqrt(5))**num-(1-sqrt(5))**num)/(2**num*sqrt(5))
