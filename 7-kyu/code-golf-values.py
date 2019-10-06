make_new_list=lambda l:[l[x]+l[x+1] for x in range(len(l)-1)]

'''
You get a list of integers. Return a new list by adding 2 elements
 surrounding each comma in the list.
Examples

If you get [1, 1, 1, 1], return [2, 2, 2] because [1+1, 1+1, 1+1]
If you get [1, 2, 3, 4], return [3, 5, 7] because [1+2, 2+3, 3+4]
If you get [1, 10, 100], return [11, 110] because [1+10, 10+100]

Restriction

Your code length should not be longer than 60 characters.
'''