def get_a_down_arrow_of(n):
    output = ''

    for x in range(n,0,-1):
        output += ' '*((x-n)*-1)
        for i in range(1,x):
            output += str(i%10)
        for k in range(x,0,-1):
            output += str(k%10)
        output += '\n'
    return output[:-1]

'''
Given a number n, make a down arrow shaped pattern.

For example, when n = 5, the output would be:

123454321
 1234321
  12321
   121
    1

and for n = 11, it would be:

123456789010987654321
 1234567890987654321
  12345678987654321
   123456787654321
    1234567654321
     12345654321
      123454321
       1234321
        12321
         121
          1

An important thing to note in the above example is that the numbers greater
than 9 still stay single digit, like after 9 it would be 0 - 9 again
instead of 10 - 19
'''
