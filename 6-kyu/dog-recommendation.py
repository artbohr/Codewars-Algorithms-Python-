'''
Many people love dogs. Also, many people have or have had a dog, and would want
to get a new dog with a similar personality as their current or previous dog, but
they don't know where to look. Thankfully, you are here to help.

Your task in this kata is to implement a dog recommendation system. You will be
given the name of a dog breed (as a string), for which you will have to return a
set of the breeds that are most similar to this breed in temper (excluding itself).
To aid you in this task, you are given a dictionary, dogs, mapping dog breeds
(e.g., "Chihuahua") to a set of adjectives describing that breed's typical
temperament (e.g., {"Lively", "Devoted", "Courageous", "Alert", "Quick"}).
The dictionary is preloaded, so you may access it as if you had defined
it in your own code.

To be clear, two breeds are more similar in temper the more adjectives they share.
For example, if dog breed A has adjectives {"Lively", "Devoted"}, it is more similar
to dog breed B ({"Lively", "Devoted"}, two adjectives in common) than to dog breed C
({"Lively", "Alert"}, one adjective in common) or even dog breed D ({"Alert", "Quick"},
zero adjectives in common). If one breed has more adjectives in common with the
original breed than any other, return a set containing only this breed. If more
than one breed has the same number of adjectives in common with the original breed,
return a set of these breeds.

To check results with the dictionary (dogs) go to the challenge page:
https://www.codewars.com/kata/dog-recommendation-system/train/python
'''

def find_similar_dogs(breed):
    similarities = 0
    result = {}
    final = set()

    for dog, tempers in dogs.items():
        for temper in tempers:
            if temper in dogs[breed] and dog!=breed:
                similarities+=1
        result[dog] = similarities
        similarities = 0

    for dog, value in result.items():
        if value == result[max(result, key=result.get)]:
            final.add(dog)

    return final

find_similar_dogs('Treeing Cur')
# Returns:
#
# {'Black Norwegian Elkhound', 'Canaan Dog', 'Canadian Eskimo Dog',
#'Lancashire Heeler', 'American Hairless Terrier', 'Australian Kelpie', 'Lhasa Apso',
#'Jack Russell Terrier', 'Airedale Terrier', 'Plott Hound', 'Miniature Schnauzer',
#'Greyhound', 'Siberian Husky', 'Kai Ken', 'Croatian Sheepdog', 'English Springer Spaniel',
#'Shih Tzu', 'Basenji', 'Swedish Vallhund', 'Mudi', 'Kooikerhondje', 'Doberman Pinscher',
#'Nova Scotia Duck-Tolling Retriever', 'Russell Terrier', 'Border Terrier', 'Borzoi',
#'French Bulldog', 'English Toy Terrier', 'Indian Spitz', 'American Eskimo Dog',
#'Maremma Sheepdog', 'Spanish Water Dog', 'Shetland Sheepdog', 'Blue Lacy',
#'Peruvian Hairless Dog', 'Italian Greyhound', 'Irish Water Spaniel','Japanese Chin',
#'Welsh Terrier', 'Prazsky Krysarik', 'Bearded Collie','German Shepherd Dog',
#'Sakhalin Husky', 'Toy Fox Terrier', 'Mexican Hairless Dog', 'Rat Terrier',
#'Australian Stumpy Tail Cattle Dog', 'Sloughi', 'Danish Swedish Farmdog',
#'Weimaraner', 'Eurasier', 'Papillon', 'Poodle', 'Border Collie'}
