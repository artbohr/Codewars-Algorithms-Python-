def closest_multiple_10(i):
    r = i % 10
    return i - r if r < 5 else i + 10 - r

'''
Given a number return the closest number to it
 that is divisible by 10.

Example input:

22
25
37

Expected output:

20
30
40
'''