def find_uniq(arr):
    return next(x for x in set(arr) if arr.count(x) == 1)

'''
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains more than 3 numbers.
'''
