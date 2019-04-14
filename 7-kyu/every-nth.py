def every(array, interval=1, start_index=0):
    return [array[x] for x in range(start_index,len(array),interval)]

'''
Create a method (JS: function) every which returns every nth element of an array.
Usage

With no arguments, array.every it returns every element of the array.
With one argument, array.every(interval) it returns every intervalth element.
With two arguments, array.every(interval, start_index) it returns every
 intervalth element starting at index start_index

Examples

[0,1,2,3,4].every      # [0,1,2,3,4]
[0,1,2,3,4].every(1)   # [0,1,2,3,4]
[0,1,2,3,4].every(2)   # [0,2,4]
[0,1,2,3,4].every(3)   # [0,3]
[0,1,2,3,4].every(1,3) # [3,4]
[0,1,2,3,4].every(3,1) # [1,4]
[0,1,2,3,4].every(3,4) # [4]
'''
