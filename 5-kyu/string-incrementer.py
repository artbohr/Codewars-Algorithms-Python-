'''
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number the number 1 should be appended to the new string.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

import re


def increment_string(strng):
    if not re.search('\d', strng):
        return strng + '1'

    num = ''.join(re.findall(r'\d+$', strng))
    rest = ''.join(re.findall(r'(?!\d+$).', strng))
    zeroes = '0' * (len(num) - len(str(int(num) + 1)))

    return rest + zeroes + str(int(num) + 1)


increment_string("@&Clzw^26P8u[3_2/x81#6.X6070J*\=I,u37du+C4>O'C88723464h.$li_76158200403187")
# Returns: @&Clzw^26P8u[3_2/x81#6.X6070J*\=I,u37du+C4>O'C88723464h.$li_76158200403188
