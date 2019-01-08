def swap(st):
    output = ''

    for x in st:
        if x in 'aeiou':
            output+=x.upper()
        else:
            output+=x

    return output

'''
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

'''
