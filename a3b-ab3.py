# Prove that given any three integers, 
# there is a pair (a,b) among them such that
# (a**3)*b - a*(b**3) is divisible by 10.

# This problem came from a YouTube video and
# suggested other interesting questions to me. 
# Anthony Kozar
# March 15-16, 2026

from itertools import combinations

def f(a,b):
    return (a**3)*b - a*(b**3)

def evalpairs(ilist, f=f):
    from itertools import combinations
    def pf(x,y):
        print "f(%d,%d) = %d" % (x, y, f(x,y))
    isorted = sorted(ilist)
    for (b,a) in combinations(isorted, 2):
        pf(a, b)

def evalpairsmod(ilist, mod, f=f):
    from itertools import combinations
    def pf(x,y):
        print "f(%d,%d) = %d" % (x, y, f(x,y)%mod)
    isorted = sorted(ilist)
    for (b,a) in combinations(isorted, 2):
        pf(a, b)

def printtable(mod, inlist = None, f=f):
    if inlist == None: inlist = xrange(1,mod)
    for a in inlist:
        for b in inlist:
            print f(a,b)%mod,
        print

# list counterexamples to any 3 integers having a pair for which mod divides f(a,b)
def listcounterex(mod, f=f, maxexamples = 10, skipzero = True, nodups = True):
    count = 0
    if skipzero: start = 1
    else: start = 0
    if nodups: inc = 1
    else: inc = 0
    for a in xrange(start, mod):
        for b in xrange(a+inc, mod):
            for c in xrange(b+inc ,mod):
                ab = f(b,a)%mod
                ac = f(c,a)%mod
                bc = f(c,b)%mod
                if all([ab!=0, ac!=0, bc!=0]):
                    print a,b,c,":", ab, ac, bc
                    count += 1
                if count >= maxexamples:
                    return

# mod values for which there are no counterexamples: 1,2,3,4,5,6,8,10,12,15,24,30
# This list should be complete because the triple (1,2,3) produces the values f(2,1) = 6, f(3,1) = 24, and f(3,2) = 30. So (1,2,3) is a counterexample for any number which does not divide any of these three values. It just happens that there are no counterexamples for any of the divisors of 24 and 30. (And every output of f() is divisible by 6).

def minsetsize(mod, f=f):
    from itertools import combinations
    for size in xrange(2, mod):
        foundcountexample = False
        for s in combinations(range(1,mod), size):
            fp = [f(a,b)%mod for (b,a) in combinations(s,2)]
            nz = map(lambda x:x!=0, fp)
            if all(nz):
                print s, fp
                foundcountexample = True
                break
        if not foundcountexample:
            print size, "ints are sufficient"
            break

# every 4 ints are divisible by 7,14,16,21,42;
# every 5 ints are divisible by 9,18,20;
# every 6 ints are divisible by 11,22 (66?);
# every 7 ints are divisible by 13 (78?);
# every 9 ints are divisible by 17 (102?);
# every 10 ints are divisible by 19 (114?).
# every 12 ints are divisible by 23,25 (138?,150?).

# Two questions for further research:
# 1. For each positive n, What is the minimum number of arbitrary integers needed to guarantee that n divides f(a,b) for some pair a,b?
# 2. Answer question #1 for other symmetric functions.

# Table of minimum # ints for n|f(a,b)
# n   | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# -----------------------------------------------------------------------
# min | 2 2 2 3 3 2 4 3 5  3  6  3  7  4  3  4  9  5 10  5  4  6 12  3 12

def g(a,b):
    return (a**5)*b - a*(b**5)

# For g() above, 
# every pair is divisible by 1,2,3,5,6,10,15,30;
# every triple is divisible by 240;
# every 4 ints are divisible by 7,13,14,21 maybe 390?;
# every 5 ints are divisible by 9,17,18;
# every 6 ints are divisible by 11,22;
# every 7 ints are divisible by 25
# every 10 ints are divisible by 19.


# Table of minimum # ints for n|g(a,b)
# n   | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# -----------------------------------------------------------------------
# min | 2 2 2 3 2 2 4 3 5  2  6  3  4  4  2  3  5  5 10  3  4  6 12?  3  7

def sumsqrs(a,b):
    return a*a + b*b

def diffsqrs(a,b):
    return a*a - b*b
