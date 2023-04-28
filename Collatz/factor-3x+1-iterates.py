import sys
from findprimes import findprimes4
from factor import tryfactors

searchlimit = 10000000
numiterations = 100

sys.stderr.write('Searching for primes up to %d\n' % searchlimit)
primes = findprimes4(searchlimit, False, False)

sys.stderr.write('Calculating iterates of 3x+1\n')
coll = lambda x: 3*x + 1
y = 0
c = [0]
for i in xrange(numiterations):
    y = coll(y)
    c.append(y)

sys.stderr.write('Factoring iterates\n')
for i in xrange(1, len(c)):
    n = c[i]
    print "%d:" % i,
    tryfactors(n, primes)

# confirm that the nth iterate divides every
# k*nth iterate
sys.stderr.write('Checking divisibility of larger iterates by smaller ones\n')
for i in xrange(2, len(c)/2 + 1):
    x = c[i]
    divall = True
    for j in xrange(i, len(c), i):
        if c[j] % x != 0:
            divall = False
            print "c[%d]=%d does not divide c[%d]=%d" % (i, x, j, c[j])
    if divall: print "c[%d]=%d divides all c[%dk]" % (i, x, i)
