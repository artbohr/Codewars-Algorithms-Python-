def squares(x, n):
    last = x
    output = []
    for i in range(1,n+1):
        output.append(last)
        last = last**2
    return output

'''
Complete the function that returns an array of length n, starting with the given
 number x and the squares of the previous number. If n is negative or zero, return
 an empty array/list.
 
Examples

2, 5  -->  [2, 4, 16, 256, 65536]
3, 3  -->  [3, 9, 81]
'''