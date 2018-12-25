def capitals_first(text):
    upper,lower = [], []

    for x in text.split():
        if x[0].upper() == x[0] and x[0].isalpha():
            upper.append(x)
        elif x[0].lower() == x[0] and x[0].isalpha():
            lower.append(x)

    return ' '.join(upper+lower)
    
'''
Create a function that takes an input String and returns a String, where all the
 uppercase words of the input String are in front and all the lowercase words at the end.
 The order of the uppercase and lowercase words should be the order in which they occur.

If a word starts with a number or special character, skip the word and leave it out of the result.

Input String will not be empty.

For an input String: "hey You, Sort me Already!" the function should return: "You, Sort Already! hey me"

'''
