def my_languages(results):
    output = {}

    for i,v in results.items():
        if v>=60:
            output[i] = v

    return sorted(output, key=output.__getitem__, reverse=True)

'''
Your task

Given a dictionary/hash/object of languages and your respective test results,
return the list of languages where your test score is at least 60,
in descending order of the results.

Note: There will be no duplicate values.
Examples

{"Java": 10, "Ruby": 80, "Python": 65}  --> ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71} --> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}   --> []
'''
