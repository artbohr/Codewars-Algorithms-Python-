def diamond(n):
    if n % 2 == 0 or n < 1:
        return None

    output = ''

    for i in range(1, n + 1):
        if i % 2 != 0:
            if i == n:
                output += i * '*' + '\n'
            else:
                output += ' ' * ((n - i) // 2) + i * '*' + '\n'

    for x in range(n - 1, 0, -1):
        if x % 2 != 0 and x + 1 != n:
            output += ' ' * ((n - x) // 2) + x * '*' + '\n'

    return output

'''
You need to return a string that displays a diamond shape on the screen using
asterisk ("*") characters. Please see provided test cases for exact output format.

The shape that will be returned from print method resembles a diamond, where the
number provided as input represents the number of *’s printed on the middle line.
The line above and below will be centered and will have 2 less *’s than the middle line.
This reduction by 2 *’s for each line continues until a line with a single * is
printed at the top and bottom of the figure.

Return null if input is even number or negative (as it is not possible to print
diamond with even number or negative number).

Python Note

Since print is a reserved word in Python, Python students must implement
the diamond(n) method instead, and return None for invalid input
'''
