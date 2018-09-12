def parse(data):
    num = 0
    output = []

    for x in data:
        if x=='s':
            num = num ** 2
        elif x=='i':
            num += 1
        elif x=='d':
            num -= 1
        elif x=='o':
            output.append(num)

    return output

'''
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array

Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]

'''
