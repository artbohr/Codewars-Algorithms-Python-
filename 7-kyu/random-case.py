'''
Write a function that will randomly upper and lower characters in a string

randomCase("Donec eleifend cursus lobortis") == "DONeC ElEifEnD CuRsuS LoBoRTIs"
'''

import random

def random_case(x):
    output = ""

    for letter in x:
        if random.random() > 0.5:
            output += letter.lower()
            continue
        output += letter.upper()

    return output
