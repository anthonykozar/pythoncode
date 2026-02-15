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

# find the size of the graph for n elements
'''
for n in xrange(2,8):
    d = derangements(n)
    e = graphcompatiblepairs(d)
    print n, len(d), len(e)
'''
# Results:
# n |V| |E|
# 2 1 0
# 3 2 1
# 4 9 12
# 5 44 276
# 6 265 10640
# 7 1854 536880
# The number of edges appears to be 1/2 of the values in OEIS A000186.
# https://oeis.org/A000186

# This graph can be used to make Latin squares by finding cliques of size n-1.
# Combining each such clique with the identity permutation provides a set of
# permutations that can be applied to any permutation of n elements to generate
# the rows of a Latin square!

# find the neighbors of vertex v
def neighbors(v, edges):
    adj = set()
    for v1,v2 in edges:
        if v1 == v: adj.add(v2)
        elif v2 == v: adj.add(v1)
    return adj

# count how many vertices there are of each degree
def countdegrees(vertices, edges):
    from collections import defaultdict
    degrees = defaultdict(int)
    for v1,v2 in edges:
        degrees[v1] += 1
        degrees[v2] += 1
    counts = defaultdict(int)
    for v in degrees:
        d = degrees[v]
        counts[d] += 1
    return counts

# count the occurrences of each degree for graphs with n elements
'''
print "n {degree: count,...}"
for n in xrange(2,8):
    d = derangements(n)
    e = graphcompatiblepairs(d)
    print n, dict(countdegrees(d,e))
'''
# Results:
# n {degree: count,...}
# 2 {}
# 3 {1: 2}
# 4 {2: 6, 4: 3}
# 5 {12: 20, 13: 24}
# 6 {80: 225, 82: 40}
# 7 {578: 420, 579: 720, 580: 714}

def isclique(cliquevertices, edges):
    vneighbors = []
    # make a list of the neighbors of each v in cliquevertices and add v to its list 
    for i, v in enumerate(cliquevertices):
        vneighbors.append(neighbors(v, edges))
        vneighbors[i].add(v)
    # test that vertices is a subset of each list
    return all([set(cliquevertices).issubset(vlist) for vlist in vneighbors])

def printclique(clique, vertices, edges, printidentity = False):
    if printidentity:
        permlen = len(vertices[0])
        print tuple(xrange(1, permlen+1))
    for v in clique:
        print vertices[v]

# find a single clique with size elements
def findclique(size, vertices, edges):
    # find a vertex with at least size-1 neighbors
    v = 0
    vadj = neighbors(v, edges)
    while v < len(vertices) and len(vadj) < size-1:
        v += 1
        vadj = neighbors(v, edges)
    if len(vadj) < size-1:
        # no suitable vertex found
        return None
    # see if v is part of a size-clique
    clique = set([v])
    #v2 = 
    #while len(clique) < size:
        
        # see how many neighbors

# find all size-cliques containing a particular vertex
# returns a list of sets
def findcliquesofv(v, size, edges):
    nv = neighbors(v, e)
    nbrsleft = set(nv)
    cliques = []
    while len(nbrsleft) > 0:
        candidate = set([v])
        shared = set(nbrsleft)
        vfirst = -1
        if len(candidate) + len(shared) < size:
            break
        while len(candidate) + len(shared) > size:
            v1 = shared.pop()
            if len(candidate) == 1:
                # remember first vertex so that we can remove it from nbrsleft
                vfirst = v1
            candidate.add(v1)
            shared = shared.intersection(neighbors(v1, edges))
        if len(candidate) + len(shared) == size:
            candidate.update(shared)
            foundclique = isclique(candidate, edges)
        else: foundclique = False
        if foundclique:
            cliques.append(candidate)
            nbrsleft.difference_update(candidate)
        else:
            if vfirst > -1:
                nbrsleft.remove(vfirst)
    return cliques

def convert2sortedtuples(listofcolls):
    listoflists = map(list, listofcolls)
    for l in listoflists:
        l.sort()
    return map(tuple, listoflists)

def sharedneighbors(v0, e):
    n0 = neighbors(v0, e)
    allshared = set()
    for v in n0:
        nv = neighbors(v, e)
        shared = n0.intersection(nv)
        allshared.update(shared)
    return allshared

# find the number of cliques of the required sizes for n elements

# cliques in n=5 derangement graph:
[[0, 16, 32, 36], [0, 17, 30, 37], [6, 12, 32, 36], [0, 18, 27, 43], [0, 19, 28, 41], [9, 11, 28, 41],
 [1, 14, 31, 39], [1, 15, 29, 38], [7, 11, 29, 38], [1, 20, 26, 40], [1, 21, 25, 42], [10, 13, 25, 42]]

