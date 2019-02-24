def pop_shift(s):
    s = list(s)
    output_pop,output_shift = '', ''

    for x in range(len(s)):
        if len(s)>1:
            output_pop+=s.pop()
            output_shift+=s.pop(0)

    return [output_pop,output_shift,''.join(s)]

'''
You will be given a string.

You need to return an array of three strings by gradually pulling apart the string.

You should repeat the following steps until the string length is 1:

a) remove the final character from the original string, add to solution
 string 1. b) remove the first character from the original string,
 add to solution string 2.

The final solution string value is made up of the remaining character from
 the original string, once originalstring.length == 1.

Example:

"exampletesthere" becomes: ["erehtse","example","t"]

The Kata title gives a hint of one technique to solve.

'''
