'''
Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
'''

def reverse_words(str):
    for word in str.split():
        str = str.replace(word, word[::-1])
    return str
  
print(reverse_words("An example!"))
# Outputs: "nA !elpmaxe"
