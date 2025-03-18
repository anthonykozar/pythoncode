# ThueMorse.py

# Anthony Kozar
# Mar. 16, 2025

from numbases import baseconvert

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
        return ("elements", "squares", "cubes")[n-1]
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

for n in xrange(2, 17):
    powf = PowerFunc(n)
    evilpow = map(powf, evil)
    odiouspow = map(powf, odious)
    chunksize = 2**n
    print "Sums of %d %s equal?" % (chunksize, powdescr(n)), sumchunks(evilpow, chunksize) == sumchunks(odiouspow, chunksize)

# sumchunks(sumchunks(cubes[:160], 8), 5), where cubes is either the cubes of the evil numbers or the cubes of the odious numbers, gives multiples of 100. Why?
# Any other patterns in the sums of other chunk sizes?

if __name__ == '__main__':
    import sys
    
    for arg in sys.argv[1:]:
        base = int(arg)
        if base >= 2 and base <= 10:
            checkidentities(base)
            print
