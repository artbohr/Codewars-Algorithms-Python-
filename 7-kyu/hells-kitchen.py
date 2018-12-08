def gordon(a):
    output = ''

    for x in a.upper():
        if x == 'A':
            output+='@'
        elif x in 'EIOU':
            output+='*'
        elif x == ' ':
            output+='!!!!{}'.format(x)
        else:
            output+=x

    return output + '!!!!'

'''
Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.

Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.

Rules:

Obviously the words should be Caps, Every word should end with '!!!!', Any letter 'a' or 'A'
 should become '@', Any other vowel should become '*'.
'''
