# NOTE: uses functions from factor.py
from factor import *

# predicate functions for use with filter()

def isodd(n): return (n%2)==1

def iseven(n): return (n%2)==0

def isprime(n): return len(pfactorlist(n)) == 1

def notprime(n): return len(pfactorlist(n)) > 1

def digitsum10plus(n): return sumdigits(n) >= 10

def primes2or5only(n):
    return reduce(boolAnd, map(lambda x: x in [2,5], pfactorlist(n)))

def digitsum4or13(n): return sumdigits(n) in [4,13]

# function makers that return predicates

def MakeCongruenceTest(modulus, congruencelist):
    return lambda n: (n%modulus) in congruencelist

def pfactorlimit(maxp):
    return lambda n: pfactormax(n) <= maxp

def allowed_pfactors(plist):
    def 
def between(low, high):
    return lambda n: n >= low and n <= high

# tests for known properties of n_1, n_2, and n_3

n1congr = MakeCongruenceTest(14, [1,7,9])
n2congr = MakeCongruenceTest(42, [16,22])
n3congr = MakeCongruenceTest(42, [4,10,34])
range1_2 = between(300, 649)

def n1p(n):
    return range1_2(n) and n1congr(n) and notprime(n) and digitsalldiff(n)

def n2p(n):
    return range1_2(n) and n2congr(n) and notprime(n)

def n3p(n):
    return n in [88, 160, 220, 256]

n1 = filter(n1p, range(1,650))
n2 = filter(n2p, range(1,650))
n3 = [88, 160, 220, 256]
