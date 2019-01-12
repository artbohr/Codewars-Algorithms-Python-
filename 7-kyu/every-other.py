def double_every_other(lst):
    return [x if c%2==0 else x*2 for c,x in enumerate(lst)]

'''
Write a function, that doubles every second integer in a list starting from the left.
'''
