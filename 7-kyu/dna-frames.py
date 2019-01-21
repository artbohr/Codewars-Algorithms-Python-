def decompose_single_strand(single_strand):
    output = ''

    for frame in range(3):
        output+='Frame {}: {} '.format(frame+1, single_strand[:frame]).strip()
        for i in range(frame,len(single_strand),3):
            output+=' {}'.format(single_strand[i:i+3])
        output+='\n'

    return output[:-1]

'''
In genetics a reading frame is a way to divide a sequence of nucleotides (DNA bases)
 into a set of consecutive non-overlapping triplets (also called codon).
 Each of this triplets is translated into an amino-acid during a translation
 process to create proteins.

Input

In a single strand of DNA you find 3 Reading frames,
 take for example the following input sequence:

AGGTGACACCGCAAGCCTTATATTAGC

Output

For the output we are going to take the combinations and show them in the following manner:

Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC
Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC
Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C

For frame 1 split all of them in groups of three starting by the first base (letter).

For frame 2 split all of them in groups of three starting by the second base (letter)
 but having the first base (letter) at the beggining.

For frame 3 split all of them in groups of three starting by the third letter,
 but having the first and second bases (letters) at the beginning in the same order.
'''
