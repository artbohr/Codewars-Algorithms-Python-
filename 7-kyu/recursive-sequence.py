def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        return begin_number + sequence_sum(begin_number+step, end_number, step)

'''
Examples

sequenceSum(2,2,2) === 2
sequenceSum(2,6,2) === 12 // 2 + 4 + 6
sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequenceSum(1,5,3) === 5 // 1 + 4
'''
