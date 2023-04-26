# findprimes.py
#
# Different approaches for searching for primes.
#
# Anthony Kozar
# February 7, 2017

import math
import bisect

# The really naive approach:
# try dividing each number by every number less than it.
# Benchmarks:
#   maxnum =    50,000  time = 1:00
#   maxnum =   100,000  time = 3:40
#   maxnum =   200,000  time = 14:34
#   maxnum = 1,000,000  time = incomplete after 2 hours
def findprimes1(maxnum = 100, echoCount = True, echoProgress = False, echoPrimes = False):
    primes = []
    for n in range(2, maxnum+1):
        foundDivisor = False
        for p in range(2, n):
            if n % p == 0:
                foundDivisor = True
                break
        if not foundDivisor:
            primes.append(n)
            if echoPrimes:
                print n
        if echoProgress and n % 1000 == 0:
            print "Searched thru %s" % n 
    if echoCount:
        print len(primes)
    return primes

# primes = findprimes1(10000, True, True)

# The fairly naive approach:
# try dividing each number by every prime less than it.
# Benchmarks:
#   maxnum =   100,000  time = ~ 7.3 secs
#   maxnum =   200,000  time = 0:27
#   maxnum =   500,000  time = 2:29
#   maxnum = 1,000,000  time = 9:44
def findprimes2(maxnum = 100, echoCount = True, echoProgress = False, echoPrimes = False):
    primes = []
    for n in range(2, maxnum+1):
        foundDivisor = False
        for p in primes:
            if n % p == 0:
                foundDivisor = True
                break
        if not foundDivisor:
            primes.append(n)
            if echoPrimes:
                print n
        if echoProgress and n % 10000 == 0:
            print "Searched thru %s" % n 
    if echoCount:
        print len(primes)
    return primes

# primes = findprimes2(100000, True, True)

# The "minimal divisions" approach:
# try dividing each number by every prime less than its square root.
# Benchmarks:
#   maxnum =    100,000  time = < 0.5 secs
#   maxnum =    200,000  time = < 0.7 secs
#   maxnum =  1,000,000  time = ~ 4.5 secs
#   maxnum = 10,000,000  time = 1:13
def findprimes3(maxnum = 100, echoCount = True, echoProgress = False, echoPrimes = False):
    primes = []
    for n in range(2, maxnum+1):
        foundDivisor = False
        nroot = int(math.sqrt(n))
        for p in primes:
            if p > nroot:
                # stop once the primes exceed the square root of n
                break
            if n % p == 0:
                foundDivisor = True
                break
        if not foundDivisor:
            primes.append(n)
            if echoPrimes:
                print n
        if echoProgress and n % 100000 == 0:
            print "Searched thru %s" % n 
    if echoCount:
        print len(primes)
    return primes

# primes = findprimes3(1000000, True, True)

# HYBRID APPROACHES
# that use divisions combined with simple sieving techniques
# to reduce the number of numbers that must be checked.

# Try dividing each number by every prime less than its square root.
# Optimizations:
#   - square primes instead of calling sqrt()
#   - skip even numbers
#
# Benchmarks:
#   maxnum =    100,000  time = < 0.4 secs
#   maxnum =  1,000,000  time = ~ 3.4 secs
#   maxnum = 10,000,000  time = 1:01
def findprimes4(maxnum = 100, echoCount = True, echoProgress = False, echoPrimes = False):
    primes = [2]
    # keep track of the maximum prime that needs to be checked
    idx = 0
    plimit = primes[idx]
    plimitsqrd = plimit * plimit
    # start with 3 and step by 2
    for n in range(3, maxnum+1, 2):
        foundDivisor = False
        # current plimit valid only up to plimitsqrd
        if n > plimitsqrd:
            # recalculate limits
            idx += 1
            plimit = primes[idx]
            plimitsqrd = plimit * plimit            
        for p in primes:
            if p > plimit:
                # stop once the primes exceed the square root of n
                break
            if n % p == 0:
                foundDivisor = True
                break
        if not foundDivisor:
            primes.append(n)
            if echoPrimes:
                print n
        if echoProgress and (n+1) % 100000 == 0:
            print "Searched thru %s" % (n+1) 
    if echoCount:
        print len(primes)
    return primes

