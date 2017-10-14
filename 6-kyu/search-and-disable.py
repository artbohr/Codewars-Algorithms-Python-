'''
100 ≤ log ≤ 100000
1 ≤ n ≤ 10000

Integer is Prime

Integer is 4 digits long such as 1031

Integer third digit is either 2 or 3 such as 1021 or 1031
                                               ^       ^
                                               |       |
The count of the integer in the log is > 3

If there are > 50 integers in the log matching this pattern the BOT at this location should be disabled

Here is an example

All the integers below are prime:

log= ['8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923', '5639', '2423', '3929', '7723',
      '8923']

Here is the Count

({'2423': 10, '3929': 10, '5639': 10, '7723': 10, '8923': 11})

Count = 51
Count > 50

Return "match disable bot"

If these rules do not hold

Return "no match continue"
'''

is_prime = lambda x: all(x % i != 0 for i in range(int(x ** 0.5) + 1)[2:])


def search_disable(log):
    log_split = log.split(' ')
    count = 0
    temp = ""
    banned = []

    if len(log_split) <= 50:
        return 'no match continue'

    for x in log_split:

        if x not in banned:
            banned.append(x)

            if is_prime(int(x)) and len(x) == 4 and log_split.count(x) > 3:

                if x.find('2', 2, 3) != -1 or x.find('3', 2, 3) != -1:

                    if temp != x:
                        count += log_split.count(x)
                        temp = x

        if count > 50:
            return 'match disable bot'

    return 'no match continue'


data = '8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923'

print(search_disable(data))
# Prints: match disable bot
