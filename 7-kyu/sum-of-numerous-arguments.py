def find_sum(*args):
    return sum(args) if all(x >= 0 for x in args) else -1

'''
After calling the function findSum() with any number of non-negative integer
arguments, it should return the sum of all those arguments. If no arguments
are given, the function should return 0, if negative arguments are given,
it should return -1.

Examples:
find_sum(1,2,3,4); # returns 10
find_sum(1,-2);    # returns -1
find_sum();        # returns 0
'''
