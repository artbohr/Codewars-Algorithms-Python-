def fruit(reels, spins):
    scoring_table = {"Wild": 10,"Star": 9,"Bell": 8,"Shell": 7,
    "Seven":6,"Cherry":5,"Bar":4,"King":3,"Queen":2,"Jack":1}

    result = [reel[spins[i]] for i, reel in enumerate(reels)]
    counted = False
    output = 0
    bonus = 1

    for x in result:
        if result.count(x) == 3:
            return scoring_table[x] * 10
        if result.count(x) == 2 and not counted:
            output = scoring_table[x]
            counted = True
        if x == 'Wild' and result.count('Wild') == 1:
            bonus = 2

    return output * bonus
    
'''
Task
  	You will be given three reels of different images and told at which index the reels stop. From this information your job is to return the score of the resulted reels.
Rules
  	1. There are always exactly three reels
2. Each reel has 10 different items.
3. The three reel inputs may be different.
4. The spin array represents the index of where the reels finish.
5. The three spin inputs may be different
6. Three of the same is worth more than two of the same
7. Two of the same plus one "Wild" is double the score.
8. No matching items returns 0.

Returns
  	Return an integer of the score.

Example:

reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [5,5,5]
result = fruit([reel1,reel2,reel3],spin)

Scoring

reel1[5] == "Cherry"
reel2[5] == "Cherry"
reel3[5] == "Cherry"

Cherry + Cherry + Cherry == 50

Return

result == 50

To see the scoring table: https://www.codewars.com/kata/fruit-machine/python

'''
