def move_ten(st):
    return ''.join([chr(ord(x)+10) if ord(x)<=112 else chr(ord(x)-16) for x in st])

'''
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.

'''
