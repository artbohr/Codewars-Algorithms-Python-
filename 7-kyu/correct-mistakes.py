def correct(string):
    output = ''
    for i in string:
        if i in '015':
            output += {'0':'O','1':'I','5':'S'}.get(i)
            continue
        output += i
    return output

'''
Character recognition software is widely used to digitise printed texts.
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter),
are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text.
You only have to handle the following mistakes:

    S is misinterpreted as 5
    O is misinterpreted as 0
    I is misinterpreted as 1

The test cases contain numbers only by mistake.
'''
