'''
In this Kata, you will be given a string that has lowercase letters and numbers.
Your task is to compare the number groupings and return the largest number.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.
'''

def solve(s):
    nums = []
    temp = ''

    for x in range(len(s)):
        if s[x].isdigit():
            temp+=s[x]
            if x==len(s)-1 and temp != '':
                nums.append(int(temp))

        elif not s[x].isdigit() and temp != '':
            nums.append(int(temp))
            temp = ''

    return max(nums)

solve("gh12cdy691312322asd913123651#231231235m1")
#Returns: 913123651
