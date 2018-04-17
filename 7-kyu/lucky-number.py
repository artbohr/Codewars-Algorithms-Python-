def is_lucky(n):
    return (sum([int(x) for x in str(n)]) / 9.0 ).is_integer()

'''
Write a function to find if a number is lucky or not.
If the sum of all digits is a multiple of 9 then the number is lucky.

1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisble by 9, hence number is lucky.

Function will return true for lucky numbers and false for others.
'''
