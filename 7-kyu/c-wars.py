def initials(name):
    a = name.split(' ')
    return '{}.{}'.format('.'.join([x[0].upper() for x in a[:-1]]), a[-1].capitalize())

'''
Normally we have firstname,middle and the last name but there may be more than
one word in a name . Like a South indian one .

Similar to those kinda names we need to initiallize the names .

See the pattern Below

initials('code wars') => returns C.Wars
initials('Barack Hussain obama') => returns B.H.Obama

Complete the function initials.
'''
