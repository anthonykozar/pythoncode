# Sums of 3 Cubes

# Anthony Kozar
# April 18, 2026

from itertools import combinations_with_replacement
from collections import defaultdict

# find postive integer solutions to a^3 + b^3 + c^3 = d^3
cubes = [n**3 for n in xrange(101)]
quads = defaultdict(list)
for c in combinations_with_replacement(xrange(1,101), 3):
    csum = cubes[c[0]] + cubes[c[1]] + cubes[c[2]]
    if csum in cubes:
        cubidx = cubes.index(csum)
        quads[cubidx].append(c)

for n in quads:
    print n, quads[n]

# find natural numbers that can be represented as 
# the sum of 3 non-negative cubes
ccc = [cubes[c[0]] + cubes[c[1]] + cubes[c[2]] for c in combinations_with_replacement(xrange(17), 3)]
ccc.sort()

# numbers with two or more representations
last = -1
dups = []
for n in ccc:
    if n == last: dups.append(n)
    last = n
