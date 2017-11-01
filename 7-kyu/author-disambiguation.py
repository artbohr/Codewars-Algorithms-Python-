'''
The objective is to disambiguate two given names: the original with another

Let's start simple, and just work with plain ascii strings.

The function could_be is given the original name and another one to test against.

Example:
could_be("Carlos Ray Norris", "Carlos Ray Norris") : True
could_be("Carlos Ray Norris", "Carlos Ray") : True
could_be("Carlos Ray Norris", "Norris") : True
could_be("Carlos Ray Norris", "Norris Carlos") : True
could_be("Carlos Ray Norris", " ") : False
could_be("Carlos Ray Norris", "carlos") : False
could_be("Carlos Ray Norris", "Norris!") : False
could_be("Carlos Ray Norris", "Carlos-Ray Norris") : False
could_be("Ray Norris", "Carlos Ray Norris") : False
could_be("Carlos", "Carlos Ray Norris") : False
'''

def could_be(original, another):
    if original!="" or another!="":
        for x in another.split(" "):
            if not x in original.split(" "):
                return False
        return True
    return False

could_be("Carlos Ray Norris", "Carlos Norr")
# Returns: False
