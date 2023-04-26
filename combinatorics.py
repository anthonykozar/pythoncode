def product(a, b):
    return a*b

def factorial(n):
    if (n == 0):
        return 1
    else:
        return reduce(product, range(1,n+1))

# number of permutations of r elements from a set with n elements
def P(n, r):
    return factorial(n) / factorial(n-r)

# number of combinations of r elements from a set with n elements
def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def binomialcoeff(degree):
    return [C(degree,r) for r in range(0,degree+1)]

# number of combinations with replacement
def CReplace(n, r):
    return C(n+r-1, r)

# integer partitions of N
partitions1 = [[1]]
partitions2 = [[2], [1,1]]
partitions3 = [[3], [2,1], [1,1,1]]
partitions4 = [[4], [3,1], [2,2], [2,1,1], [1,1,1,1]]
partitions5 = [[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]]

# convert partitions to tuples (a,b,c,d,...) where a is the # of 1's,
# b is the # of 2's, c is the # of 3's, etc.
