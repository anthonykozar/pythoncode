# SpragueGrundy.py
#
# A collection of functions using Sprague-Grundy theory to
# calculate the nim values of Grundy's Game and other
# impartial combinatorial games.
#
# Anthony Kozar
# October 4-11, 2018

import operator

# Return a list of all ways of splitting n into 2 parts
def bipartitions(n, incl_perms = False):
    parts = list()
    for i in range(1,n):
        if i<=(n-i) or incl_perms:
            parts.append((i, n-i))
    return parts

# Return a list of all ways of splitting n into 3 parts
def tripartitions(n, incl_perms = False):
    parts = list()
    for i in range(1,n):
        if incl_perms: s=1
        else: s=i
        for j in range(s,n-i):
            if j<=(n-i-j) or incl_perms:
                parts.append((i, j, n-i-j))
    return parts

# Return a list of all ways of splitting n into 2 unequal parts
def unequalbipartitions(n):
    parts = list()
    for i in range(1,n):
        if i<(n-i):
            parts.append((i, n-i))
    return parts

# Return a list of all ways of splitting n into 3 unequal parts
def unequaltripartitions(n):
    parts = list()
    for i in range(1,n):
        for j in range(i+1,n-i):
            if j<(n-i-j):
                parts.append((i, j, n-i-j))
    return parts

# Minimal excluded value: returns the smallest natural number
# (incl. 0) not contained in the set values.
def mex(values):
    i=0
    # minimal excluded value should never be greater than
    stop = len(values) + 1
    while i<stop:
        if not i in values:
            return i
        i+=1
    print "mex(): stop assumption is incorrect?", values
    return None

# Calculate the nim values for single heaps in Grundy's Game.
def GrundysGame(maxheap = 20):
    g = [0]
    for n in range(1, maxheap+1):
        moves = unequalbipartitions(n)
        movevals = list()
        for mv in moves:
            val = g[mv[0]] ^ g[mv[1]]
            movevals.append(val)
        nval = mex(movevals)
        g.append(nval)
        # print n, movevals, nval
    return g

# Calculate the nim values for single heaps in a variant of Grundy's Game
# where moves are to split a heap into 3 unequal heaps.
def GrundySplit3(maxheap = 20):
    g = [0]
    for n in range(1, maxheap+1):
        moves = unequaltripartitions(n)
        movevals = list()
        for mv in moves:
            val = g[mv[0]] ^ g[mv[1]] ^ g[mv[2]]
            movevals.append(val)
        nval = mex(movevals)
        g.append(nval)
        # print n, movevals, nval
    return g

# Calculate the nim values for a game parameterized by a single natural
# number with moves defined by the function movesfunc(n).
def NimSequence(movesfunc, maxheap = 20):
    g = [0] # assumes no moves from position 0!
    for n in range(1, maxheap+1):
        moves = movesfunc(n)
        movevals = list()
        for mv in moves:
            # allow mixed types in moves
            if type(mv) in [list, tuple, buffer, xrange, str, unicode]:
                val = reduce(operator.xor, map(lambda i: g[i], mv))
            else: val = g[mv]
            movevals.append(val)
        nval = mex(movevals)
        g.append(nval)
        # print n, movevals, nval
    return g

# Return move options for the game Subtraction {1,2}.
def Sub12(n):
    moves = list()
    if n-1 >= 0: moves.append(n-1)
    if n-2 >= 0: moves.append(n-2)
    return moves

# Return move options for the game Subtraction {2,3}.
def Sub23(n):
    moves = list()
    if n-3 >= 0: moves.append(n-3)
    if n-2 >= 0: moves.append(n-2)
    return moves

# Return move options for a variant of Grundy's Game that also allows
# subtracting 1 or 2 from any heap. (The nim sequence is identical to
# octal game 4.33 below).
def Sub12PlusGrundy(n):
    return Sub12(n) + unequalbipartitions(n)

# Return move options for octal game 4.33.
def OctalGame433(n):
    return Sub12(n) + bipartitions(n)

# Return move options for a Subtraction game with the subtraction set subtrset.
def SubtractSet(n, subtrset):
    moves = list()
    for m in subtrset:
        if n-m >= 0: moves.append(n-m)
    return moves

# Return a function that returns move options for a Subtraction game
# with the subtraction set subtrset.
def SubtractSetFunc(subtrset):
    return lambda n: SubtractSet(n, subtrset)
