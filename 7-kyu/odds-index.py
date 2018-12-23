def odd_ball(arr):
    for x in arr:
        if isinstance(x,int) and x<len(arr) and arr[x]=='odd':
            return True
    return False

'''
You are given an array with several "even" words, one "odd" word, and some numbers mixed in.

Determine if any of the numbers in the array is the index of the "odd" word. If so,
 return true, otherwise false.
'''
