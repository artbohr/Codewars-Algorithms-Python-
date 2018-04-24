def hex_hash(code):
    sum = 0

    for x in code:
        for i in hex(ord(x))[2:]:
            if i.isdigit():
                sum+=int(i)
    return sum

'''
Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy! Every character of the string should be
converted to the hex value of its ascii code, then the result should be
the sum of the numbers in the hex strings (ignore letters).
Examples

"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113
'''
