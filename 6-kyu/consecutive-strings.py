def longest_consec(n, k):
    if len(n) < 1 or k > len(n) or k < 1: return ''

    d = {}

    for x in range(len(n)):
        if len(n[x:x+k]) == k:
            d[x] = sum([len(w) for w in n[x:x+k]])

    idx = max(d, key=d.get)

    return "".join(n[idx:idx+k])

'''
You are given an array strarr of strings and an integer k. Your task is to return
the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas",
"theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

'''
