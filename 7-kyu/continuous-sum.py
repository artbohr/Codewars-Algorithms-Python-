def add(l):
    if not isinstance(l,list): return 'Invalid input'

    for x in l:
        if type(x)!=int: return 'Invalid input'

    return [sum(l[:c+1]) for c,x in enumerate(l)]

'''
Make a function "add" that will be able to sum elements of list continuously and
 return a new list of sums. In python there can be cases where input is not a list,
 or there are other objects in it instead of integers like string characters or
 float numbers, in these cases return 'Invalid input'

For example:

add([1,2,3,4,5]) == [1, 3, 6, 10, 15] , because it's calculated like
 this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]

add([1,'a',2,'b',3,'c']) == 'Invalid input'

add('All string') == 'Invalid input'

add((1,2,3,4)) == 'Invalid input'

If you want to learn more see https://en.wikipedia.org/wiki/Prefix_sum

'''
