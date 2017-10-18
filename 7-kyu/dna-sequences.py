'''
In genetics 2 differents DNAs sequences can code for the same protein.

This is due to the redundancy of the genetic code, in fact 2 different
tri-nucleotide can code for the same amino-acid.
For example the tri-nucleotide 'TTT' and the tri-nucleotide 'TTC' both code for
the amino-acid 'F'. For more information you can take a look here.

Your goal in this kata is to define if two differents DNAs
sequences code for exactly the same protein. Your function take the
2 sequences you should compare. For some kind of simplicity here the sequences
will respect the following rules:

    It is a full protein sequence beginning with a Start codon and finishing by an Stop codon
    It will only contain valid tri-nucleotide.

The translation hash is available for you under a translation hash
 $codons [Ruby] or codons [Python and JavaScript].
'''
codons =   {'ATT': 'I', 'GCG': 'A', 'CAC': 'H', 'TCG': 'S', 'TGC': 'C', 'CAG': 'Q',
'GCA': 'A', 'GGT': 'G', 'CCA': 'P', 'ATC': 'I', 'GTG': 'V', 'CGT': 'R', 'GTC': 'V',
'CTT': 'L', 'CAT': 'H', 'AAG': 'K', 'TCA': 'S', 'CTG': 'L', 'GGG': 'G', 'AGG': 'R',
'AGT': 'S', 'AGA': 'R', 'AGC': 'S', 'GAC': 'D', 'AAC': 'N', 'TTC': 'F', 'TTG': 'L',
'TTA': 'L', 'CGA': 'R', 'TAA': '*', 'ACT': 'T', 'ATG': 'M', 'CCG': 'P', 'CCC': 'P',
'TCT': 'S', 'ATA': 'I', 'GAT': 'D', 'TCC': 'S', 'GGC': 'G', 'TGA': '*', 'TAC': 'Y',
'TGT': 'C', 'AAA': 'K', 'GCT': 'A', 'GGA': 'G', 'CTA': 'L', 'TTT': 'F', 'GAA': 'E',
'GCC': 'A', 'TAT': 'Y', 'CTC': 'L', 'GAG': 'E', 'ACC': 'T', 'TGG': 'W', 'ACG': 'T',
'GTT': 'V', 'TAG': '*', 'CAA': 'Q', 'CGG': 'R', 'CGC': 'R', 'AAT': 'N', 'GTA': 'V',
'ACA': 'T', 'CCT': 'P'}


def code_for_same_protein(seq1,seq2):
    for x in range(0,len(seq1),3):
       if codons[seq1[x:x+3]] != codons[seq2[x:x+3]]:
           return False
    return True

code_for_same_protein("ATGTTTTAA","ATGTTCTAA")
# Returns: True
