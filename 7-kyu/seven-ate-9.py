def seven_ate9(str_):
    output = ''
    str = '_{}_'.format(str_)

    for c, x in enumerate(str):
        if x == '9' and str[c-1] == '7'and str[c+1] == '7':
            continue
        output += x

    return output[1:-1]

'''
Write a function that removes every lone 9 that is inbetween 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'

Input: String of numbers
Output: String
'''
