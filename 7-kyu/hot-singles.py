def hot_singles(arr1, arr2):
    output = []

    for x in arr1:
        if x not in output and x not in arr2:
            output.append(x)

    for x in arr2:
        if x not in output and x not in arr1:
            output.append(x)

    return output

'''
Write a function that takes two arguments, and returns a new array populated
with the elements that only appear once, in either one array or the other,
taken only once; display order should follow what appears in arr1 first, then arr2:

hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5]) # [4, 5]
hot_singles(["tartar", "blanket", "cinnamon"], ["cinnamon", "blanket", "domino"]) # ["tartar", "domino"]
hot_singles([77, "ciao"], [78, 42, "ciao"]) # [77, 78, 42]
hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5, 4]) # [4,5]
'''
