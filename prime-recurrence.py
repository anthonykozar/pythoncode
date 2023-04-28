# "A natural prime-generating recurrence"
# by Eric S. Rowland
# https://arxiv.org/abs/0710.3217
# https://en.m.wikipedia.org/wiki/Formula_for_primes

from fractions import gcd

f = open('/storage/emulated/0/Documents/python/prime-recurrence.out', 'w')
acc = 7
for n in xrange(2,10000000):
    d = gcd(n, acc)
    if d > 1:
        f.write("%-7d  %-8d  %d\n" % (n, acc, d))
    acc += d
f.close()
