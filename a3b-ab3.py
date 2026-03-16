# Prove that given any three integers, 
# there is a pair (a,b) among them such that
# (a**3)*b - a*(b**3) is divisible by 10.

# This problem came from a YouTube video and
# suggested other interesting questions to me. 
# Anthony Kozar
# March 15-16, 2026

def f(a,b):
    return (a**3)*b - a*(b**3)

def evalpairs(a,b,c, f=f):
    def pf(x,y):
        print "f(%d,%d) = %d" % (x, y, f(x,y))
    abc = [a,b,c]
    abc.sort()
    pf(abc[1], abc[0])
    pf(abc[2], abc[0])
    pf(abc[2], abc[1])

def printtable(mod, f=f):
    for a in xrange(1,mod):
        for b in xrange(1,mod):
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

# Two questions for further research:
# 1. For each positive n, What is the minimum number of arbitrary integers needed to guarantee that n divides f(a,b) for some pair a,b?
# 2. Answer question #1 for other symmetric functions.
