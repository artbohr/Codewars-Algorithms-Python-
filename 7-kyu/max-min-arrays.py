def solve(arr):
    arr_s = sorted(arr)
    arr_l = len(arr_s)
    output = []

    for x in range(arr_l//2+1):
        output.append(arr_s[-(x+1)])
        output.append(arr_s[x])

    return output[:-1] if arr_l%2!=0 else output[:-2]

'''
In this Kata, you will be given an array of unique elements, and your task is to
 rerrange the values so that the first max value is followed by the first minimum,
 followed by second max value then second min value, etc.

For example:

solve([15,11,10,7,12]) = [15,7,12,10,11]

The first max is 15 and the first min is 7. The second max is 12 and the
 second min is 10 and so on.

More examples in the test cases.

Good luck!

'''
