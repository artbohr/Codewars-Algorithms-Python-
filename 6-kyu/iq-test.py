'''
Bob is preparing to pass IQ test. The most frequent task in this test is to
find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among the given numbers
finds one that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)

##Examples :
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
'''

def iq_test(numbers):
    numbers = numbers.split()
    odd, even = [], []

    for x in numbers:
        if int(x) % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    diff = odd if len(odd) < len(even) else even
    return numbers.index(diff[0])+1

iq_test('21 41 23 21 49 13 41 5 37 12 9 51 5 33 29 29')
#Returns: 10 -> Index(9) -> number 12
