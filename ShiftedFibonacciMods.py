# Fibonacci sequence modded with a shifted copy of itself
#
# This code implements an idea Bea had to take each number
# in the Fibonacci sequence modulo the ith previous number
# in the sequence.  For example, if i=2 then we have
#
# F(n)     1  1  2  3  5  8 13 21 34 55 89 ...
# modulus        1  1  2  3  5  8 13 21 34 ...
# result         0  0  1  2  3  5  8 13 21 ...
#
# Anthony Kozar
# Sept. 24, 2024

# Make a list of the first 'length' Fibonacci numbers.
def FibonacciSequence(length):
    fibseq = [1,1]
    idx = 0
    while idx < length - 2:
        fi = fibseq[idx] + fibseq[idx+1]
        fibseq.append(fi)
        idx += 1
    return fibseq

SEQLEN = 30

FibonacciNums = FibonacciSequence(SEQLEN)

# i is the number of places earlier in the sequence to
# look for the modulus.
for i in xrange(1, SEQLEN/2):
    print "F(n) mod F(n-%d) starting with F(%d):" % (i, i+1)
    # Start with the (i+1)-th member of sequence so that the
    # ith previous member exists. (Python lists are indexed
    # from 0 so j ranges from i to the end of the list
    # FibonacciNums).
    for j in xrange(i, len(FibonacciNums)):
        print FibonacciNums[j] % FibonacciNums[j-i],
    print
    print


# i = 1,2,3 produces the Fibonnaci sequence after some initial
# zeros (and only a single 1 for 1 & 2).  i = 5,7,9,11,... also
# appear eventually to produce the Fibonnaci sequence after
# some other initial values. i = 4,6,8,10,... appear to produce
# other sequences using the Fibonnaci rule/recurrence after some
# initial values.  This needs further checking and investigation!
