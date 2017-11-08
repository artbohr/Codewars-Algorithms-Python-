'''
The autocomplete function will take in an input string and a dictionary array and
return the values from the dictionary that start with the input string. If
there are more than 5 matches, restrict your output to the first 5 results.
If there are no matches, return an empty array.

For this kata, the dictionary will always be a valid array of strings.
Please return all results in the order given in the dictionary, even if
they're not always alphabetical. The search should NOT be case sensitive,
but the case of the word should be preserved when it's returned.

For example, "Apple" and "airport" would both return for an input of 'a'.
However, they should return as "Apple" and "airport" in their original cases.
'''

import re

def autocomplete(input_, dictionary):
    final = []
    clean_s = "".join(re.findall('[a-zA-Z]', input_))

    for word in dictionary:
        if len(final) == 5:
            break
        if clean_s[:len(clean_s)] == word[:len(clean_s)].lower():
            final.append(word)
    return final


dictionary = ['airplane', 'apple', 'air', 'avenue', 'airport', 'adamantium',
'awkwardness', 'awesome', 'amazing', 'ball', 'book', 'bike', 'bill', 'billiard',
'bell', 'bowl', 'Blastoise', 'beautiful', 'car', 'cookie', 'coup', 'candle',
'change', 'champion', 'call', 'camel', 'Charizard', 'catastrophic', 'cat',
'keepsake', 'kick', 'kicker', 'knot', 'kit', 'kitten', 'lamp', 'light', 'lol', 'llama',
'lake', 'love', 'link', 'league', 'legend', 'laboratory', 'lab', 'more', 'morbid',
'move', 'mover', 'movie', 'monocle', 'murica', 'molar', 'mouth', 'muscle', 'montage',
'nope', 'no', 'naughty', 'nice', 'nail polish', 'noodles', 'niece', 'nissan', 'octopus',
'under', 'undercover', 'united', 'unbelievable', 'unimaginable', 'ultra', 'ultraviolet',
'victory', 'violin', 'viola', 'vibrant', 'video playback', 'velcro', 'velvet', 'window',
'win', 'wedding', 'wet', 'where', 'wild', 'well', 'welcome', 'wonderful', 'xylophone',
'x-ray', 'X-Men', 'Xavier', 'xenon', 'xerox', 'Xerneas', 'Yaphi', 'you', 'yourself',
'your', 'yonder', 'yodel', 'yammer', 'Yveltal', 'Zelda', 'Zygarde', 'zebra',
'zero', 'Zeus', 'zap cannon', 'zephyr', 'zig-zag']

autocomplete('$-*z', dictionary)
#Returns: ['Zelda', 'Zygarde', 'zebra', 'zero', 'Zeus']
