def passer_rating(att, yds, comp, td, ints):
    A = ((comp / att) - .3) * 5
    B = ((yds / att) - 3) * .25
    C = (td / att) * 20
    D = 2.375 - ((ints / att) * 25)

    arr = [x for x in (A,B,C,D) if x > 0]
    return round(sum([x if x < 2.375 else 2.375 for x in arr])/6 * 100, 1)

'''
Passer ratings are the generally accepted standard for evaluating NFL quarterbacks.
I knew a rating of 100 is pretty good, but never knew what makes up the rating.
So out of curiosity I took a look at the wikipedia page
and had an idea or my first kata: https://en.wikipedia.org/wiki/Passer_rating

Formula

There are four parts to the NFL formula:

A = ((Completions / Attempts) - .3) * 5
B = ((Yards / Attempts) - 3) * .25
C = (Touchdowns / Attempt) * 20
D = 2.375 - ((Interceptions / Attempts) * 25)

However, if the result of any calculation is greater than 2.375, it is set to 2.375.
If the result is a negative number, it is set to zero.

Finally the passer rating is: ((A + B + C + D) / 6) * 100

Return the rating rounded to the nearest tenth.
Example

Last year Tom Brady had 432 attempts, 3554 yards, 291 completions,
28 touchdowns, and 2 interceptions. His passer rating was 112.2

Happy coding!

'''
