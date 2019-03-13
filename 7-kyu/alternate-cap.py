def capitalize(s):
    output = ''

    for i,x in enumerate(s.lower()):
        if i%2==0:
            output += x.upper()
        else:
            output += x

    return [output, output.swapcase()]

'''
Given a string, capitalize the letters that occupy even indexes and odd indexes
 separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF'].
 See test cases for more examples.

The input will be a lowercase string with no spaces.
'''
