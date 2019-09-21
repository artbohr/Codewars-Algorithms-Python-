def determineTime(arr):
    hours = 0
    
    for time in arr:
        sp = time.split(':')
        hours += sum([int(sp[0]),int(sp[1])/60,int(sp[2])/3600])
        
    return hours < 24

'''
Can Santa save Christmas?
Oh no! Santa's little elves are sick this year. He has to distribute the
 presents on his own.
 
But he has only 24 hours left. Can he do it?

Your job is to determine if Santa can distribute all the presents in 24 hours.
Your Task:

You will get an array as input with time durations as string in the following format:
"hh:mm:ss"

Each duration is a present Santa has to distribute.

Return true or false whether he can do it in 24 hours or not. 
'''