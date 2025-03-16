# factor.py

# Crude functions for finding the prime factorization of an integer, 
# checking if a number is prime, finding the next prime, etc.

import math
import operator

def pfactor(num):
    limit = int(math.sqrt(num))
    for p in xrange(2,limit+1):
        if num < 2:
            break
        while num % p == 0:
            print p,
            num = num / p
    if num > 1:
        print num
    else:
        print

def pfactorlist(num):
    limit = int(math.sqrt(num))
    factors = []
    for p in xrange(2,limit+1):
        if num < 2:
            break
        while num % p == 0:
            factors.append(p)
            num = num / p
    if num > 1:
        factors.append(num)
    return factors

# Use printfactors() with map():
#    map(printfactors, haslist)
def printfactors(num):
    print str(num)+": ",
    pfactor(num)

def pfactormax(n):
    return max(pfactorlist(n))

def tryfactors(num, factors):
    for p in factors:
        if num < 2:
            break
        while num % p == 0:
            print p,
            num = num / p
    if num != 1:
        print num, '**'
    else: print

def isprime(n): return len(pfactorlist(n)) == 1

def notprime(n): return len(pfactorlist(n)) > 1

# return the next prime greater than num
def nextprime(num):
    start = num + 1 + num%2  # start with an odd number
    for n in xrange(start, 2*start, 2):
        if isprime(n):
            return n

# Interesting number sequences for factoring
repunits = [(10**n - 1)/9 for n in xrange(2,25)]

# for i in xrange(len(repunits)):
#     for j in xrange(i-1):
#         if (repunits[i] % repunits[j]) == 0:
#             print repunits[i], "=", repunits[j], "*", repunits[i]/repunits[j]

mersenne = [2**n - 1 for n in xrange(2,64)]
dblmersenne = [2**(2**n) - 1 for n in xrange(1,9)]
fermat = [2**(2**n) + 1 for n in xrange(0,8)]

# The factors of the nth dblmersenne number are the first n fermat numbers!!
# for f in dblmersenne:
#     print f, ":",
#     tryfactors(f, fermat)

def intersect(setA, setB):
    return filter(lambda x: x in setB, setA)

def factorsum(num):
    return reduce(operator.add, pfactorlist(num))

def printfactorsum(num):
    factors = pfactorlist(num)
    print num, factors, reduce(operator.add, factors)

def pfactorstr(num):
    factors = ""
    for p in xrange(2,num):
        if num < 2:
            break
        while num % p == 0:
            factors += str(p) + " "
            num = num / p
    return factors
