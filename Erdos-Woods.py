# Erdős-Woods numbers
#
# See https://en.m.wikipedia.org/w/index.php?title=Erd%C5%91s%E2%80%93Woods_number
# and this Numberphile video:
#     https://m.youtube.com/watch?v=uJtxlErlx0U
#
# Anthony Kozar
# Sept. 26, 2024

# Definition from Wikipedia:
# "A positive integer k is said to be an Erdős–Woods number if it has the following property: there exists a positive integer a such that in the sequence (a, a + 1, …, a + k) of consecutive integers, each of the elements has a non-trivial common factor with one of the endpoints."

# Some observations:
# 1. With k=1, every pair of consecutive numbers trivially has the EW property.
# 2. gcd(n,n+1) = 1 for all positive integers n, therefore 
#   a. k=2 is not an Erdős-Woods number because a+1 cannot share any factors with either endpoint; and
#   b. for k>2, a+1 can only share a factor with a+k and a+(k-1) can only share a factor with a.
# 3. 

# print 
def fwdrev(n):
    for i in xrange(n+1):
        print "%2d" % i,
    print
    for j in xrange(n, -1, -1):
        print "%2d" % j,
    print

for n in xrange(8,16):
    fwdrev(n)
    print
