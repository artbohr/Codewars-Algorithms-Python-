from string import ascii_lowercase as alphabet

def add_letters(*letters):
    return alphabet[sum(alphabet.index(x)+1 for x in letters)%26 - 1]

'''
Your task is to add up letters to one letter.

The function will be given a variable amount of arguments,
 each one being a letter to add.
 
Notes:

    Letters will always be lowercase.
    Letters can overflow (see second to last example of the description)
    No letters should return 'z'

Examples:

add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
'''