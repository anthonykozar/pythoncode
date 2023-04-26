# Prime Circles
# see <https://oeis.org/A051252>
# September 24, 2022

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# find all pairs of distinct elements in numlist that sum to an element in primelist
def findprimepairs(numlist, primelist = primes):
    pairs = []
    for i in xrange(len(numlist) - 1):
        for j in xrange(i+1, len(numlist)):
            if numlist[i] + numlist[j] in primelist:
                pairs.append((numlist[i], numlist[j]))
    return pairs

# return all sequences in "pairs" that contain n
def getpairswith(n, pairs):
	return filter(lambda p: n in p, pairs)

# find a cyclic arrangement of the numbers 1 to twoN (which must be even)
# such that every adjacent pair in the cycle sums to a prime number
def findprimecircle(twoN):
    circle = [1]
    last = 1
    pairs = findprimepairs(range(1,twoN+1))
    # following an algorithm suggested by Paul Boddington on OEIS
    while len(circle) < twoN:
        withlast = getpairswith(last, pairs)
        idx = len(withlast) - 1
        newval = 0
        # find the "largest" pair in withlast with a number not yet in circle
        while idx >= 0:
            p = withlast[idx]
            if p[0] == last:
                otherval = p[1]
            else: otherval = p[0]
            if not otherval in circle:
                newval = otherval
                break
            idx -= 1
        if newval > 0:
            circle.append(newval)
            last = newval
        else:
            print "No unused pairs for last!", circle, last
            return None
    # check that the list forms a cycle with the sum property
    if not (circle[0], circle[twoN-1]) in pairs:
        print "First and last values do not sum to a prime!", circle
        return None
    return circle
