# Sums of Distinct Powers
#
# Looking for numbers that are the sums of k
# distinct powers for two different bases.
# This is equivalent to finding numbers that 
# have k ones and the rest zeros in their base
# N & M representations for some N & M.

# Inspired by a related (but more challenging)
# problem in this Numberphile video:
# "Why 82,000 is an extraordinary number"
# https://m.youtube.com/watch?v=LNS1fabDkeA

# Anthony Kozar
# Apr. 30, 2025

# Search parameters to modify

K = 3    # num of powers in each sum
VERBOSE = False
MAXVAL = 10**12
INCL1 = False
BASEMIN = 2
BASEMAX = 100
BASES = xrange(BASEMIN, BASEMAX+1)
basemap = {}

print "Looking for equal sums of %d powers." % K
print "Checking bases from %d to %d" % (BASEMIN, BASEMAX)
print "and values of b^n up to", MAXVAL
if not INCL1: print "not",
print "including ones (b^0). "

# make a set of sums of pairs of distinct elements of arr
def sumsdistinctpairs(arr):
    out=set()
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            out.add(arr[i]+arr[j])
    return out

# Returns a copy of indices with the next values needed to iterate thru all N-tuples of distinct elements in an array of length arrlength. Returns None when indices can no longer be incremented.
# Note: This is the same as iterating over all combinations of N objects chosen from a set of arrlength.
def incrementindices(indices, arrlength):
    N = len(indices)
    if arrlength < N:
        raise ValueError("Array length is smaller than indices length.")
    newidc = list(indices)
    # find the last index that is not its maximum value
    i = N-1
    maxval = arrlength-1
    while i >= 0 and newidc[i] == maxval:
        i -= 1
        maxval -= 1
    if i < 0: return None
    # then increment that index and set each index after it to one more than the previous index
    ival = newidc[i] + 1
    for j in xrange(i, N):
        newidc[j] = ival
        ival += 1
    return newidc

# make a set of sums of N-tuples of distinct elements of arr
def sumsdistinctNtuples(N, arr):
    out=set()
    arrlen = len(arr)
    idc = range(N)
    while idc:
        out.add(sum([arr[idc[i]] for i in xrange(N)]))
        idc = incrementindices(idc, arrlen)
    return out

# map some values to b for later
def dobasemap(bn, b):
    if bn > 1 and bn in BASES and not basemap.has_key(bn):
        basemap[bn] = b

# two bases that are powers of the same number make lots of equal sums
def arepowersofsamebase(n, m):
    if basemap.has_key(n) and basemap.has_key(m):
        return basemap[n] == basemap[m]
    else:
        return False

def powersof(b, maxval = MAXVAL, inclOne = True):
    pows = []
    if inclOne: bn = 1
    else: bn = b
    while bn <= maxval:
        pows.append(bn)
        dobasemap(bn, b)
        bn *= b
    return pows

powsb = {}
for b in BASES:
    powsb[b] = powersof(b, MAXVAL, INCL1)

'''
sumspairs = {}
for b in BASES:
    sumspairs[b] = sumsdistinctpairs(powsb[b])
'''

sumstuples = {}
for b in BASES:
    sumstuples[b] = sumsdistinctNtuples(K, powsb[b])

if VERBOSE: print basemap

# check for any shared values among the sums of tuples of powers with different bases
for i in xrange(len(BASES)-1):
    for j in xrange(i+1, len(BASES)):
        b1 = BASES[i]
        b2 = BASES[j]
        # ignore base pairs that are powers of the same number
        if arepowersofsamebase(b1, b2):
            if VERBOSE:
                print "Skipping base pair %d and %d" % (b1, b2)
            continue
        sharedsums = sumstuples[b1].intersection(sumstuples[b2])
        if len(sharedsums) > 0 or VERBOSE:
            sortedsums = list(sharedsums)
            sortedsums.sort()
            print "Intersections of %d and %d: %s" % (b1, b2, str(sortedsums))

