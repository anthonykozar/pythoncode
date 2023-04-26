# Sequence Transformations
# March 13, 2018

# Partial Sums transform
# (In new sequence, B(n) is the sum of the first n elements of A(n))

def PartialSums(seq):
    return [sum(seq[0:i]) for i in range(1, len(seq)+1)]

def NthPartialSums(N, seq):
    sums = seq
    for i in range(N):
        sums = PartialSums(sums)
    return sums

# First and Nth differences transforms
def FirstDiffs(seq, includeFirstTerm = False):
    diffs = [seq[i] - seq[i-1] for i in range(1,len(seq))]
    if includeFirstTerm:
        diffs = seq[0:1] + diffs
    return diffs

def NthDiffs(N, seq, includeFirstTerm = False):
    diffs = seq
    for i in range(N):
        diffs = FirstDiffs(diffs, includeFirstTerm)
    return diffs

# Define a set of sequences including the natural numbers, triangular numbers,
# tetrahedral numbers, etc.

numSequences = 11
seqLength = 288
a0 = [1] + [0]*(seqLength-1)
a1 = [1]*seqLength
a = [a0, a1] + [None]*(numSequences-2) # an array of integer sequences

# Each sequence a[i] is the partial sums transform of a[i-1]
for i in range(2, numSequences):
    a[i] = PartialSums(a[i-1])


# number of columns to print different modulos of a sequence
cols = [72, 72, 8, 9, 16, 25, 72, 49, 32, 27, 25, 11, 72, 13, 56, 25, 64, 17, 54, 19, 20]

def PrintModuliInColumns(seq, mod, columns = 0):
    print "seq %% %d\n" % mod
    if columns == 0 and mod < len(cols):
        columns = cols[mod] # use default if none given
    count = 0
    for a in seq:
        print str(a % mod) + ",",
        count += 1
        if count == columns:
            print
            count = 0
    print "\n"


# Function to calculate number of combinations of r objects from a set of n ("n Choose r")
# from https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import operator as op

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom

# number of permutations of r objects from a set of n
def nPr(n, r):
    return reduce(op.mul, xrange(n, n-r, -1), 1)

# altsign(n) returns (-1)^n
def altsign(n):
    if n%2 == 0: return 1
    else: return -1


# Binomial transform
# https://en.wikipedia.org/wiki/Binomial_transform

def BinomialTransform(seq):
    return [sum( [altsign(k)*nCr(n,k)*seq[k] for k in range(n+1)] )
            for n in range(len(seq))]


# (L)-sieve transform
# Defined at https://oeis.org/A152009
#
# If seq is the complete list of elements of a finite sequence, then
# the values of its LST can be computed arbitrarily high.  But if higher terms
# are missing from seq, then we cannot accurately compute its LST beyond the
# maximum term in seq (or max+1). (right?)
def LSieveTransform(seq, seqIsComplete = False, Nlength = None, debug = True):
    seq = sorted(seq)
    seqmax = max(seq)
    seqlen = len(seq)
    # if seq is complete and Nlength is given, use it, otherwise
    # set a default limit for how many natural numbers to start with in N
    if not seqIsComplete:
        Nlength = seqmax+1
    elif Nlength == None:
        Nlength = seqmax + seqlen**2
    N = range(1, Nlength+1)
    s = []
    if debug: print "N = [1 ... %d]" % Nlength
    while len(N) > 0:
        # remove the first element of N and put it in the output seq s()
        e = N[0]
        N.remove(e)
        s.append(e)
        deleted = []
        # for each k in seq, delete the kth element of N
        # delete them in reverse order so that the indices of the rest of N don't change!
        for i in xrange(seqlen-1, -1, -1):
            k = seq[i]
            if k <= len(N):
                e = N[k-1]
                N.remove(e)
                deleted.insert(0, e)
        if debug:
            print "s =", s
            print "deleted =", deleted[0:100], "(...)"
            print "N =", N[0:100], "(...)"
        # if len(N) < seqmax + 1:
        #    break
    
    return s

