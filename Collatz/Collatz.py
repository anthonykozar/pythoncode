# Code for exploring patterns of the Collatz conjecture
# <https://en.wikipedia.org/wiki/Collatz_conjecture>
# Nov. 9, 2017

# The basic function
def collatz(n):
    if (n%2) == 0:
        return n/2
    else:
        return 3*n+1

# Print the sequence of numbers derived from iteratively applying
# the Collatz function to n until it reaches 1.
def printhailstoneseq(n):
    num = n
    while num != 1:
        print num, '->',
        num = collatz(num)
    print '1'

# Shortcut function that returns the next odd number in the sequence from n.
def nextodd(n):
    num = collatz(n)
    while (num%2) == 0:
        num = collatz(num)
    return num

def printmap(func, seq):
    for i in seq:
        print i, '->', func(i)

# Check that numbers of the form (2^(2n)-1)/3 have nextodd==1
goto1 = [(2**(2*n)-1)/3 for n in range(1,100)]
printmap(nextodd, goto1)
