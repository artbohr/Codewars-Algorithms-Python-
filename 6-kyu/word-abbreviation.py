'''
The word i18n is a common abbreviation of internationalization the developer
community use instead of typing the whole word and trying to spell it correctly.
Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below)
within that string of length 4 or greater into an abbreviation following the same rules.

Notes:
    A "word" is a sequence of alphabetical characters. By this definition, any other
    character like a space or hyphen (eg. "elephant-ride") will split up a series
    of letters into two words (eg. "elephant" and "ride").
    The abbreviated version of the word should have the first letter, the the number
    of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").
'''
import re


def abbreviate(s):
    final = ''
    words = re.findall('[a-zA-Z]+', s)
    symbols = re.findall('[^a-zA-Z]+', s)

    for i in range(len(words)):
        if len(words[i]) < 4:
            final += words[i]
            if symbols:
                final += symbols[i]
        else:
            final += (words[i][0] + str(len(words[i]) - 2) + words[i][-1])
            if symbols:
                final += symbols[i]
    return final

abbreviate("elephant-rides are really fun!")
#Returns: e6t-r3s are r4y fun!
