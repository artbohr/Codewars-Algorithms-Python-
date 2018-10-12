def close_to_zero(t):
    if not t: return 0

    plus = min([int(x) for x in t.split() if int(x)>-1])
    minus = max([int(x) for x in t.split() if int(x)<0])

    return minus if abs(minus) < plus else plus

'''
You were given a string of integer temperature values. Create a function
close_to_zero(t) and return the closest value to 0 or 0 if the string is empty.
If two numbers are equally close to zero, return the positive integer.
'''
