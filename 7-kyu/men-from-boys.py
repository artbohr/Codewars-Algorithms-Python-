def men_from_boys(arr):
    even, odd = [], []

    [even.append(x) if x%2==0 else odd.append(x) for x in set(arr)]

    return sorted(even) + sorted(odd,reverse=True)

'''
Scenario

Now that the competition gets tough it will Sort out the men from the boys .

Men are the Even numbers and Boys are the odd

Task

Given an array/list [] of n integers, Separate The even numbers from the odds,
or Separate the men from the boys

Notes

    Return an array/list where Even numbers come before the odds

    Since Men are stronger than the Boys, sort the Even numbers in
    ascending order While the odds in descending order.

    Array/list numbers could be a mixture of positives , negatives .

'''
