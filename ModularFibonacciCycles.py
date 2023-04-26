# Modular Fibonacci Cycles

# When the Fibonacci recurrence relation (F(n) = F(n-1) + F(n-2)) is computed
# with modular arithmetic, the result is a number of cyclic sequences.  I
# started investigating this because of a recently completed Zendo game that
# I ran (SDG #29845) with the rule:
#
#   [Koans are positive integers of at least three digits]
#   Each digit after the second is the sum (mod 10) of the two previous
#   digits.  Eg.  12358314 HTBN because 1+2=3, 2+3=5, 3+5=8, 5+8=3(mod 10),
#   8+3=1(mod 10), and 3+1=4.
#
# A generalization of this rule would be
#
#   Each digit after the second [within the base N representation of the
#   koan] is the sum (mod K) of the two previous digits.
#
# The function below calculates all of the cycles for particular combinations
# of base and modulus.

# See also https://en.wikipedia.org/wiki/Pisano_period

# Anthony Kozar
# June 13, 2016

# All possible starting pairs (i, j) with 0 <= i,j < base are checked and if
# the pair is not part of a previously computed cycle, a new cycle is begun and
# printed.  The modulus can be any natural number up to base and is set equal
# to base if omitted.
def PrintFibonacciModCycles(base, modulus = 0, printcommas = True):
    if modulus == 0:
        modulus = base
    if modulus > base:
        print "Error: modulus must be less than or equal to base"
        return

    # create an array with base-squared elements initialized to False
    checkedpairs = [False] * base * base

    for i in range(base):
        for j in range(base):
            idx = i * base + j
            if not checkedpairs[idx]:
                # start a new sequence
                digit1 = i
                digit2 = j
                if printcommas:
                    print str(digit1) + ', ' + str(digit2) + ',',
                else:
                    print digit1, digit2,
                looping = False
                while not looping:
                    if checkedpairs[idx]:
                        # this pair has already occurred in some (this?) sequence
                        # so we are looping
                        print "..."
                        looping = True
                    else:
                        # mark this pair as checked
                        checkedpairs[idx] = True
                        # print next digit in this sequence
                        nextdigit = (digit1+digit2) % modulus
                        if printcommas:
                            print str(nextdigit) + ',',
                        else:
                            print nextdigit,
                        # update for next pair
                        digit1 = digit2
                        digit2 = nextdigit
                        idx = digit1 * base + digit2
