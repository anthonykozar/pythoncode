# primelist must contain all primes less than num for this to work
# (or at least less than sqrt(num))
def pfactorwithplist(num, primelist):
    factors = []
    for p in primelist:
        while num % p == 0:
            factors.append(p)
            num = num / p
    if len(factors) == 0 and num > 1:
        # num is prime
        factors.append(num)
    return factors

def CountNumsWithLessThanFourPrimeFactors(uptoMax):
    hascount = 0
    notcount = 0
    primes = []
    for i in range(1,uptoMax+1):
            factors = pfactorwithplist(i, primes)
            if len(factors) > 3:
                    notcount += 1
            else:
                    hascount += 1
            if len(factors) == 1:
                primes.append(i)
            # print i, ":", (len(factors) > 3), ":", factors
    print "HAS:", hascount
    print "NOT:", notcount
