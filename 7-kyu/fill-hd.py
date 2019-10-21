def save(sizes, hd): 
    for i in range(len(sizes)):
        sm = sum(sizes[:i+1])
        if sm>hd:
            return i
        elif sm==hd:
            return i+1
    return len(sizes)

'''
Your task is to determine how many files of the copy queue you will be
 able to save into your Hard Disk Drive.
 
Input:

    Array of file sizes (0 <= s <= 100)
    Capacity of the HD (0 <= c <= 500)

Output:

    Number of files that can be fully saved in the HD

Examples:

save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, but 4+4+4+3 > 12

save([4,4,4,3,3], 11) -> 2
# 4+4 <= 11, but 4+4+4 > 11

Do not expect any negative or invalid inputs.

'''