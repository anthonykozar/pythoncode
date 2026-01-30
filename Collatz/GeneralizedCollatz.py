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

def f5xp1d6(n):
    if (n%2) == 0:
        return n/2
    elif (n%3) == 0:
        return n/3
    else:
        return 5*n+1

def f3xp5(n):
    if (n%2) == 0:
        return n/2
    else:
        return 3*n+5

# Returns a new function f(n) that equals n/d when n is divisible by d or an+b when it is not.
def newcollatzfunc(a, b, d = 2):
    def collfunc(n):
        if (n%d) == 0:
            return n/d
        else:
            return a*n+b
    return collfunc

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

def cyclereport(cycles, classes, printleadinglists = True,  printdivergents = True, maxlistlen = 100, maxnum = 10**12):
    # workaround for bug in Pyonic
    partOfCycle = 1
    leadsToCycle = 2
    possiblyDivergent = 3

    numcycles = len(cycles)
    # create lists of numbers that lead to each cycle or that might diverge
    if printleadinglists or printdivergents:
        leadgbycyc = [list() for i in xrange(numcycles)]
        divergent = []
        for n in classes:
            if classes[n][0] == leadsToCycle and printleadinglists and n <= maxnum:
                leadgbycyc[classes[n][1]].append(n)
            elif classes[n][0] == possiblyDivergent and printdivergents and n <= maxnum:
                divergent.append(n)
    
    # print each cycle beginning with its smallest value and print its list of leading numbers (if requested)
    for i in xrange(numcycles):
        cycmin = min(cycles[i])
        minidx = cycles[i].index(cycmin)
        cyc = cycles[i][minidx:] + cycles[i][0:minidx]
        print "Cycle %d (len %d):\n" % (i, len(cyc))
        print " ", " ".join(map(str, cyc))
        print
        if printleadinglists:
            leadgbycyc[i].sort()
            print "  Numbers leading to cycle %d (%d):" % (i, len(leadgbycyc[i]))
            print "   ", " ".join(map(str, leadgbycyc[i][:maxlistlen]))
            print
    
    if printdivergents:
        divergent.sort()
        print "Numbers that appear to diverge (%d):\n" % (len(divergent))
        print " ".join(map(str, divergent[:maxlistlen]))
        print

# Analyze the iterated behavior of collfunc for inputs 1 to maxtest and print a 
# detailed report of the cycles found, which numbers lead to each cycle, and which 
# numbers appear to diverge.
def dolongreport(collfunc, maxtest, listlen = 100, maxint = 10**12):
    g = makegraph(1, maxtest, 1, collfunc, False, maxint)
    cycles,clss = analyzegraph(g)
    cyclereport(cycles, clss, printleadinglists = True,  printdivergents = True, maxlistlen = listlen, maxnum = maxtest)

for a in [3, 5, 7]:
    # start = 2 - a%2 # b%2 must = a%2 to avoid all sequences monotonically increasing (and taking lots of time)
    for b in [1, 3, 5]:
        horizline = "-" * 20
        print horizline
        print "f(n)=%dn+%d or n/2" % (a,b)
        print horizline
        cf = newcollatzfunc(a, b, 2)
        dolongreport(cf, 10000, maxint = 10**9)
        print "\n"
