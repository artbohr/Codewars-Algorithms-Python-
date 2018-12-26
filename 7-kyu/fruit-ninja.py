def cut_fruits(fruits):
    output = []

    for x in fruits:
        if x in FRUIT_NAMES:
            di = (len(x)+1)//2
            output.append(x[:di])
            output.append(x[di:])
        else:
            output.append(x)

    return output


'''
Description

You are a Fruit Ninja, your skill is cutting fruit. All the fruit will be
 cut in half by your knife. For example:

[  "apple",     "pear",     "banana"  ]  -->
["app", "le", "pe", "ar", "ban", "ana"]

As you see, all fruits are cut in half. You should pay attention to "apple":
 if you cannot cut a fruit into equal parts, then the first part will have
 an extra character.

You should only cut fruit, other things should not be cut, such as "bomb":

[  "apple",     "pear",     "banana",   "bomb"]  -->
["app", "le", "pe", "ar", "ban", "ana", "bomb"]

The valid fruit names are preloded for you as:

FRUIT_NAMES

Task

Complete function cut_fruits that accepts argument fruits.
 Returns the result in accordance with the rules above.

OK, that's all. I guess this is a 7kyu kata. If you agree, please rank
 it as 7kyu and vote very;-) If you think this kata is too easy or too hard,
 please shame me by rank it as you want and vote somewhat or none :[

 https://www.codewars.com/kata/i-guess-this-is-a-7kyu-kata-number-6-fruit-ninja-i/python
'''
