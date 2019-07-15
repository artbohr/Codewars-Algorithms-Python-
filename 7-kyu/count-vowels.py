def count_vowels(s = ''):
    try:
        return len([x for x in s.lower() if x in 'aeiou'])
    except AttributeError:
        return None

'''
Write a function count_vowels to count the number of vowels in a given string.
Notes:

    Return nil or None for non-string inputs.
    Return 0 if the parameter is omitted.

Examples:

count_vowels("abcdefg") => 2
count_vowels("aAbcdeEfg") => 4

count_vowels(12) => None


'''
