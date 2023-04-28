# Euler Products & Dirichlet Series
# https://en.m.wikipedia.org/wiki/Euler_product
# https://en.m.wikipedia.org/wiki/Dirichlet_series

import math

plist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

# Approximate one term of the Euler product for the Zeta function, i.e. Sum_k(1/p^ks) for k = 0 to infinity
def zetaterm(p, s, numterms = 20, printpartialsums = False, pow = math.pow):
    pinv = 1.0 / pow(p,s)
    total = 0.0
    pkinv = 1.0
    for k in xrange(numterms):
        total += pkinv
        if printpartialsums:
            print pkinv, total
        pkinv *= pinv
    return total

def eulerproduct(s, primes, termfunc, numterms= 20):
    prod = 1.0
    for p in primes:
        prod *= termfunc(p, s, numterms)
    return prod

# approximate zeta function values
# for zeta(2), zeta(4), and zeta(8)
# and show error from true values
z2 = eulerproduct(2, plist, zetaterm)
print z2, math.pi**2/6 - z2
z4 = eulerproduct(4, plist, zetaterm)
print z4, math.pi**4/90 - z4
z8 = eulerproduct(8, plist, zetaterm)
print z8, math.pi**8/9450 - z8
