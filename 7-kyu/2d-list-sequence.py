def make_2d_list(head,row,col):
    output, temp = [], []
    head -= 1

    for x in range(row):
        for i in range(col):
            head += 1
            temp.append(head)
        output.append(temp)
        temp = []

    return output

'''
Make the 2D list by the sequential integers started by the head number.

See the example test cases for the expected output.

Note:

-10**20 < the head number <10**20
1 <=  the number of rows <= 1000
0 <=  the number of columms <= 1000

'''
