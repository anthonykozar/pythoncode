# See "Prime at the End of the Line (extra)"
# by Numberphile
# https://m.youtube.com/watch?v=u-_8wX4cECo
# and
# https://oeis.org/A376187

# Anthony Kozar
# April 10, 2026

from findprimes import findprimes4

primes = findprimes4(1000000, True, True)

maxslope = 0
maxpoints = 0

print "\nSlope #Pts Points"
# This code currently only looks for lines that pass through two consecutive primes.
# It can also miss earlier primes that lie on the same line.
for i in xrange(1000): # len(primes)-1):
    p = primes[i]
    d = primes[i+1]-primes[i]
    points = [(x+1,primes[x]) for x in xrange(i, len(primes)) if primes[x] == d*(x-i)+p]
    numpts = len(points)
    if numpts > 2:
        print d, numpts, points
        if d > maxslope: maxslope = d
        if numpts > maxpoints: maxpoints = numpts

print "\nMax slope:", maxslope
print "Max points:", maxpoints
