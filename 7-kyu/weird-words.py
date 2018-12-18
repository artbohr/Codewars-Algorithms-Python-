def next_letter(string):
    output = ''

    for x in string:
        if x.isalpha():
            if x == 'Z' or x == 'z':
                output += chr(ord(x)-25)
            else:
                output += chr(ord(x)+1)
        else:
            output += x

    return output

'''
In this kata you will have to change every letter in a given string to the next
 letter in the alphabet. You will write a functionnextLetter to do this.
  The function will take a single parameter str (string).

EXAMPLES:

"Hello" --> "Ifmmp"

"What is your name?" --> "Xibu jt zpvs obnf?"

"zoo" --> "app"

"zzZAaa" --> "aaABbb"

Note: spaces and special characters should remain the same.
 Capital letters should transfer in the same way but remain capitilized.

'''
