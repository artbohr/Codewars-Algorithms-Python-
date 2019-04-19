def char_to_ascii(string):
    if not string: return None
    output = {}
    for x in string:
        if x not in output and x.isalpha():
            output[x] = ord(x)
    return output

'''
Take a string and return a hash with all the ascii values of the
 characters in the string. Returns nil if the string is empty.
 The key is the character, and the value is the ascii value of the character.
 Repeated characters are to be ignored and non-alphebetic characters as well.
'''
