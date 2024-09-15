# Caboose Numbers
# June 21, 2024

# See this Numberphile video:
# https://m.youtube.com/watch?v=gM5uNcgn2NQ

# Usually called Euler's lucky numbers and closely related to Heegner numbers.
# https://en.m.wikipedia.org/wiki/Heegner_number

from findprimes import findprimes4

# Make a list of the values of the polynomial
# n^2 + n (which are twice the triangular numbers).
def basevalues(maxn, maxval = None):
    a = []
    for n in xrange(maxn+1):
        val = n*n + n
        if maxval and val > maxval:
            break
        a.append(val)
    
    return a
    
# Check prime numbers p from 3 to maxprime to 
# see if the formula n^2 + n + p produces
# prime numbers for 0 <= n <= p-2.
# If minmatches is a positive integer, then also print a message for any p for which
# n^2 + n + p produces at least minmatches consecutive primes (starting with n = 0).
def findcabooses(maxprime, minmatches = None, primes = None, primesf = findprimes4, basevalues = basevalues):
    if not primes:
        maxp = maxprime*(maxprime+2)
        primes = primesf(maxp, False, False, False)
    pset = frozenset(primes)
    polyvals = basevalues(maxprime)
    lastp = 0
    cabnums = []
    for p in primes:
        if p > maxprime: break
        incr = p - lastp
        polyvals = map(lambda v: v+incr, polyvals)
        for i in xrange(len(polyvals)):
            if polyvals[i] not in pset:
                break
        if i >= p-2:
            print p, "is a caboose number"
            cabnums.append(p)
        if type(minmatches) == int and minmatches > 0 and i >= minmatches:
            print p, "produces", i, "primes"
        lastp = p
    
    return cabnums

findcabooses(3163, 9)
