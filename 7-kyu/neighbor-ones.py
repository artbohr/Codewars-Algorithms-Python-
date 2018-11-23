def ones_counter(input):
    output = []
    cons = 0

    for x in input:
        if x == 1:
            cons += 1
        else:
            if cons>0:
                output.append(cons)
                cons = 0
    if cons>0:
        output.append(cons)

    return output

'''
Tranform of input array of zeros and ones to array
in which counts number of continuous ones:

[1, 1, 1, 0, 1] -> [3,1]

'''
