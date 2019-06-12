def string_parse(string):
    if not type(string) == str: return "Please enter a valid string"
    output = ""
    seq = ""

    for i, letter in enumerate(string):
        if i!=len(string)-1 and letter == string[i+1]:
            seq+=letter
        elif seq:
            seq+=letter
            output += seq[:2]
            if len(seq)>2:
                output += "[{}]".format(seq[2:])
            seq = ""
        else:
            output += letter

    return output

'''
Create a program that will take in a string as input and, if there are duplicates
 of more than two alphabetical characters in the string, returns the string with
 all the extra characters in a bracket.

For example, the input "aaaabbcdefffffffg" should return "aa[aa]bbcdeff[fffff]g"

Please also ensure that the input is a string, and return "Please enter a valid
 string" if it is not.

'''