# primes = findprimes4(1000000, True, True)


# UTILITIES

def printincolumns(alist, numcols, colwidth = 4):
    numrows = len(alist) / numcols
    for row in range(numrows):
        for col in range(numcols):
            print "%*s" % (colwidth, alist[numcols*row+col]),
        print
    # print a partial row if necessary
    for i in range(numcols*numrows, len(alist)):
        print "%*s" % (colwidth, alist[i]),
    print

# printincolumns(range(1,31), 6)
# printincolumns(findprimes4(1000, False), 10, 5)

# Returns true if val in alist.  Uses binary search so alist must be presorted.
def insortedlist(val, alist, low=0, high=None):
    if high == None: high=len(alist)
    i = bisect.bisect_left(alist, val, low, high)
    return (i != len(alist) and alist[i] == val)

# Uses binary search to find the index of val in alist.  alist must be presorted.
# Returns the index or None if val not found.
# (Code adapted from example at https://docs.python.org/2/library/bisect.html )
def indexinlist(val, alist, low=0, high=None):
    if high == None: high=len(alist)
    i = bisect.bisect_left(alist, val, low, high)
    if i != len(alist) and alist[i] == val:
        return i
    return None


# FIND LISTS OF SPECIAL PRIMES

# Find Sophie Germain primes in a sorted list of primes.
# A Sophie Germain prime is a prime p where 2p+1 is also prime.
# https://en.wikipedia.org/wiki/Sophie_Germain_prime
# NOTE: Only returns p if 2p+1 is also in input list!
def findSophie(primes):
    largestp = primes[len(primes)-1]
    limit = largestp // 2 # only check numbers where 2p+1 could be in primes
    sophie = []
    for idx in xrange(len(primes)):
        p = primes[idx]
        if p > limit: return sophie
        if insortedlist(2*p+1, primes, idx+1):
            sophie.append(p)
    return sophie

# Find "safe" primes in a sorted list of primes.
# A safe prime is a prime 2p+1 where p is also prime.
# https://en.wikipedia.org/wiki/Safe_prime
# NOTE: Only returns p if (p-1)/2 is also in input list!
def findsafe(primes):
    safe = []
    for idx in xrange(len(primes)):
        p = primes[idx]
        if insortedlist((p-1)//2, primes, 0, idx):
            safe.append(p)
    return safe

# Find chains of numbers in a sorted list that satisfy a given relation.
# nextval(n, nthval) should be a function that returns the next value of a
# chain if the n'th value is nthval.  Set disjoint = True if the chains
# are expected to be pairwise disjoint.  minlen is the minimum length for
# a complete chain to be returned.
def findchains(numlist, nextval, disjoint = False, minlen = 2):
    smallestn = numlist[0]
    largestn = numlist[len(numlist)-1]
    chains = []
    def notdisjoint(val):
        # check if val is in another chain
        foundi = False
        for ch in chains:
            if val in ch:
                foundi = True
                break
        return foundi
    for idx in xrange(len(numlist)):
        # start a new chain
        i = numlist[idx]
        curchain = [i]
        n = 1
        sortidx = idx
        if disjoint and notdisjoint(i):
            continue
        while True:
            # check next value
            j = nextval(n, i)
            if j > largestn or j < smallestn:
                break
            if disjoint and notdisjoint(j):
                break
            # find index of j in numlist
            if j > i:
                jidx = indexinlist(j, numlist, sortidx+1)
            elif j < i:
                jidx = indexinlist(j, numlist, 0, sortidx)
            else:
                jidx = sortidx # j == i
            if jidx == None:
                break
            else:
                # add j to chain if it was in numlist
                curchain.append(j)
                n += 1
                i = j
                sortidx = jidx
        # end of chain
        if n >= minlen:
            chains.append(curchain)
    return chains

# Nextval functions for findchains()

# Find Cunningham chains of the first kind
# https://en.wikipedia.org/wiki/Cunningham_chain
def Cunningham1(n, nth):
    return 2*nth + 1

# Find Cunningham chains of the second kind
def Cunningham2(n, nth):
    return 2*nth - 1

