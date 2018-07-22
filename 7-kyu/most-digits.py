def find_longest(arr):
    max = ''

    for x in arr:
        if len(str(x)) > len(str(max)):
            max = x

    return max

'''
Find the number with the most digits.

If two numbers in the argument array have the same number of digits,
return the first one in the array.
'''
