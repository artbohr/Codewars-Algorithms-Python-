def solve(s):
    mx = ''
    temp = ''

    for x in s:
        if x in 'aeiou':
            temp+=x
        else:
            if len(temp) > len(mx):
                mx=temp
            temp=''

    return len(mx)

'''
The vowel substrings in the word codewarriors are o,e,a,io.
The longest of these has a length of 2. Given a lowercase
string that has alphabetic characters only and no spaces,
return the length of the longest vowel substring.
'''
