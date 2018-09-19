def chessboard(s):
    s = s.split()
    di = int(s[1])//2
    output = ''

    for x in range(int(s[0])):
        if x%2 == 0:
            output += '*.' * di if int(s[1])%2 == 0 else '*.' * di + '*'
        else:
            output += '.*' * di  + '.' if int(s[1])%2 != 0 else '.*' * di

        output += '\n'

    return output[:-1]

'''
Write a program that prints a chessboard with N rows and M columns with the following rules:
The top left cell must be an asterisk (*) Any cell touching (left, right, up or down)
a cell with an asterisk must be a dot (.) Any cell touching (left, right, up or down)
a cell with a dot must be an asterisk.

A chessboard of 8 rows and 8 columns printed using these rules would be:

*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*

Input

A single line with two integers N and M separated by space. The number N will
represent the number of rows and M the number of columns.

Output

Return N lines each containing M characters with the chessboard pattern.
Empty string if N, M or both are 0.

From: 2016 AIPO National Finals http://aipo.computing.dcu.ie/2016-aipo-national-finals-problems

'''
