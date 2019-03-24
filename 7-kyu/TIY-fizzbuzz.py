def tiy_fizz_buzz(string):
    return ''.join(manage_letter(x) for x in string)

def manage_letter(letter):
    if letter in 'aeiouAEIOU':
        if letter.upper() == letter:
            return 'Iron Yard'
        else:
            return 'Yard'
    else:
        if letter.upper() == letter and letter.isalpha():
            return 'Iron'
        else:
            return letter

'''
In this exercise, you will have to create a function named tiyFizzBuzz.
 This function will take on a string parameter and will return that string
 with some characters replaced, depending on the value:

    If a letter is a upper case consonants, replace that character with "Iron".
    If a letter is a lower case consonants or a non-alpha character,
     do nothing to that character
    If a letter is a upper case vowel, replace that character with "Iron Yard".
    If a letter is a lower case vowel, replace that character with "Yard".

'''
