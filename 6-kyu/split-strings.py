def solution(s):
    a = s + len(s)%2 * '_'
    return [a[c:c+2] for c,x in enumerate(a) if c%2==0]

'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''
