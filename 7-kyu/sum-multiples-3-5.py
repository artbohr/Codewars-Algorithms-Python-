def find(n):
    return sum(x for x in range(3,n+1) if x%3==0 or x%5==0)

'''
Your task is to write function findSum.

Upto and including n, this function will return the sum
 of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)

'''
