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

from collections import defaultdict

def MakeSquareSumGraph(n):
    maxsum = 2*n - 1
    # make a list of squares up to maxsum
    sqrs = []
    i = 2
    while (i*i) <= maxsum:
        sqrs.append(i*i)
        i += 1

    # graph maps vertices to sets of adjacent vertices
    graph = defaultdict(set)
    for a in xrange(1, n+1):
        for sq in sqrs:
            b = sq - a
            if b > 0 and b <= n and b != a:
                graph[a].add(b)
                graph[b].add(a)
    return graph
