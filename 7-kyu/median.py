def median(arr):
    arr = sorted(arr)
    indx = len(arr)//2

    if (len(arr)/2).is_integer():
        return (arr[indx-1] + arr[indx]) / 2
    return arr[indx]

'''
Description:

The mean (or average) is the most popular measure of central tendency; however
it does not behave very well when the data is skewed (i.e. wages distribution).
In such cases, it's better to use the median.

Your task for this kata is to find the median of an array consisting of n elements.

You can assume that all inputs are arrays of numbers in integer format.
For the empty array your code should return NaN (false in JavaScript/NULL in PHP).

Examples:

Input [1, 2, 3, 4] --> Median 2.5

Input [3, 4, 1, 2, 5] --> Median 3

'''
