# Functions for creating, applying, and decoding simple ciphers

import operator

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Scramble a string using a linear congruence (an affine transformation?)
# The multiplier and the length of inputalphabet should be
# relatively prime.
def makeLCGcipher(inputalphabet, multiplier, offset):
    cipheralphabet = ""
    alphsize = len(inputalphabet)
    for i in range(alphsize):
        pos = (offset + i*multiplier) % alphsize
        cipheralphabet += inputalphabet[pos]
    return cipheralphabet

def makeROTcipher(inputalphabet, offset):
    return makeLCGcipher(inputalphabet, 1, offset)

def sortstr(s):
    slist = list(str(s))
    slist.sort()
    ssorted = reduce(operator.add, slist)
    return ssorted

# assumes cipher and inputalphabet are all uppercase
def decodechar(char, key, inputalphabet = alphabet):
    pos = inputalphabet.find(char.upper())
    if pos < 0:
        return char
    else:
        outch = key[pos]
        if char.islower():
            return outch.lower()
        else:
            return outch.upper()

def decode(text, key, inputalphabet = alphabet):
    transfunc = lambda ch:decodechar(ch,key,inputalphabet)
    decodedlist = map(transfunc, text)
    return reduce(operator.add, decodedlist)

def encode(text, decodekey, inputalphabet = alphabet):
    return decode(text, inputalphabet, decodekey)

def makecipher(key):
    return encode(alphabet, key)

def searchLCG(text):
    for multiplier in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for offset in range(26):
            key = makeLCGcipher(alphabet, multiplier, offset)
            print multiplier, offset, decode(text, key)


# specific ciphers for Zendo games
Zendo22246 = makeLCGcipher(alphabet, 5, 3)

HAS = ["b","db","dhbi","ixhd","sbmlibh","sbmlibhd"]
HASNOT = ["bh","bm","bs","dmldi","hd","ib","ibb","li","lxths","mblxi","sbm","sbml"]


# cipher for Tim's "secret decoder ring"

TimsDecoderKey = 'FKYHARUZJGMCELDQPSWOIXBTNV'
TimsEncoderKey = 'EWLOMAJDUIBNKYTQPFRXGZSVCH'   # the outside ring of the decoder
