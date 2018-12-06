def sort_by_height(a):
    indices = [c for c,x in enumerate(a) if x==-1]
    output = sorted(a)[len(indices):]
    for x in indices:
        output.insert(x, -1)
    return output

'''
Task

Some people are standing in a row in a park. There are trees between
 them which cannot be moved.

Your task is to rearrange the people by their heights in a
 non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be

[-1, 150, 160, 170, -1, -1, 180, 190].
Input/Output

    [input] integer array a

    If a[i] = -1, then the ith position is occupied by a tree.
    Otherwise a[i] is the height of a person standing in the ith position.

    Constraints:

    5 ≤ a.length ≤ 30,

    -1 ≤ a[i] ≤ 200.

    [output] an integer array

    Sorted array a with all the trees untouched.

'''
