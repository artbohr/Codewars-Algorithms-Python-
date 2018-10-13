def box(n):
    output = ['-' * n]

    for x in range(n-2):
        output.append('-' + ' ' * (n-2) + '-')

    return output + ['-' * n]

'''
Easy; Make a box
Given a number as a parameter, return an array containing strings which form a box.

Like this:

n = 5

[
  '-----',
  '-   -',
  '-   -',
  '-   -',
  '-----'
]

n = 3

[
  '---',
  '- -',
  '---'
]

'''
