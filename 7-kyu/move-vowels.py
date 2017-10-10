'''
Given a string as input, move all of its vowel to the end of the string.

Example input: day Example output: dya

Example input: apple Example output: pplae

Note: All input string are of small letters, and the order of the vowels at the end should be the same as they were before.

'''

def move_vowels(word):
    vowels = ['a','e','i','o','u']
    result = ''
    append_end = ''

    for x in range(len(word)):
        if word[x] in vowels:
            append_end  += word[x]
        else:
            result+=word[x]

    return result + append_end

print(move_vowels('day'))
# Prints: dya
