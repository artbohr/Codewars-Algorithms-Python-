def find_missing_numbers(arr):
    return [x for x in range(arr[0],arr[-1]) if x not in arr] if arr else []

'''
You will get an array of numbers.

Every preceding number is smaller than the one following it.

Some numbers will be missing, for instance:

[-3,-2,1,5] //missing numbers are: -1,0,2,3,4

Your task is to return an array of those missing numbers:

[-1,0,2,3,4]

'''
