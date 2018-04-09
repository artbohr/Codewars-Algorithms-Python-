def check_three_and_two(array):
    return [2,3] == sorted([array.count(x) for x in set(array)])

'''
Given an array with 5 string values "a", "b" or "c", check if
the array contains three and two of the same values.

Examples

["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"
'''
