def convert_hash_to_array(hash):
    return sorted([[k,v] for k,v in hash.items()])

'''
Convert a hash into an array. Nothing more, Nothing less.

{name: 'Jeremy', age: 24, role: 'Software Engineer'}

should be converted into

[["name", "Jeremy"], ["age", 24], ["role", "Software Engineer"]]

Note: The output array should be sorted alphabetically.
'''
