def spacify(string):
    return ''.join(x+' ' for x in string)[:-1]

'''
Modify the spacify function so that it returns the given string with
 spaces insertedbetween each character.

spacify("hello world") === "h e l l o   w o r l d"
'''