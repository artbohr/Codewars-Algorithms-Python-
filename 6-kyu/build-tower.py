"""
    Build Tower by the following given argument:
    number of floors (integer and always greater than 0).

    Tower block is represented as "*"

    for example, a tower of 3 floors looks like below:

    [
      '  *  ',
      ' *** ',
      '*****'
    ]

"""

def tower_builder(n_floors):
  arr = []

  for x in range(n_floors):
    stars  = "*" + "*" * (x*2)
    spaces  = " " * ((2 * (n_floors) - len(stars)) // 2)
    arr.append(spaces + stars + spaces)

  return arr

tower_builder(6)
# returns: ['     *     ', '    ***    ', '   *****   ', '  *******  ', ' ********* ', '***********']
