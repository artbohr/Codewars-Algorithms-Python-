def happy_g(s):
    s = " {}".format(s)
    for x in range(1, len(s)-1):
        if s[x]=='g' and (s[x+1]!='g' and s[x-1]!='g'):
            return False
    return True

'''
Task

Let's say that "g" is happy in the given string, if there is
 another "g" immediately to the right or to the left of it.

Find out if all "g"s in the given string are happy.
Example

For str = "gg0gg3gg0gg", the output should be true.

For str = "gog", the output should be false.
Input/Output

    [input] string str

    A random string of lower case letters, numbers and spaces.

    [output] a boolean value

    true if all "g"s are happy, false otherwise.


'''