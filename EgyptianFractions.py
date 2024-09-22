# Egyptian Fractions
#
# Functions to work with rational numbers expressed as the sum of (distinct) unit fractions (1/n).
#
# Anthony Kozar
# circa Nov. 23, 2022
# Sept. 19, 2024

import fractions

# Egyptian fraction representations (EFRs) will be stored as a list of the denominators.
# E.g. [2,3,6] means 1/2 + 1/3 + 1/6

# Calculate the sum of an EFR
def egyptiansum(denoms, frac = fractions.Fraction):
    return sum(map(lambda d: frac(1,d), denoms))

# Find an EFR for the rational a/b using the "greedy" algorithm 
def greedy(a, b, frac = fractions.Fraction):
    r = frac(a,b)
    denoms = []
    while r.numerator > 1:
        d = r.denominator // r.numerator + 1
        denoms.append(d)
        r -= frac(1,d)
    if r.numerator == 1:
        denoms.append(r.denominator)
    else:
        print "r =", r
    return denoms

def greedy1(a, b):
    d = b // a + 1
    print d
    a = a*d - b
    b *= d
    return (a,b)

''' Examples
for d in xrange(2,21):
    print "4/%d" % d, greedy(4, d)

for d in xrange(3,41,2):
    denoms = greedy(4, d)
    print "4/%d" % d, denoms, egyptiansum(denoms)
'''

from SumsDivisors import *

# Find an EFR for the rational a/b using a practical number that is a multiple of b
def usepractical(a, b, frac = fractions.Fraction, findpracticalmultiple = findpracticalmultiple):
    d = findpracticalmultiple(b)
    divs = divisors(d)
    numerators = findsublistwithsum(divs, a*(d/b))
    if numerators:
        denoms = []
        for n in numerators:
            r = frac(n,d)
            print n, d, r
            if r.numerator == 1:
                denoms.append(r.denominator)
            else:
                print "r =", r
        denoms.reverse()
        return denoms
    else:
        print "Warning: findsublistwithsum(divisors(%d),%d) did not return anything in usepractical(%d,%d)." % (d, a*(d/b), a, b)
        return None
