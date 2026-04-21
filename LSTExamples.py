# LST examples

from SequenceTransforms import LSieveTransform

print "(L)-sieve transform of arithmetic progressions"
print "Start Step LST"
ap = range(1, 500, 2) # 2^n-1 A000225
print 1, 2, LSieveTransform(ap)
ap = range(2, 500, 2) # 2^n A000079
print 2, 2, LSieveTransform(ap)
print
ap = range(1, 500, 3) # A152009
print 1, 3, LSieveTransform(ap)
ap = range(2, 500, 3) # A006999
print 2, 3, LSieveTransform(ap)
ap = range(3, 500, 3) # A061419
print 3, 3, LSieveTransform(ap)
print
# ap = range(3, 500, 4) # A155167
# print 3, 4, LSieveTransform(ap)

for start in xrange(1,6):
    ap = range(start, 500, 4)
    print start, 4, LSieveTransform(ap)
print

# The LST of the triangular numbers is the triangular numbers.
tri = [sum(range(1,n+1)) for n in xrange(1,21)]
LSieveTransform(tri) == tri

# The LST of the squares gives sequence A154287 containing the squares of 
# 1,3,7,15... at indices 2^(n+1) - n - 2 (A125128).
sqrs = [n**2 for n in xrange(1,130)]
lst = LSieveTransform(sqrs)
lstsqrs = sorted(list(set(sqrs).intersection(set(lst))))
[lst.index(sq)+1 for sq in lstsqrs]
