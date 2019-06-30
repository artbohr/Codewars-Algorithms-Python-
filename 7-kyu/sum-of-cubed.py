def cube_odd(arr):
    if len([x for x in arr if isinstance(x,int)])!=len(arr): return None
    return sum(x**3 for x in arr if x%2!=0)

'''
Find the sum of the odd numbers within an array, after cubing the initial integers.
 This function will return undefined (NULL in PHP) if any of the values aren't numbers. 
'''
