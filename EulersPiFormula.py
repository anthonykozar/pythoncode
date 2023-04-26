# Check Euler's formula for pi

# This sequence (due to Euler) converges to pi but VERY slowly:

#           5   7   11   13   17   19   23   29   31
#  pi = 3 * - * - * -- * -- * -- * -- * -- * -- * -- * ...
#           4   8   12   12   16   20   24   28   32

# The numerators are primes starting with 3.
# The denominators are closest multiple of 4 to the numerator.
# The formula was expressed on Wikipedia as pi/4 = 3/4 + 5/4 + ...

# Calculating terms with primes up to 100,000, the only sure
# digits are 3.14 and the product has been hovering around 3.1425
# for a while.  Is there a mistake in my code?

# See this Wikipedia article for an explanation of how this sequence
# can be used to prove that there are infinite primes.
# http://en.wikipedia.org/wiki/Infinitude_of_the_prime_numbers#Proof_using_the_irrationality_of_.CF.80

factorfound = False
piproduct = 3.0
primes = [2,3]
# test all odd numbers for primeness
for n in range(5,100000,2):
    # show our progress from time to time
    if (n-1) % 1000 == 0:
        print n,
        print ":"
    # divide by each prime found so far
    for p in primes:
        if n % p == 0:
            factorfound = True
    if factorfound == False:
        # n is prime, so add it to our list
        primes += [n]
        # multiply by this prime
        piproduct = piproduct * n
        # and divide by the closest multiple of four
        # (which is always one less or one more than an odd number)
        if (n-1) % 4 == 0:
            piproduct = piproduct / (n-1)
        else:
            piproduct = piproduct / (n+1)
        # print the result so far
        print piproduct
    factorfound = False
