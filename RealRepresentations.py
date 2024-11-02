# Representations of Real Numbers
# Oct. 6, 2024

def encode(x, finv):
    digits = []
    while len(digits) < 20:
        ix = int(x)
        digits.append(ix)
        x = finv(x-ix)
    return digits

def decode(seq, f):
    x = 0
    for i in xrange(len(seq)-1, -1, -1):
        x = seq[i] + f(x)
    return x

dec = lambda x: x/10.0
decinv = lambda x: 10.0*x

'''
from math import *
encode(pi, decinv)
'''

# map the interval [0,10] to [0,1] with an exponential curve
# scexp = lambda x: expm1(x*(log(2.0)/10.0))
def scexp(x, expm1=expm1, log=log):
    return expm1(x*(log(2.0)/10.0))

