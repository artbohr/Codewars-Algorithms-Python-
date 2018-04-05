'''
If　a = 1, b = 2, c = 3 ... z = 26
Then l + o + v + e = 54
and f + r + i + e + n + d + s + h + i + p = 108
'''

def words_to_marks(s):
    return sum([ord(x) -96 for x in s])
