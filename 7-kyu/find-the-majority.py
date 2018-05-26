def majority(arr):
    cn = sorted((arr.count(x), x) for x in set(arr))

    if len(cn) == 1:
        return cn[-1][1]

    return cn[-1][1] if len(cn) > 1 and cn[-1][0] != cn[-2][0] else None

'''
Goal
Given a list of elements [a1, a2, ..., an], with each ai being a string,
write a function majority that returns the value that appears the most in the list.

If there's no winner, the function should return None.

Example
majority(["A", "B", "A"]) returns "A" majority(["A", "B", "B", "A"]) returns None
'''
