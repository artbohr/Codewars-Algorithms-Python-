def arrange(arr):
    output = []

    for x in arr:
        if 'T' in x:
            output.append((int(x[:-1]) * 1000 ,x))
        elif 'K' in x:
            output.append((int(x[:-2]) ,x))
        else:
            output.append((int(x[:-1]) / 1000 ,x))

    return [x[1] for x in sorted(output)]

'''
Given an array of strings, sort the array into order of weight from light to heavy.

Weight units are grams(G), kilo-grams(KG) and tonnes(T).

Arrays will always contain correct and positive values aswell as uppercase letters.
'''
