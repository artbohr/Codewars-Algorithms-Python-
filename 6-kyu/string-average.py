from math import floor

def average_string(s):
    if not s: return "n/a"

    nums = {"one":1, "two":2, "three":3, "four":4, "five":5,
    "six":6, "seven":7, "eight":8, "nine":9, "zero":0}

    num_sum = 0
    s = s.split()

    for x in s:
        if x not in nums:
            return "n/a"
        else:
            num_sum += nums[x]

    res = floor(num_sum/len(s))

    for k, v in nums.items():
        if res == v:
            return k

    return "n/a"
