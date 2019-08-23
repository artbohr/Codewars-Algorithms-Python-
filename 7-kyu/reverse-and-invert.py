def reverse_invert(lst):
    output = []

    for x in lst:
        if type(x)==int:
            x = str(x*-1)
        else:
            continue
        x = x[0] + x[1:][::-1] if x[0]=='-' else x[::-1]
        output.append(int(x))
    return output

'''
Reverse and invert all integer values in a given list.

Python:

reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
'''
