def switcher(arr):
    c = ''.join([chr(123-int(x)) for x in arr if int(x)>0])
    return c.replace('`','!').replace('_','?').replace('^',' ')

'''
Given an array of numbers, you must return a string. The numbers correspond
 to the letters of the alphabet in reverse order: a=26, z=1 etc.
 You should also account for '!', '?' and ' ' that are represented
 by '27', '28' and '29' respectively.

All inputs will be valid.
'''
