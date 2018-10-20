def mutate_my_strings(s1,s2):
    output = s1 + '\n'

    for x in range(len(s1)):
        if s1[x] == s2[x]:
            continue
        output+= '{}\n'.format(s2[:x+1] + s1[x+1:])

    return output

'''
I will give you two strings. I want you to transform stringOne
into stringTwo one letter at a time.

Example:

stringOne = 'bubble gum';
stringTwo = 'turtle ham';

Result:
bubble gum
tubble gum
turble gum
turtle gum
turtle hum
turtle ham
'''
