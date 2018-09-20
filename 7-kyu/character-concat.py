def char_concat(word):
    output = ''
    r_word = word[::-1][:len(word) // 2]

    for x in range(len(r_word)):
        output += '{}{}{}'.format(word[x], r_word[x], str(x+1))

    return output

'''
Given a string, you progressively need to concatenate the first letter from the
left and the first letter to the right and "1", then the second letter from the
left and the second letter to the right and "2", and so on.

If the string's length is odd drop the central element.

For example:

char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
'''
