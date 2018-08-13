def check_concatenated_sum(n, t):
    if t == 0: return False

    minus = True if str(n)[0] == '-' else False
    n_s = str(n)[1:] if minus else str(n)
    arr_s = []

    for x in n_s:
        if minus:
            arr_s.append('-' + (x * t))
        else:
            arr_s.append(x * t)

    res = sum([int(x) for x in arr_s])

    return n == res

'''
The number 198 has the property that 198 = 11 + 99 + 88, i.e.,
if each of its digits is concatenated twice and then summed,
the result will be the original number. It turns out that 198
is the only number with this property. However, the property can
be generalized so that each digit is concatenated n times and then summed.

eg:-

original number =2997 , n=3
2997 = 222+999+999+777 and here each digit is concatenated three times.

original number=-2997 , n=3

-2997 = -222-999-999-777 and here each digit is concatenated three times.

Write afunction named check_concatenated_sum that tests if a number has this
generalized property.
'''
