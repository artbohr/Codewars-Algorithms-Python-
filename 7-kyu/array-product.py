def product(numbers):
    if not numbers: return None
    output = 1

    for x in numbers:
        output*=x

    return output

'''
Calculate the product of all elements in an array.

If the array is empty or None, return None.

'''
