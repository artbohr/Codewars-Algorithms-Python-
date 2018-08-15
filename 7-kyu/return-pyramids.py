def pyramid(n):
    output = ''

    for x in reversed(range(n)):
        if x != 0:
            output += (x * ' ' + '/' + (((x+1) - n)*-1)*2 * ' ' + '\\' + '\n')
        else:
            output += (x * ' ' + '/' + (((x+1) - n)*-1)*2 * '_' + '\\' + '\n')

    return output

'''
The task is very simple.

You must to return pyramids. Given a number n you print a pyramid with n floors

For example , given a n=4 you must to print this pyramid:

   /\
  /  \
 /    \
/______\

Other example, given a n=6 you must to print this pyramid:

     /\
    /  \
   /    \
  /      \
 /        \
/__________\

Another example, given a n=10, you must to print this pyramid:

         /\
        /  \
       /    \
      /      \
     /        \
    /          \
   /            \
  /              \
 /                \
/__________________\

Note: an extra line feed character is needed at the end of the string.
Case n=0 should so return "\n".
'''
