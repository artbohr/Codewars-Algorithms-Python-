args_count = lambda *args, **kwargs: len(args) + len(kwargs)

'''
Create a function args_count, that returns the count of passed arguments

args_count(1, 2, 3) -> 3
args_count(1, 2, 3, 10) -> 4
'''
