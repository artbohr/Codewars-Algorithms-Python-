def unused_digits(*args):
    nums = ['0','1','2','3','4','5','6','7','8','9']

    for x in args:
        for i in list(str(x)):
            if i in nums:
                nums.remove(i)

    return ''.join(nums)

'''
Given few numbers, you need to print out the digits that are not being used.

Example:

unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"

Note:

    Result string should be sorted
    The test case won't pass Integer with leading zero
'''
