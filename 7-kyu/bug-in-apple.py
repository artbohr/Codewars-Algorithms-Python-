def sc(apple):
    for i, x in enumerate(apple):
        try:
            return [i, x.index('B')]
        except:
            continue

'''
#Task:

Find out "B"(Bug) in a lot of "A"(Apples).

There will always be one bug, no need to consider the case of no bugs or several
bugs, all the cases contain only 1 bug to be found.

input: string Array ```apple```

output: Location of "B", ```[x,y]```

'''
