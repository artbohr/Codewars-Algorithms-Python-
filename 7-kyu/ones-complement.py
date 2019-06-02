def ones_complement(binary_number):
    return binary_number.replace("1","x").replace("0","1").replace("x","0")

'''
The Ones' Complement of a binary number is the number obtained by swapping all
 the 0s for 1s and all the 1s for 0s. For example:

onesComplement(1001) = 0110
onesComplement(1001) = 0110

For any given binary number,formatted as a string, return the Ones' Complement
 of that number.
'''
