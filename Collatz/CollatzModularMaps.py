# Maps of generalized Collatz functions modulo N
from collections import defaultdict

coll = lambda x: 3*x + 1

def makemap(func, mod):
    m = {}
    for i in range(mod):
        m[i] = func(i) % mod
    return m

# This is a useful piece of code but only works if fmap is bijective.
# Could be generalized by allowing fmap to be a collection or a callable and replacing mod with an iterable "domain".
def findcycles(fmap, mod):
    cycles = []
    used = set()
    start = 0
    while start < mod:
        # start a new cycle
        curcycle = []
        curcycle.append(start)
        used.add(start)
        # iterate fmap to find cycle
        next = fmap[start]
        while next != start:
            curcycle.append(next)
            used.add(next)
            next = fmap[next]
        cycles.append(curcycle)
        # find the smallest unused value
        while start in used: start += 1
    return cycles

filepath = "/sdcard/Documents/python/"
writefiles = True

# prime moduli (except for 3) seem to make bijective maps for 3x+1
primes = [2]
for n in xrange(3, 10000, 2):
    isprime = True
    for p in primes:
        isprime = isprime and (n%p != 0)
    if isprime: primes.append(n)

# all cycles for prime moduli
cycles = {}
for p in primes[2:]:  # skip 2 and 3
    cycles[p] = findcycles(makemap(coll, p), p)

if writefiles:
    fout = open(filepath + "3x+1modp-cycles.txt", 'w')
    for p in primes[2:]:
        fout.write("%d %s\n" % (p, cycles[p]))
    fout.close()

# lengths of all cycles for prime moduli
allcyclens = {}
for p in primes[2:]:  # skip 2 and 3
    allcyclens[p] = map(len, cycles[p])

if writefiles:
    fout = open(filepath + "3x+1modp-cycle-lengths.txt", 'w')
    for p in primes[2:]:
        fout.write("%d %s\n" % (p, allcyclens[p]))
    fout.close()

# every prime moduli appears to produce cycles of two lengths: one cycle of length 1 (the fixed point floor(p/2)) and one or more cycles of a second length k that divides p-1. There are (p-1)/k of these length k cycles.
# the length of the "long" cycles and their multiplicity for each prime moduli
cyclenmultiplicity = {}
for p in primes[2:]:  # skip 2 and 3
    longlen = allcyclens[p][0]
    multiplicity = allcyclens[p].count(longlen)
    cyclenmultiplicity[p] = (longlen, multiplicity)
    if longlen * multiplicity != p - 1:
        print "Cycle length * multiplicity != p-1 for p=%d" % p

if writefiles:
    fout = open(filepath + "3x+1modp-cycle-multiplicities.txt", 'w')
    fout.write("p length multiplicity\n")
    for p in primes[2:]:
        fout.write("%d\t%d\t%d\n" % (p, cyclenmultiplicity[p][0], cyclenmultiplicity[p][1]))
    fout.close()

# build an inverse map from each cycle length to its prime moduli
cyclentop = defaultdict(list)
for p in primes[2:]:  # skip 2 and 3
    cyclentop[cyclenmultiplicity[p][0]].append(p)

if writefiles:
    fout = open(filepath + "3x+1modp-length-to-p.txt", 'w')
    lengths = cyclentop.keys()
    lengths.sort()
    for k in lengths:
        fout.write("%d %s\n" % (k, cyclentop[k]))
    fout.close()

# build an inverse map from each multiplicity value to its prime moduli
multiplicitytop = defaultdict(list)
for p in primes[2:]:  # skip 2 and 3
    multiplicitytop[cyclenmultiplicity[p][1]].append(p)

if writefiles:
    fout = open(filepath + "3x+1modp-multiplicity-to-p.txt", 'w')
    mults = multiplicitytop.keys()
    mults.sort()
    for k in mults:
        fout.write("%d %s\n" % (k, multiplicitytop[k]))
    fout.close()

########
primes = findprimes4(10000000, True, True)

y = 1
c = []
for i in xrange(50):
    y = coll(y)
    c.append(y)

for n in c:
    print "%d: " % n,
    tryfactors(n, primes)
