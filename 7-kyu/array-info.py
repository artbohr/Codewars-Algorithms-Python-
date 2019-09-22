def array_info(x):
    if not x: return 'Nothing in the array!'
    ints,floats,strings,whites = [[0],[0],[0],[0]]
  
    for item in x:
        if isinstance(item, int): ints[0]+=1
        elif isinstance(item, float): floats[0]+=1
        elif item==' ': whites[0]+= 1
        elif isinstance(item, str): strings[0]+=1

    return [[len(x)],checker(ints),checker(floats),checker(strings),checker(whites)]
    
def checker(item):
    return item if item[0]>0 else [None]

'''
Brief

Sometimes we need information about the list/arrays we're dealing with. You'll have to write
 such a function in this kata. Your function must provide the following informations:

    Length of the array
    Number of integer items in the array
    Number of float items in the array
    Number of string character items in the array
    Number of whitespace items in the array

The informations will be supplied in arrays that are items of another array. Like below:

Output array = [[array length],[no of integer items],[no of float items],[no of string chars items],[no of whitespace items]]
Added Difficulty

If any item count in the array is zero, you'll have to replace it with a None/nil/null value (according to the language).
 And of course, if the array is empty then return 'Nothing in the array!. For the sake of simplicity, let's just suppose
that there are no nested structures.

Output

If you're head is spinning (just kidding!) then these examples will help you out-


array_info([1,2,3.33,4,5.01,'bass','kick',' '])--------->[[8],[3],[2],[2],[1]]    
array_info([0.001,2,' '])------------------------------>[[3],[1],[1],[None],[1]]   
array_info([])----------------------------------------->'Nothing in the array!'
array_info([' '])-------------------------------------->[[1],[None],[None],[None],[1]]

'''