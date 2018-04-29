def accum(s):
    output = ''

    for x in range(len(s)):
        output += '-{}{}'.format(s[x].upper(),s[x].lower()*(x+1))[:-1]

    return output[1:]

'''
Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
