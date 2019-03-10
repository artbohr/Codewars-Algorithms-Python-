def alex_mistakes(number_of_katas, time_limit):
    req_time = 5
    sets = 0
    remaining = time_limit - number_of_katas * 6

    while remaining>=req_time:
        remaining-=req_time
        req_time*=2
        sets+=1

    return sets

'''
Alex is transitioning from website design to coding and wants to sharpen his
 skills with CodeWars. He can do ten kata in an hour, but when he makes a mistake,
 he must do pushups. These pushups really tire poor Alex out, so every time he does
 them they take twice as long. His first set of redemption pushups takes 5 minutes.
 Create a function, alexMistakes, that takes two arguments: the number of kata he
 needs to complete, and the time in minutes he has to complete them.
 
 Your function should return how many mistakes Alex can afford to make.
'''
