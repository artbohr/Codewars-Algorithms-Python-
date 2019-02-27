def filter_long_words(sentence, n):
    return [x for x in sentence.split() if len(x)>n]

'''
Write a function filter_long_words that takes a string sentence and an integer n.

Return a list of all words that are longer than n.

Example:

filter_long_words("The quick brown fox jumps over the lazy dog", 4)
 = ['quick', 'brown', 'jumps']

'''
