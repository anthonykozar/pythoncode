# The Sum and Product Puzzle (a.k.a. the Impossible Puzzle)
# See https://en.m.wikipedia.org/wiki/Sum_and_Product_Puzzle
#
# Anthony Kozar
# November 10, 2024

# Observations:
#    0. 5 <= X+Y <= 100, 6 <= XY <= 2499
#    1. Y>X>1 implies XY cannot be prime or the square of a prime. 
#    2. For S to know "P does not know X and Y.", ALL of the corresponding products of X+Y must be able to be factored in more than one way.
#    3. #2 implies that XY must have 6 or more divisors which implies XY cannot be semiprime or the cube or fourth power of a prime.

# Return a list of all of the products XY whose corresponding sum X+Y is summ,
# excluding X=1 and X=Y.
def productsWithSum(summ):
    return [n*(summ-n) for n in xrange(2,(summ+1)/2)]

from collections import defaultdict
prodcounts = defaultdict(int)
productsbysum = dict()
sumsbyproduct = defaultdict(list)

# Create maps between all possible sums and their corresponding products. Count the number of occurrences of each product.
for s in xrange(5,101):
    prs = productsWithSum(s)
    productsbysum[s] = prs
    for n in prs:
        prodcounts[n] += 1
        sumsbyproduct[n].append(s)

# Find the products that occur more than once.
# These are the products that satisfy observation #3.
# This doesn't work in Pyonic: 
# prodmoreonce = filter(lambda k: prodcounts[k] > 1, prodcounts.keys())
prodmoreonce = [k for k in prodcounts.keys() if prodcounts[k] > 1]
prodmoreonce = frozenset(prodmoreonce)

# Find sums with only one product in prodmoreonce.
'''
singleprodsums = []
for s,prs in productsbysum.iteritems():
    prset = set(prs)
    if len(prset.intersection(prodmoreonce)) == 1:
        singleprodsums.append(s)

for s in singleprodsums:
    print s, productsbysum[s]
'''

# Find sums with all products in prodmoreonce.
allprodsums = []
for s,prs in productsbysum.iteritems():
    prset = set(prs)
    if prset.intersection(prodmoreonce) == prset:
        allprodsums.append(s)

'''
for s in allprodsums:
    print s, productsbysum[s]
'''

'''
prodcounts2 = defaultdict(int)
for s in allprodsums:
    for n in productsbysum[s]:
        prodcounts2[n] += 1
a = [n for n in prodcounts2.keys() if prodcounts2[n]==1 and prodcounts[n]>1]
'''

# Count the occurrences of val in seq
def count(val, seq):
    isval = lambda x: int(x == val)
    return sum(map(isval, seq))

# Count the number of sums for product p that can't be ruled out after S says "P does not know X and Y."
def countpossiblesums(p, count = count,  prodcounts = prodcounts, productsbysum = productsbysum, sumsbyproduct = sumsbyproduct):
    return count(True, [not 1 in [prodcounts[p2] for p2 in productsbysum[s]] for s in sumsbyproduct[p]])

# Find sums for which S can determine X and Y after P says "Now I know X and Y."
for s in allprodsums:
    scounts = [countpossiblesums(p) for p in productsbysum[s]]
    if count(1, scounts) == 1:
        print s, productsbysum[s], scounts

# That produces a single solution!
# X+Y=17, XY=52
# X=4, Y=13

# Verify the solution
print "S knows that X+Y=17. The corresponding products are"
print productsbysum[17]
print "S sees that each of these products has multiple non-trivial factor pairs, so P is unable to deduce X and Y."
print "Number of factor pairs:"
print [prodcounts[p] for p in productsbysum[17]]
print
print "P knows that XY=52 and checks each corresponding sum and finds that only 17 has no products with a single non-trivial factor pair. P concludes that X+Y=17, X=4, and Y=13."
for s in sumsbyproduct[52]:
    print s, productsbysum[s]
print "Number of factor pairs:"
for s in sumsbyproduct[52]:
    print s, [prodcounts[p] for p in productsbysum[s]]
print
print "S performs the same analysis for each of the corresponding products of 17 and finds that only 52 has a single corresponding sum that could allow P to deduce X and Y."
print [countpossiblesums(p) for p in productsbysum[17]]
