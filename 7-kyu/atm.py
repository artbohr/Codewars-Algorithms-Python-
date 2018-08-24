def solve(n):
    output = 0

    for x in [500,200,100,50,20,10]:
        if n%10 != 0:
            return -1

        if n < x:
            continue

        output += (n//x)
        n = n%x

        if n == 0:
            return output

'''
There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of n with 1<=n<=1500.

Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.
'''
