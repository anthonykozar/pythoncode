# Affinely Self-Generating Sets

# Found this Olympiad problem on YouTube:
# 2021 is "fantabulous".  If any of 
# {m, 2m+1, 3m} are fantabulous, then the
# other two are also. Is 2021^2021 fantabulous?

# Generating numbers with f(n)=2n+1 and 
# g(n)=3n, starting with f(1) and g(1)
# led me to sequences A190811 and A190803
# and to papers like 
# David Garth and Adam Gouge. Affinely Self-Generating Sets and Morphisms. Journal of Integer Sequences, Vol. 10 (2007), 1-13.

# Anthony Kozar
# April 27, 2026

# Generate a set of integers by repeatedly
# applying the functions in list funcs to
# the starting values.
def genset(funcs, startvals = [1], setsize = 100, maxval = 10**100):
    # insertions = 0
    queue = startvals
    s = set(queue)
    while len(s) < setsize and len(queue) > 0:
        n = queue[0]
        queue = queue[1:]
        for f in funcs:
            m = f(n)
            if type(m) == int and (not m in s) and m <= maxval:
                queue.append(m)
                s.add(m)
                # insertions += 1
    # print insertions, "insertions"
    return s

# Make a new affine (linear) function
def affinefunc(slope, yintercept):
    return lambda n: slope*n + yintercept

# Make a new inverse affine function that only returns integers or None for no solution.
def invaffinefunc(slope, yintercept):
    def inversefunc(n):
        m = n - yintercept
        q,r = divmod(m, slope)
        if r == 0:
            return q
        else:
            return None
    return inversefunc

# functions for the Olympiad problem
fantabulous = [affinefunc(2,1), affinefunc(3,0), invaffinefunc(2,1), invaffinefunc(3,0)]

a = sorted(genset(fantabulous, [2021], 2000))
i = a.index(2021)
a[:i+1]

# Generate a graph of an affinely self- 
# generating set with the members of the set 
# as vertices and an edge (a,b) whenever 
# f(a) = b for some f in funcs.
def gengraph(funcs, startvals = [1], setsize = 100, maxval = 10**100, stopon = None, directed = False):
    from collections import defaultdict
    # insertions = 0
    queue = startvals
    g = defaultdict(list)
    while len(g) < setsize and len(queue) > 0:
        n = queue[0]
        queue = queue[1:]
        for f in funcs:
            m = f(n)
            if type(m) == int and m <= maxval:
                if not m in g:
                    queue.append(m)
                    g[m] # create g[m]
                if not m in g[n]:
                    g[n].append(m)
                if not directed and not n in g[m]:
                    g[m].append(n)
                # insertions += 1
        if n == stopon: break
    # print insertions, "insertions"
    return g
