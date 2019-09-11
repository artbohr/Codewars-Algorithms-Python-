def array_mash(a, b):
    output = []
    for x in range(len(a)):
       output.append(a[x])
       output.append(b[x])
    return output

'''
Mash 2 arrays together so that the returning array has alternating
 elements of the 2 arrays . Both arrays will always be the same length.

eg. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']

'''