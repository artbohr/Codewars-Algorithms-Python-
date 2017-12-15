'''
Story

A freak power outage at the zoo has caused all of the electric
cage doors to malfunction and swing open...

All the animals are out and some of them are eating each other!
It's a Zoo Disaster!

Here is a list of zoo animals, and what they can eat

    antelope eats grass
    big-fish eats little-fish
    bug eats leaves
    bear eats big-fish
    bear eats bug
    bear eats chicken
    bear eats cow
    bear eats leaves
    bear eats sheep
    chicken eats bug
    cow eats grass
    fox eats chicken
    fox eats sheep
    giraffe eats leaves
    lion eats antelope
    lion eats cow
    panda eats leaves
    sheep eats grass

Kata Task
INPUT

A comma-separated string representing all the things at the zoo
TASK

Figure out who eats who until no more eating is possible.
OUTPUT

A list of strings (refer to the example below) where:

    The first element is the initial zoo (same as INPUT)
    The last element is a comma-separated string of what the zoo looks like
    when all the eating has finished
    All other elements (2nd to last-1) are of the form X eats Y describing what happened

Notes

    Animals can only eat things beside them
    Animals always eat to their LEFT before eating to their RIGHT
    Always the LEFTMOST animal capable of eating will eat before any others
    Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible

Check this algorithm for 400+ random test cases:
https://www.codewars.com/kata/the-hunger-games-zoo-disaster/python
'''


def who_eats_who(zoo):
    rules = {
        "antelope":["grass"],
        "big-fish":["little-fish"],
        "bug":["leaves"],
        "bear":["big-fish","bug","chicken","cow","leaves","sheep"],
        "chicken":["bug"],
        "cow":["grass"],
        "fox":["chicken", "sheep"],
        "giraffe":["leaves"],
        "lion":["antelope", "cow"],
        "panda":["leaves"],
        "sheep":["grass"]
    }

    # add unknown dict elements
    for el in zoo.split(','):
        if el not in rules:
            rules[el] = []

    zoo_list = zoo.split(",")
    final = [zoo]
    count = 1

    while count > 0:
        count = 0

        for index, animal in enumerate(zoo_list):
            if len(zoo_list) < 2:
                break

            # if animal is first in the list, only look to the right
            if index == 0:
                animal_r = zoo_list[index+1]
                if animal_r in rules[animal]:
                    final.append("{} eats {}".format(animal, animal_r))
                    del zoo_list[index+1]
                    count+=1
                    break

            # if animal is last in the list, only look to the left
            elif index == len(zoo_list)-1:
                animal_l = zoo_list[index-1]
                if animal_l in rules[animal]:
                    final.append("{} eats {}".format(animal, animal_l))
                    del zoo_list[index-1]
                    count+=1
                    break

            # if animal is not last or first, look to the left then to the right
            else:
                animal_r = zoo_list[index+1]
                animal_l = zoo_list[index-1]

                if animal_l in rules[animal]:
                    final.append("{} eats {}".format(animal, animal_l))
                    del zoo_list[index-1]
                    count+=1
                    break

                elif animal_r in rules[animal]:
                    final.append("{} eats {}".format(animal, animal_r))
                    del zoo_list[index+1]
                    count+=1
                    break

    final.append(",".join(zoo_list))
    return final

who_eats_who("fox,bug,chicken,grass,sheep")
# Returns:
# ['fox,bug,chicken,grass,sheep', 'chicken eats bug', 'fox eats chicken', 'sheep eats grass', 'fox eats sheep', 'fox']
