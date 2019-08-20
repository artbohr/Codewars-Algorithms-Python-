from functools import reduce
import operator

def multi(lst):
    return reduce(operator.mul, lst)
def add(lst):
    return sum(lst)
def reverse(string):
    return string[::-1]

'''
here are three functions:
Multiplication (x)
Addition (+)
and
Reverse (!esreveR)

first two use lists as input, last one a string.
'''
