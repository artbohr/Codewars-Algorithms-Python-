def capitals(word):
    return [c for c,i in enumerate(word) if i.upper() == i]

'''
Instructions

Write a function that takes a single string (word) as argument.
The function must return an ordered list containing the indexes
of all capital letters in the string.

Example

Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
'''
