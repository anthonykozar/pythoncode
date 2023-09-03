from collections import defaultdict

def modadd(a, b, mod):
    return (a+b)%mod

def modmult(a, b, mod):
    return (a*b)%mod

def modpow(a, exp, mod):
    prod = 1
    for i in xrange(exp):
        prod = (prod*a)%mod
    return prod

def modneg(a, mod):
    return -a % mod

def prmulttable(mod):
    for i in xrange(1,mod):
        for j in xrange(1,mod):
            p = (i*j)%mod
            if p < 10:
                print " %d" % p,
            else:
                print p,
        print

# Returns a list of the square numbers in 
# Z_mod. Only needs to square half of the
# elements because of symmetry:
#   x^2 = (-x)^2 = (mod-x)^2
def modsquares(mod):
    return [(i*i)%mod for i in xrange(0,(mod+2)//2)]

# Returns a set of the square numbers in 
# Z_mod.
def setofsquares(mod):
    return set([(i*i)%mod for i in xrange(0,(mod+2)//2)])

# Returns a list of all solutions of the
# elliptic curve y^2 = x^3 + Ax + B over
# the ring Z_mod. Each solution is a pair
# (x,y).
def solveEllipticCurve(A, B, mod, defaultdict = defaultdict):
    # build a map of each square element to its roots
    sqrroots = defaultdict(list)
    for i in xrange(mod):
        sqrroots[(i*i)%mod].append(i)
    solutions = []
    for x in xrange(mod):
        cubic = (x**3 + A*x + B) % mod
        if len(sqrroots[cubic]) > 0:
            for y in sqrroots[cubic]:
                solutions.append((x, y))
    return solutions

# example of finding the coefficients of the power series for y^2 = x^3 + x + 5
[len(solveEllipticCurve(1, 5, n)) for n in xrange(2, 33)]
[(n, len(solveEllipticCurve(1, 5, n))) for n in xrange(2, 33)]

# print a table of the sums of powers mod k
# a^n + b^n (mod k)
def prfermattable(exp, mod, modadd = modadd, modpow = modpow):
    for i in xrange(mod):
        for j in xrange(mod):
            p = modadd(modpow(i, exp, mod), modpow(j, exp, mod), mod)
            if p < 10:
                print " %d" % p,
            else:
                print p,
        print

# Find all moduli m up to MMAX where all residues 0..m-1 can be cubes.
# i.e. {i^3 mod m | 0 <= i < m} == {0 ,1, ..., m-1}
MMAX = 1000
mcomplt = []
for m in xrange(2, MMAX+1):
    cubes = [modpow(i,3,m) for i in xrange(m)]
    cset = set(cubes)
    if len(cset) == m:
        mcomplt.append(m)
# mcomplt is an interesting and non-obvious sequence.
# See moduli-with-all-cubic-residues.txt

# Conjecture: All elements of mcomplt are square-free. 
from math import sqrt
nmax = int(sqrt(MMAX))
sq = [n*n for n in xrange(2, nmax+1)]
[m for m in mcomplt if any([m%d == 0 for d in sq])]

# Find all elements of mcomplt not divisible by any previous elements of mcomplt.
# Conjecture: Elements of nondiv are all prime
nondiv = [mcomplt[i] for i in xrange(len(mcomplt)) if all([mcomplt[i]%d != 0 for d in mcomplt[0:i]])]

comp = [m for m in mcomplt if not m in nondiv]

# nondiv are the primes congruent to 0 or 2 (mod 3)
# See OEIS sequence A045309.
map(lambda n: n%3, nondiv)
