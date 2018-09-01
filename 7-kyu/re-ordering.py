def re_ordering(text):
    output = text.split()

    for x in text.split():
        if x[0].isupper():
            output.remove(x)
            output.insert(0, x)

    return " ".join(output)

'''
There is a sentence which has a mistake in it's ordering.

The part with a capital letter should be the first word.

Please build a function for re-ordering
Examples

>>> re_ordering('ming Yao')
'Yao ming'

>>> re_ordering('Mano donowana')
'Mano donowana'

>>> re_ordering('wario LoBan hello')
'LoBan wario hello'

>>> re_ordering('bull color pig Patrick')
'Patrick bull color pig'
'''
