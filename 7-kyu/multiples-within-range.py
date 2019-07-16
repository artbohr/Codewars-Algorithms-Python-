def multiples(s1,s2,s3):
    return [x for x in range(s1, s3-1) if x%s1==0 and x%s2==0]

'''
Print all numbers up to 3rd parameter which are multiple
 of both 1st and 2nd parameter.

Python, Javascript, Java versions: return results in a list/array

NOTICE:

    Do NOT worry about checking zeros or negative values.
    To find out if 3rd parameter (the upper limit) is inclusive or not,
     check the tests, it differs in each translation

'''
