def reverse(a):
    str_a = "".join(a)[::-1]
    output = []
    iter = 0

    for x in a:
        l = len(x)
        output.append(str_a[iter:iter+l])
        iter+=l

    return output

'''
Task

Given an array of strings, reverse them and their order in such way that
 their length stays the same as the length of the original inputs.
 
Example:

Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
'''
