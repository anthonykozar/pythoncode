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
