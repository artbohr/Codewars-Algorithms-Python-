def game(a, b):
    if not a or not b: return "Non-drinkers can't play"
    mike, joe = a, b
    switch_turn = False

    for x in range(1, max(a,b)+2):
        if not switch_turn:
            mike -= x
            switch_turn = True
        else:
            joe -= x
            switch_turn = False
        if mike < 0:
            return "Joe"
        if joe < 0:
            return "Mike"

'''
Mike and Joe are fratboys that love beer and games that involve drinking.
They play the following game: Mike chugs one beer, then Joe chugs 2 beers,
then Mike chugs 3 beers, then Joe chugs 4 beers, and so on. Once someone
can't drink what he is supposed to drink, he loses.

Mike can chug at most A beers in total (otherwise he would pass out),
while Joe can chug at most B beers in total. Who will win the game?

Write the function game(A,B) that returns the winner, "Mike" or "Joe"
accordingly, for any given integer values of A and B.

Note: If either Mike or Joe cannot drink at least 1 beer,
return the string "Non-drinkers can't play".

'''
