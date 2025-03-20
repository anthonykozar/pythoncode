# ThueMorse.py
# coding=utf-8

# Anthony Kozar
# Mar. 16, 2025

from numbases import baseconvert
from SequenceTransforms import FirstDiffs

# Make a Thue-Morse-like sequence in any base from 2 thru 10.
def ThueMorseSequence(length, base=2, baseconvert = baseconvert):
    if base < 2 or base > 10:
        raise ValueError("Invalid base parameter")
    s = ""
    for n in xrange(length):
        nbase = baseconvert(n, base)
        digitsum = sum(map(int, list(nbase)))
        s += str(digitsum % base)
    return s

def sumchunks(seq, chunksize):
    return [sum(seq[i:i+chunksize]) for i in xrange(0 ,len(seq), chunksize)]

class PowerFunc(object):
    def __init__(self, power):
        self.n = power
    
    def __call__(self, x):
        return x**self.n

def powdescr(n):
    if n > 3:
        return "%dth powers" % n
    elif n > 0:
        return ("terms", "squares", "cubes")[n-1]
    else:
        raise ValueError(n)

def closestpower(b, target = 1000000):
    logb = math.log(target) / math.log(b)
    p = int(round(logb))
    return (p, b**p)


tm2 = ThueMorseSequence(131072)
evil = [i for i in xrange(len(tm2)) if tm2[i]=='0']
odious = [i for i in xrange(len(tm2)) if tm2[i]=='1']
print "Sums of pairs equal?", sumchunks(evil, 2) == sumchunks(odious, 2)

def checkidentities(base):
    for n in xrange(2, 17):
        powf = PowerFunc(n)
        evilpow = map(powf, evil)
        odiouspow = map(powf, odious)
        chunksize = 2**n
        print "Sums of %d %s equal?" % (chunksize, powdescr(n)), sumchunks(evilpow, chunksize) == sumchunks(odiouspow, chunksize)

def runlengths(seq, val):
    count = 0
    runs = []
    for e in seq:
        if e == val:
            count += 1
        elif count > 0:
            runs.append(count)
            count = 0
    return runs

# compare the beginnings of two lists that may be different lengths
def compareseqs(seq1, seq2, length=None):
    if length == None:
        length = min(len(seq1), len(seq2))
    return seq1[:length] == seq2[:length]

# find additional identities
def findidentities(power, chunksize):
    a = []
    powf = PowerFunc(power)
    for i in xrange(len(evil)-chunksize+1):
        ev4 = evil[i:i+chunksize]
        od4 = odious[i:i+chunksize]
        es = sum(map(powf, ev4))
        os = sum(map(powf, od4))
        if es == os and i%chunksize != 0:
            a.append(i)
    return a

a = findidentities(3, 8)
print "Identity true for:", a[:50]

# a = findidentities(2, 4)
# a[] is the sequence 6, 22, 30, 38, 54, 70, 86, 94 ...
# Dividing each term by 2 matches OEIS A131323
# "Odd numbers whose binary expansion ends in an even number of 1's".
# for n in  a[:50]:
#     print "%12s" % bin(n)
# Yep! So, the identity e[i]²+e[i+1]²+e[i+2]²+e[i+3]² = o[i]²+o[i+1]²+o[i+2]²+o[i+3]²,
# where e[n] are the evil numbers and o[n] are the odious numbers, 
# appears to hold whenever i%4 == 0 or i is 
# twice a member of A131323.

# The first differences of a[] have an interesting pattern that is similar
# to an Eta sequence:
# [16, 8, 8, 16, 16, 16, 8, 8, 16, 8, 8, 16, 8, 8, 16, 16, 16, 8, 8, 16, 16, 16, 8, 8, 16, 16, 16, 8, 8, 16, 8, 8, ...]
ad = FirstDiffs(a)
print "First diffs:", ad[:50]
# And the run lengths of the 16s make a
# sequence of 1s & 3s with the run lengths of the 3s equal to the sequence itself!
# [1, 3, 1, 1, 3, 3, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 3, 3, 3, ...]
runs16 = runlengths(ad, 16)
print "Run lengths of 16:", runs16[:50]
runs3 = runlengths(runs16, 3)
print "Run lengths of 3:", runs3[:50]
print "Run lengths of 16 & 3 equal?", runs16[:len(runs3)] == runs3

# sumchunks(sumchunks(cubes[:160], 8), 5), where cubes is either the cubes of the evil numbers or the cubes of the odious numbers, gives multiples of 100. Why?
# Any other patterns in the sums of other chunk sizes?

if __name__ == '__main__':
    import sys
    
    for arg in sys.argv[1:]:
        base = int(arg)
        if base >= 2 and base <= 10:
            checkidentities(base)
            print
