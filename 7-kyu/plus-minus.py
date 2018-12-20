def catch_sign_change(lst):
    if not lst: return 0

    total = -1
    state = ''

    for x in lst:
        if x > -1 and state != 'p':
            total+=1
            state = 'p'
        elif x < 0 and state != 'n':
            total+=1
            state = 'n'

    return total

'''
Count how often sign changes in array.
result

number from 0 to ... . Empty array returns 0
example

const arr = [1, -3, -4, 0, 5]

| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |

return 2;
'''
