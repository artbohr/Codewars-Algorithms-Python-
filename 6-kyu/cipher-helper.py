# python 2.7.6

from string import maketrans

class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, string):
        enc = maketrans(self.map1, self.map2)
        return string.translate(enc)

    def decode(self, string):
        dec = maketrans(self.map2, self.map1)
        return string.translate(dec)

'''
A simple substitution cipher replaces one character from an alphabet with a
 character from an alternate alphabet, where each character's position in an
 alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"

If a character provided is not in the opposing alphabet, simply leave it as be.

'''
