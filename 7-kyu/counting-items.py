def count(array):
    return {item:array.count(item) for item in array}

'''
Write a function that takes an array and counts the number of each unique element present.

count(['james', 'james', 'john'])
#=> { 'james' => 2, 'john' => 1}

'''
