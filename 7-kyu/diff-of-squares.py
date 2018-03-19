'''
Find the difference between the sum of the squares of the first n natural numbers
(1 <= n <= 100) and the square of their sum.

For example, when n = 10:

    The square of the sum of the numbers is:

    (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)^2 = 55^2 = 3025

    The sum of the squares of the numbers is:

    1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 + 9^2 + 10^2 = 385

Hence the difference between square of the sum of the first ten natural numbers
and the sum of the squares of those numbes is: 3025 - 385 = 2640
'''

def difference_of_squares(n):
    sq_of_sum = 0
    sum_of_sqs = 0

    for x in range(1,n+1):
        sq_of_sum += x
        sum_of_sqs += x**2

    return sq_of_sum ** 2 - sum_of_sqs

difference_of_squares(5)
# Returns: 170
