'''
When Sigma1 Function Has Equals Values For an Integer and Its Reversed One
***

Description is too large, read the description here:
https://www.codewars.com/kata/when-sigma1-function-has-equals-values-for-an-integer-and-its-reversed-one/train/python
'''

def equal_sigma1(nMax):
    verified = {}
    r = []
    r2 = []
    final = 0

    for i in range(1, nMax+1):
        if str(i) ==str(i)[::-1]:
            continue
        new_i = int(i**0.5)
        new_i_rev = int(int(str(i)[::-1])**0.5)

        for x in range(1, new_i+1):
            if i % x == 0:
                r.append(x)
                if x*x != i:
                    r.append(i/x)

        for x in range(1, new_i_rev):
            if int(str(i)[::-1]) % x == 0:
                r2.append(x)
                if x*x != int(str(i)[::-1]):
                    r2.append(int(str(i)[::-1])/x)

        if sum(r) == sum(r2):
            verified.update({i:sum(r)})
            verified.update({int(str(i)[::-1]):sum(r2)})

        r = []
        r2 = []

    for key in verified:
        if key<=nMax:
            final+= key

    return final

equal_sigma1(1600)
# Returns: 2914
