def string_chunk(*args):
    if len(args)!=2 or type(args[1]) is not int or args[1]<1: return []
    return [args[0][x:x+args[1]] for x in range(0,len(args[0]),args[1])]

'''
You should write a function that takes a string and a positive integer n,
 splits the string into parts of length n and returns them in an array.
 It is ok for the last element to have less than n characters.

If n is not a valid size (> 0) (or is absent), you should return an empty array.

If n is greater than the length of the string, you should return an array with
 the only element being the same string.

Examples:

string_chunk('codewars', 2) # ['co', 'de', 'wa', 'rs']
string_chunk('thiskataeasy', 4) # ['this', 'kata', 'easy']
string_chunk('hello world', 3) # ['hel', 'lo ', 'wor', 'ld']
string_chunk('sunny day', 0) # []
'''
