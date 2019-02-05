def am_I_afraid(day,num):
    ff = {
    'Monday': lambda x:x==12,
    'Tuesday':lambda x:x> 95,
    'Wednesday': lambda x:x==34,
    'Thursday': lambda x:x==0,
    'Friday': lambda x:x%2==0,
    'Saturday': lambda x:x==56,
    'Sunday': lambda x: abs(x)==666
    }

    return ff.get(day)(num)

'''
I've got a crazy mental illness. I dislike numbers a lot. But it's a little
 complicated: The number I'm feared of depends on which day of week it is...
 This a concrete description of my mental illness:

Monday --> 12

Tuesday --> numbers greater than 95

Wednesday --> 34

Thursday --> 0

Friday --> numbers divisable by 2

Saturday --> 56

Sunday --> 666 or -666

Write a function which takes a string (day of week) and an integer
 (number to be tested) so it tells the doctor if I'm feared or not. (return a boolean)
'''
