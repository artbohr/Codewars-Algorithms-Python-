'''
Your task is to make a function that can take any non-negative integer as a argument and return it with it's digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
'''

def descending_order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))

descending_order(1254859723)
# Returns: 9875543221
