def ordered_count(input):
    return [(x,input.count(x))for i,x in enumerate(input) if x not in input[:i]]

'''
Count the number of occurrences of each character and return it as a list of
 tuples in order of appearance.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

'''
