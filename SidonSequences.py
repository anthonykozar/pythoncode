

def testnewelement(n, sidon, ssums):
    newsums = []
    for e in sidon:
        if e+n in ssums:
            return False
        else:
            newsums.append(e+n)
    return newsums

A = set([1,2])
sums = set([3])

for k in xrange(3, 101):
    newsums = testnewelement(k, A, sums)
    if newsums:
        A.add(k)
        sums = sums.union(newsums)

