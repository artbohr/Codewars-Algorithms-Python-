def tickets(people):
    register = {100: 0, 50: 0, 25: 0}

    for x in people:
        change = x - 25
        while change != 0:
            if change >= 100 and register[100] > 0:
                register[100] -= 1
                change -= 100
            elif change >= 50 and register[50] > 0:
                register[50] -= 1
                change -= 50
            elif change >= 25 and register[25] > 0:
                register[25] -= 1
                change -= 25
            else:
                return 'NO'
        register[x] += 1
    return 'YES'

'''
The new "Avengers" movie has just been released! There are a lot of people at the
cinema box office standing in a huge line. Each of them has a single 100, 50 or 25
dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every
single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no
money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the
bills he has at hand at that moment. Otherwise return NO.

###Examples:

tickets([25, 25, 50]) # => YES
tickets([25, 100])
         # => NO. Vasya will not have enough money to give change to 100 dollars
'''
