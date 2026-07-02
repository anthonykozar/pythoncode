# June 9, 2026

from SumsDivisors import sumofpowers, sumdivsfromprimes
import itertools
import operator as op

it = itertools.product([1], [0,2,4,6], [0,2,4], [0,2])
for exps in it:
    factors = zip([5,3,7,11], exps)
    n = reduce(op.mul, ([p**e for p,e in factors]))
    sum1 = sumdivsfromprimes(factors)
    print exps, n, sum1, sum1/2

# examine congruence classes of divisor sums of p^n to see which congruence classes of primes mod 6 or 30 might work as chains of prime factors in an odd perfect number
gcd1mod6 = [1,5]
gcd1mod30 = [1,7,11,13,17,19,23,29]

print "p(mod 6)  1  5"
for n in xrange(1, 21):
    print "sig(p^%d)  %d  %d" % (n, sumofpowers(7,n)%6, sumofpowers(5,n)%6)

print
print "p(mod 30)",
for a in gcd1mod30: print "%2d" % a,
print
for n in xrange(1, 30):
    print "%-9s" % "sig(p^%d)" % n,
    for a in gcd1mod30: print "%2d" % (sumofpowers(a,n)%30),
    print
