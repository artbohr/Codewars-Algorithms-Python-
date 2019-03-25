def sort_transform(arr):
    f_part = "{}{}{}{}".format(chr(arr[0]),chr(arr[1]),chr(arr[-2]),chr(arr[-1]))
    arr2 = sorted(arr)
    s_part = "{}{}{}{}".format(chr(arr2[0]),chr(arr2[1]),chr(arr2[-2]),chr(arr2[-1]))

    return '{}-{}-{}-{}'.format(f_part, s_part,''.join(sorted(s_part,reverse=True)), s_part)

'''
Given an array of numbers, return a string made up of four parts:

a) a four character 'word', made up of the characters derived from the first two
 and last two numbers in the array. order should be as read left to right
 (first, second, second last, last),

b) the same as above, post sorting the array into ascending order,

c) the same as above, post sorting the array into descending order,

d) the same as above, post converting the array into ASCII characters
 and sorting alphabetically.

The four parts should form a single string, each part separated by a hyphen: '-'

example format of solution: 'asdf-tyui-ujng-wedg'

'''
