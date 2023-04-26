# Zendo #36257
#
# AKHTBN iff its digits appear in order as consecutive digits within the
# first 51 digits of PI (3 + 50 digits after the decimal point).

pi = "314159265358979323846264338327950288419716939937510"

# Count how many numbers of length 'digits' are substrings of pi.
def countsubstrpi(digits, echo = False):
    count = 0
    for n in xrange(10**(digits-1), 10**digits):
        if str(n) in pi:
            if echo: print n
            count += 1
    return count

print [countsubstrpi(n) for n in xrange(1,8)]
