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

def divisors(num):
    return [1] + [n for n in xrange(2, num/2+1) if num % n == 0] + [num]

# Returns None if no sublist exists that sums to targetsum.
def findsublistwithsum(nums, targetsum):
    nums.sort()
    totalsum = sum(nums)
    if totalsum < targetsum:
        return None
    elif totalsum == targetsum:
        return nums
    else:
        sublist = []
        backupstates = []
        needed = targetsum
        idx = len(nums) - 1
        while needed > 0:
            while idx >= 0 and nums[idx] > needed: idx -= 1
            if idx >= 0:
                backupstates.append((idx-1, needed, list(sublist)))
                sublist.append(nums[idx])
                needed -= nums[idx]
                if needed == 0:
                    sublist.reverse()
                    return sublist
                idx -= 1
            elif len(backupstates) > 0:
                idx, needed, sublist = backupstates.pop()
            else:
                return None
    print "Warning: findsublistwithsum() reached the end."
    return None

# Search for abundant numbers for which there exist a subset of their divisors that add up to themselves ("pseudoperfect numbers") and check that those divisors make unit fractions that add up to 1.
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

# "Practical numbers" are positive integers for which all smaller positive integers are equal to a sum of some of its proper divisors.
# https://en.m.wikipedia.org/wiki/Practical_number

# Verify that num satisfies the definition of a practical number.
def verifypracticalbydef(num, divisors = divisors, findsublistwithsum = findsublistwithsum):
    divs = divisors(num)
    for n in xrange(1, num):
        if findsublistwithsum(divs, n) == None:
            return False
    return True

# A complete sequence is a sequence of natural numbers such that every natural number can be represented as a sum of elements in the sequence using each value at most once.  (If there are duplicates in the sequence, each can be used once).
# An ordered sequence a[n] is complete if and only if a[0] = 1 and a[k] <= sum(a[0]...a[k-1]) + 1. I'm pretty sure that these conditions are enough to guarantee that a finite sequence can make any number up to the total sum of the sequence.
# seq should be sorted
def iscompleteseq(seq):
    if seq[0] != 1: return False
    psum = 1
    for ak in seq[1:]:
        if ak > psum + 1: return False
        psum += ak
    return True

# A more efficient way to determine if a number is practical.
# iscompleteseq() is probably sufficient but we can avoid calling divisors in simple cases.
def ispractical(num, divisors = divisors, iscompleteseq = iscompleteseq):
    if num == 1 or num == 2:
        return True
    elif num%4 == 0 or num%6 == 0:
        return iscompleteseq(divisors(num))
    else:
        return False
