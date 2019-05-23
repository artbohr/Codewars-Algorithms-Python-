def find_E(s):
    if s=="": return ""

    try:
        amount = s.lower().count('e')
    except AttributeError:
        return None

    return "There is no \"e\"." if not amount else str(amount)

'''
Is it possible to write a book without the letter 'e' ?
Task

Given String str, return:
How much "e" does it contains (case-insensitive) - return number as String.
If given String doesn't contain any "e", return: `"There is no "e"."`
If given String is empty, return empty String.
If given String is `null`/`None`/`nil`, return `null`/`None`/`nil`
'''
