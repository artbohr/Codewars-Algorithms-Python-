def solve(st,a,b):
    return st.replace(st[a:b+1], st[a:b+1][::-1])

'''
In this Kata, you will be given a string and two indexes. Your task is to reverse
the portion of that string between those two indices inclusive.

solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.

Input will be lowercase and uppercase letters only.
'''
