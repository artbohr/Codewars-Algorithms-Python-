def kill_count(counselors, jason):
    return [x[0] for x in counselors if x[1] < jason]

'''
It's Friday the 13th, and Jason is ready for his first killing spree!

Create a function, killcount, that accepts two arguments: an array of array
 pairs (the conselor's name and intelligence - ["Chad", 2]) and an integer
 representing Jason's intellegence.

Ruby, Python, Crystal:

counselors = [["Chad", 2], ["Tommy", 9]]
jason = 7

'''
