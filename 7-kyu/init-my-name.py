'''
Some people just have a first name; some people have first and last names
 and some people have first, middle and last names.
You task is to initialize the middle names (if there is any)
'''

def initialize_names(name):
    output = ""
    n_list = name.split(" ")

    for x in n_list:
        if x == n_list[0] and x != n_list[len(n_list)-1]:
            output += '{} '.format(x)
        elif x == n_list[len(n_list)-1]:
            output += x
        else:
            output += '{}. '.format(x[0])

    return output

initialize_names('Lois Mary Lane')
# Returns: 'Lois M. Lane'
