def lstzip(a,b,fn):
    return [fn(x[0], x[1]) for x in zip(a, b)]

'''
lstzip

that merges the corresponding elements of two sequences using a specified
 selector function fn (a block in Ruby)

For example:

a = [1, 2, 3, 4, 5]
b = ['a', 'b']
lstzip(a,b, lambda a,b: str(a)+str(b))

a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']
lstzip(a,b, lambda a, b: a * ord(b[0]))

if arrays have different lengths, go up to the minimum length and then stop.

'''
