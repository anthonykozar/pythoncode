# From <https://rosettacode.org/wiki/Permutations/Derangements#Python>

from itertools import permutations
import math

def derangements_from_0(n):
    'All deranged permutations of the integers 0..n-1 inclusive'
    return [ perm for perm in permutations(range(n))
             if all(indx != p for indx, p in enumerate(perm)) ]

def derangements(n):
    'All deranged permutations of the integers 1..n inclusive'
    from itertools import permutations
    import math
    return [ perm for perm in permutations(range(1, n+1)) if all(indx+1 != p for indx, p in enumerate(perm)) ]

# An application to Latin square generation

# make a graph with the derangements of n as vertices and
# edges connecting pairs that do not have the same value in the same position (column).
def graphcompatiblepairs(vertices):
    edges = []
    for i in xrange(len(vertices)):
        p1 = vertices[i]
        for j in xrange(i, len(vertices)):
            p2 = vertices[j]
            if all([p1[k] != p2[k] for k in xrange(len(p1))]):
                edges.append((i,j))
    return edges

# This graph can be used to make Latin squares by finding cliques of size n-1.  Combining each such clique with the identity permutation provides a set of permutationsthat can be applied to any permutation of n elements to generate the rows of a Latin square!

# find the number of cliques of the required sizes for n elements

# find the size of the graph for n elements
'''for n in xrange(2,10):
    d = derangements(n)
    e = graphcompatiblepairs(d)
    print n, len(d), len(e)
'''

def neighbors(n, edges):
    adj = set()
    for a,b in edges:
        if a == n: adj.add(b)
        elif b == n: adj.add(a)
    return adj
