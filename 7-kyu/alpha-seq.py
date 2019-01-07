def alpha_seq(string):
    return ','.join((x*(ord(x)-96)).capitalize() for x in sorted(string.lower()))

'''
In this kata you will be given a random string of letters and tasked with returning
 them as a string of comma-separated sequences sorted alphabetcally, with each
 sequence starting with an uppercase character followed by n-1 lowercase characters,
 where n is the letter's alphabet position 1-26.

Example

alpha_seq("ZpglnRxqenU") -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,
Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,
Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"

Technical Details

    The string will include only letters.
    The first letter of each sequence is uppercase followed by n-1 lowercase.
    Each sequence is seperated with a comma.
    Return value needs to be a string.
'''
