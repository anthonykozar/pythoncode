# Sums of Squares
#
# Anthony Kozar
# Apr. 8, 2020

# make a list of sums of pairs of elements of arr (the pair can be the same element)
def pairwisesums(arr):
    out=[]
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            out.append(arr[i]+arr[j])
    return out

# make a list of products of pairs of elements of arr (the pair can be the same element)
def pairwiseproducts(arr):
    out=[]
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            out.append(arr[i]*arr[j])
    return out

# find all numbers up to MAX**2 that are the sum of two squares
MAX = 20
sqr = [n*n for n in xrange(1,MAX+1)]
sum2sqr = list(set(pairwisesums(sqr)))
sum2sqr.sort()
sum2sqr = filter(lambda (x): x<=MAX*MAX, sum2sqr)

print 'Sums of squares:'
print sum2sqr
print

# numbers that are either square or the sum of two squares
ss = list(set(sqr + sum2sqr))
ss.sort()

print 'Possible areas of squares:'
print ss
print

# Numbers that cannot be the area of square with vertices on a square lattice.
# See this video for explanation/inspiration:
# Impossible Squares - Numberphile
# https://www.youtube.com/watch?v=xyVl-tcB8pI
imposs = filter(lambda(x): x not in ss, xrange(1,401))

print 'Impossible areas of squares:'
print imposs
print
