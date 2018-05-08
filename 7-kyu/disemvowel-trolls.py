def disemvowel(string):
    return ''.join(i for i in string if i not in 'aeiouAEIOU')

'''
Write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
'''
