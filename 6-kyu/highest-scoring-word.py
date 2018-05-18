def high(str):
    leader, current = 0, 0

    for word in str.split():
        for letter in word:
            current += ord(letter)-96
        if current > leader:
            leader = current
            output = word
        current = 0

    return output

'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the

alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''
