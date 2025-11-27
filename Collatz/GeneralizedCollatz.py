# Code for exploring patterns of generalized Collatz-like functions
#
# Anthony Kozar
# Nov. 22, 2025

def collatz(n):
    if (n%2) == 0:
        return n/2
    else:
        return 3*n+1

def f5xp1(n):
    if (n%2) == 0:
        return n/2
    else:
        return 5*n+1

# Print the sequence of numbers derived from iteratively applying
# collfunc to n until it reaches 1 or exceeds maxnum.
# Will loop forever if a small cycle is found!
def printhailstoneseq(n, collfunc = collatz, maxnum = 10**12):
    num = n
    while num != 1 and num < maxnum:
        print num, '->',
        num = collfunc(num)
    if num == 1: print '1'
    else:
        print

# Make a graph of an iterated function for inputs in range(a, b+1, step), optionally printing hailstone sequences until they reach a known part of the graph (or exceed maxnum).
def makegraph(a, b, step, collfunc, printhailstones = True, maxnum = 10**12):
    def extendgraph(n, graph):
        num = n
        while not num in graph and num < maxnum:
            if printhailstones:
                print num, '->',
            fnum = collfunc(num)
            graph[num] = fnum
            num = fnum
        if printhailstones:
            if num in graph: print num, '-> *'
            else:
                print '...'
    
    graph = dict()
    for n in xrange(a, b+1, step):
        extendgraph(n, graph)
    return graph
