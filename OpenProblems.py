# Code to explore some simple open problems
# described in this video by Joseph Oesterle
# https://m.youtube.com/watch?v=BflyQyBi7y4

import math
import random

# First problem: For any finite family of 
# finite sets F satisfying A and B in F => 
# A union B in F, is there always at least 
# one element that is found in at least half 
# of the sets in F?
# What is known:
#   - true if F contains a set with 1 element
#   - true if |F| <= 46
#   - true if largest set in F has <= 11 elements

def makeUnionClosure(listoflists):
    basesets = map(frozenset, listoflists)
    fam = set()
    for b in basesets:
        fam.update([b] + [b.union(s) for s in fam])
    return fam

# makeUnionClosure([[1,2],[3,4],[5,6],[7,8]])
# makeUnionClosure([[1,2],[2,3],[3,4],[4,5]])

def checkProblem1(listoflists, showallcounts = False, makeUnionClosure = makeUnionClosure):
    fam = makeUnionClosure(listoflists)
    print "Size of family:", len(fam)
    allelems = set().union(*listoflists)
    maxcount = 0
    maxelem = None
    for e in allelems:
        count = 0
        for s in fam:
            if e in s: count += 1
        if showallcounts: print e, count
        if count > maxcount:
            maxcount = count
            maxelem = e
    print maxelem, "occurs", maxcount, "times (", 1.0*maxcount/len(fam), ")"
    return (maxcount >= (len(fam)+1)//2)

# checkProblem1([[1,2],[3,4],[5,6],[7,8]])
# checkProblem1([[1,2],[2,3],[3,4],[4,5]])

def makeRandomFamily(minnumsets = 47, minlargeset = 12, minelement = 1, maxelement = 100, math = math, random = random, makeUnionClosure = makeUnionClosure):
    minbasesets = int(math.ceil(math.log(minnumsets, 2)))
    elems = xrange(minelement, maxelement+1)
    baselists = [random.sample(elems, minlargeset) for i in xrange(minbasesets)]
    fam = makeUnionClosure(baselists)
    print "Size of family:", len(fam)
    largestset = max(fam, key=len)
    print "Largest set has", len(largestset), "elements."
    return baselists

# Three cases --
#   nonoverlap > 0: [1 2) 3 4 (5 6] 7 8 [9 10) ... (n-3 n-2] n-1 n [1 2)
#   nonoverlap = 0: [1 2 3) (4 5 6] [7 8 9) ... (n-2 n-1 n] [1 2 3)
#   nonoverlap < 0: [1 2) (3 4} {5 6] [7 8) (9 10} ... {n-1 n] [1 2) (3 4}
def makeOverlappingRingFamily(numsets, setsize, overlap):
    nonoverlap = (setsize - 2*overlap)
    numelems = (overlap + nonoverlap) * numsets
    laststarter = (overlap + nonoverlap) * (numsets-1)
    wrap = lambda n: n % numelems + 1
    return [map(wrap, range(i, i+setsize)) for i in xrange(0, laststarter+1, setsize-overlap)]

#   return [range(i ,i+setsize) for i in xrange(1, laststarter, setsize-overlap)] + [range(laststarter, numelems+1) + range(1, overlap+1)]

import fractions

# Second problem: the Erdős–Straus conjecture
# For any integer n > 1, can we find positive integers
# a, b, and c such that 4/n = 1/a + 1/b + 1/c ?
# See also https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture
# What is known:
#   - true for n up to 10^17 (verified by computer)
#   - only need to check prime n's because any composite counterexample
#     would imply a smaller counterexample for one of its factors
#   - always true if negative a, b, c are allowed

def egyptiansum(denoms, frac = fractions.Fraction):
    return sum(map(lambda d: frac(1,d), denoms))

def greedy(a, b, frac = fractions.Fraction):
    r = frac(a,b)
    denoms = []
    while r.numerator > 1:
        d = r.denominator // r.numerator + 1
        denoms.append(d)
        r -= frac(1,d)
    if r.numerator == 1:
        denoms.append(r.denominator)
    else:
        print "r =", r
    return denoms

def greedy1(a, b):
    d = b // a + 1
    print d
    a = a*d - b
    b *= d
    return (a,b)

''' Examples
for d in xrange(2,21):
    print "4/%d" % d, greedy(4, d)

for d in xrange(3,41,2):
    denoms = greedy(4, d)
    print "4/%d" % d, denoms, egyptiansum(denoms)
'''

# Search for abundant numbers for which there exist a subset of their divisors that add up to themselves ("pseudoperfect numbers")
# and check that those divisors make unit fractions that add up to 1.
# (Omit multiples of perfect numbers that trivially satisfy these conditions).
for n in [i for i in xrange(2, 500) if i%6 != 0 and i%28 != 0]:
    divs = divisors(n)
    dsum = sum(divs) - n
    if dsum > n:
        divsub = findsublistwithsum(divs[0:-1], n)
        if divsub:
            print n, dsum, divsub, egyptiansum([n/d for d in divsub])

# Search for abundant numbers for which there does NOT exist a subset of their divisors that add up to themselves ("weird numbers").
for n in [i for i in xrange(2, 5000) if i%6 != 0 and i%28 != 0]:
    divs = divisors(n)
    dsum = sum(divs) - n
    if dsum > n and findsublistwithsum(divs[0:-1], n) == None:
        print n, dsum, divs
