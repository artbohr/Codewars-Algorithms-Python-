def seqlist(first,c,l):
    output = [first]

    for x in range(l-1):
       output.append(first+c)
       first += c
    return output

'''
In this kata, you will write an arithmetic list which is basically a list that
contains consecutive terms in the sequence.

You will be given three parameters :

    first the first term in the sequence
    c the constant that you are going to ADD ( since it is an arithmetic sequence...)
    l the number of terms that should be returned
'''
