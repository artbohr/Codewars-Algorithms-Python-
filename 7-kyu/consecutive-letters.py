from string import ascii_lowercase as alphabet

def solve(st):
    sr_s = ''.join(sorted(st))
    start = ord(sr_s[0]) - 97
    return sr_s == alphabet[start:start+len(st)]

'''
In this Kata, we will check if a string contains consecutive letters as they
 appear in the English alphabet and if each letter occurs only once.

For example:
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True

All inputs will be lowercase letters.
'''
