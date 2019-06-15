def decrypt(encrypted_text, n):
    if n < 1: return encrypted_text
    output = ""
    mid = len(encrypted_text)//2
    e_text = encrypted_text

    for x in range(n):
        for i in range(mid):
            output += e_text[mid+i]
            output += e_text[i]
        e_text = output
        if n-1!=x:
            output = ""
        elif x==n-1 and len(encrypted_text)%2!=0:
            output+=encrypted_text[-1]

    return output


def encrypt(text, n):
    ev_s, rest = '', ''
    output = text

    for x in range(n):
        for i, letter in enumerate(output):
            if i%2!=0:
                ev_s+=letter
            else:
                rest+=letter
        output = ev_s + rest
        ev_s, rest = '', ''

    return output

'''
For building the encrypted string:
Take every 2nd char from the string, then the other chars,
 that are not every 2nd char, and concat them as new String.

Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
'''
