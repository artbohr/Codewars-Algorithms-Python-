def dollar_to_speech(value):
    if value[1]=='-': return 'No negative numbers are allowed!'

    dot = value.index('.')
    dollars = int(value[1:dot])
    cents = int(value[dot+1:])
    end_d = '' if dollars == 1 else 's'
    end_c = '' if cents == 1 else 's'

    if dollars and cents:
        return '{} dollar{} and {} cent{}.'.format(str(dollars),end_d,str(cents),end_c)
    elif dollars and not cents:
        return '{} dollar{}.'.format(str(dollars),end_d)
    elif cents and not dollars:
        return '{} cent{}.'.format(str(cents),end_c)
    else:
        return '0 dollars.'

'''
You start with a value in dollar form, e.g. $5.00. You must convert this value to
 a string in which the value is said, like '5 dollars' for example. This should
 account for ones, cents, zeroes, and negative values. Here are some examples:

dollar_to_speech('$0.00') == '0 dollars.'
dollar_to_speech('$1.00') == '1 dollar.'
dollar_to_speech('$0.01') == '1 cent.'
dollar_to_speech('$5.00') == '5 dollars.'
dollar_to_speech('$20.18') == '20 dollars and 18 cents.'
dollar_to_speech('$-1.00') == 'No negative numbers are allowed!'

These examples account for pretty much everything. This kata has many specific outputs, so good luck!

'''
