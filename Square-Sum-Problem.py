# The Square-Sum Problem
# (and other related problems solvable with graphs)
#
# Problem: Can the numbers 1 thru N be arranged in a
# sequence (permutation) so that each pair of adjacent
# numbers adds up to a square number.
#
# See this Numberphile video for an introduction:
#   https://m.youtube.com/watch?v=G1m7goLCJDY
#
# Anthony Kozar
# May 4, 2023

# From the video: 15 is the smallest N with a solution.  16
# and 17 also work, but then 18 does not.

# Solution: Construct a graph with the numbers as vertices
# and the edges connecting pairs that do sum to a square.
# If any Hamiltonian paths exist in the graph, they are the
# solutions for 1 to N.

import sys
from collections import defaultdict


# make a list of squares up to maxval, excluding 1
def listofsquares(maxval):
    sqrs = []
    i = 2
    while (i*i) <= maxval:
        sqrs.append(i*i)
        i += 1
    return sqrs

# Our graphs will be dictionaries that maps vertices to sets
# of adjacent vertices.
def addedge(graph, a, b):
    graph[a].add(b)
    graph[b].add(a)

# Add edges to graph for every b such that a + b is in vals
def ConnectVertexBySums(graph, a, vals, maxval):
    for val in vals:
        b = val - a
        if b > 0 and b <= maxval and b != a:
            addedge(graph, a, b)
    # make sure that vertex 'a' exists
    return graph[a]

def MakeSquareSumGraph(n):
    maxsum = 2*n - 1
    sqrs = listofsquares(maxsum)
    graph = defaultdict(set)
    for a in xrange(1, n+1):
        ConnectVertexBySums(graph, a, sqrs, n)
    return graph

# print a graph in dreadnaut format
def PrintGraph(graph, out = sys.stdout):
    pass

# print the adjacency matrix of a graph
def PrintAdjacencyMatrix(graph, out = sys.stdout):
    vertices = graph.keys()
    for v in vertices:
        for w in vertices:
            if w in graph[v]:
                out.write('1 ')
            else: out.write('0 ')
        out.write('\n')

# print the adjacency matrices of a range of square-sum graphs,
# prefacing each with the header expected by the amtog program
# included with the gtools/nauty package.
def PrintRangeSquareSumMatrices(firstn, lastn, out = sys.stdout):
    maxsum = 2*lastn - 1
    sqrs = listofsquares(maxsum)
    graph = defaultdict(set)
    # make the graph of size firstn
    for a in xrange(1, firstn+1):
        ConnectVertexBySums(graph, a, sqrs, firstn)
    out.write('n=%d m\n' % firstn)
    PrintAdjacencyMatrix(graph, out)
    out.write('\n')
    # add one vertex at a time to make the other graphs
    for a in xrange(firstn+1, lastn+1):
        ConnectVertexBySums(graph, a, sqrs, a)
        out.write('n=%d m\n' % a)
        PrintAdjacencyMatrix(graph, out)
        out.write('\n')

# Hamiltonion paths can be found by the gtools' program hamheuristic:
#     python2 Square-Sum-Problem.py > square-sum-matrices.txt
#     amtog square-sum-matrices.txt | hamheuristic -p -v

