def pattern(n):
    output = ''
    row = '{}{}'.format((n-1)*' ',''.join(str(l%10) for l in range(1,n+1)))
    for x in range(n):
        output+='{}{}{}'.format(row[x:],x*' ','\n')
    return output[:-1]

'''
###Task:

You have to write a function pattern which returns the following Pattern(See Examples)
 upto n rows, where n is parameter.

####Rules/Note:

    If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
    The length of each line = (2n-1).
    Range of n is (-∞,100]

###Examples:

pattern(5):

    12345
   12345 
  12345  
 12345   
12345    

pattern(10):

         1234567890
        1234567890 
       1234567890  
      1234567890   
     1234567890    
    1234567890     
   1234567890      
  1234567890       
 1234567890        
1234567890         
'''