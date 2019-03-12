def remove_duplicate_words(s):
    output = ""
    for x in s.split():
        if x not in output:
            output+= "{} ".format(x)

    return output[:-1]

'''
Your task is to remove all duplicate words from string, leaving only single
 (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'

'''
