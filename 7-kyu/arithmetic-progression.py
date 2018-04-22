def arithmetic_sequence_elements(a, r, n):
    num = a
    output = '{}, '.format(str(a))

    for _ in range(n-1):
        num += r
        output += '{}, '.format(num)

    return output[:-2]

'''
You have decided to write a function that will return the first n elements
of the sequence with the given common difference r and first element a.

The result should be a string of numbers, separated by comma and space.
Example

arithmetic_sequence_elements(1, 2, 5) == "1, 3, 5, 7, 9"
# first element: 1, difference: 2, how many: 5
'''
