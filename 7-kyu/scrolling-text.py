def scrolling_text(text):
    return [(text[i:]+text[:i]).upper() for i in range(len(text))]

'''
Your task is to complete the function which takes a string, and returns an
array with all possible rotations of the given string, in uppercase.

Example
scrollingText("codewars") should return:

[ "CODEWARS",
  "ODEWARSC",
  "DEWARSCO",
  "EWARSCOD",
  "WARSCODE",
  "ARSCODEW"
  "RSCODEWA",
  "SCODEWAR" ]
'''
