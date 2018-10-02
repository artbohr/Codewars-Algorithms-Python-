def bubble(l):
    output = []
    new_l = l

    for x in range(len(l)):
        for c in range(len(new_l) - x):
            if c != len(new_l)-1 and new_l[c] > new_l[c+1]:
                new_l[c], new_l[c+1] = new_l[c+1], new_l[c]
                output.append(new_l[:])
    return output

'''
#Bubbleing around

Since everybody hates chaos and loves sorted lists we should implement
some more sorting algorithms. Your task is to implement a Bubble sort
(for some help look at https://en.wikipedia.org/wiki/Bubble_sort) and
return a list of snapshots after each change of the initial list.

e.g.

If the initial list would be l=[1,2,4,3] my algorithm rotates l[2] and l[3]
and after that it adds [1,2,3,4] to the result, which is a list of snapshots.

[1,2,4,3] should return [ [1,2,3,4] ]
[2,1,4,3] should return [ [1,2,4,3], [1,2,3,4] ]
[1,2,3,4] should return []

'''
