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

def f3xp5(n):
    if (n%2) == 0:
        return n/2
    else:
        return 3*n+5

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

# Classifications for cycle analysis:
partOfCycle = 1
leadsToCycle = 2
possiblyDivergent = 3

# Returns two objects, the first being a list of lists containing the numbers for each cycle in graph. 
# The second object is a new dictionary associating with each key n in graph a 3-tuple 
# (class of n, the cycle in which n appears or to which it leads or None, the index of n in the cycle or None).
def analyzegraph(graph):
    # workaround for bug in Pyonic
    partOfCycle = 1
    leadsToCycle = 2
    possiblyDivergent = 3
    
    classes = dict()
    cycles = []
    notcyclic = []
    def cycleidx(m):
        for i in xrange(len(cycles)):
            if m in cycles[i]:
                idx = cycles[i].index(m)
                return (i, idx)
        return None
    
    for n in graph:
        # check if n's in a previous cycle
        res = cycleidx(n)
        if res:
            classes[n] = (partOfCycle, res[0], res[1])
            continue
        # follow edges in the graph until we detect a cycle or the end of the sequence
        nseq = []
        isrepeat = False
        seqended = False
        cur = n
        while not isrepeat and not seqended:
            nseq.append(cur)
            # get next value in sequence
            nxt = graph[cur]
            # check if it's in a previous cycle
            res = cycleidx(nxt)
            if res:
                classes[n] = (leadsToCycle, res[0], None)
                notcyclic.append(n)
                break
            # check if nxt is already classified
            if nxt in classes:
                classes[n] = classes[nxt]
                notcyclic.append(n)
                break
            isrepeat = nxt in nseq
            seqended = not nxt in graph
            cur = nxt
        if isrepeat:
            # found a new cycle, locate 
            # where it begins and save
            idx = nseq.index(cur)
            cycles.append(nseq[idx:])
            # classify n
            if idx == 0:
                classes[n] = (partOfCycle, len(cycles)-1, idx)
            else:
                classes[n] = (leadsToCycle, len(cycles)-1, None)
                notcyclic.append(n)
            # could classify the rest of nseq right now too!!
        elif seqended:
            # sequence ended so we don't know whether n diverges or eventually becomes periodic
            # classify all of nseq as possiblyDivergent
            pd = (possiblyDivergent, None, None)
            for m in nseq:
                classes[m] = pd
                notcyclic.append(m)
    return (cycles, classes)
