def is_nice(arr):
    if not arr: return False

    for x in arr:
        if x-1 not in arr and x+1 not in arr:
            return False
    return True

'''
A Nice array is defined to be an array where for every value n in the array,
 there is also an element n-1 or n+1 in the array.

example:

[2,10,9,3] is a Nice array because

2=3-1
10=9+1
3=2+1
9=10-1

Write a function named isNice/IsNice that returns true if its array argument is
 a Nice array, else false. You should also return false if input array has no elements.

'''
