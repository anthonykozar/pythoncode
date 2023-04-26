import operator

def bipartitions(n,incl_perms= False):
    parts = list()
    for i in range(1,n):
        if i<=(n-i) or incl_perms:
            parts.append((i, n-i))
    return parts

def tripartitions(n,incl_perms= False):
    parts = list()
    for i in range(1,n):
        if incl_perms: s=1
        else: s=i
        for j in range(s,n-i):
            if j<=(n-i-j) or incl_perms:
                parts.append((i, j, n-i-j))
    return parts

def unequalbipartitions(n):
    parts = list()
    for i in range(1,n):
        if i<(n-i):
            parts.append((i, n-i))
    return parts

def unequaltripartitions(n):
    parts = list()
    for i in range(1,n):
        for j in range(i+1,n-i):
            if j<(n-i-j):
                parts.append((i, j, n-i-j))
    return parts

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

def NimSequence(movesfunc, xor, maxheap = 20):
    g = [0]
    for n in range(1, maxheap+1):
        moves = movesfunc(n)
        movevals = list()
        for mv in moves:
            # allow mixed types in moves
            if type(mv) in [str, unicode, list, tuple, buffer, xrange]:
                val = reduce(xor, map(lambda i: g[i], mv))
            else: val = g[mv]
            movevals.append(val)
        # nval = mex(movevals)
        nval=0
        # minimal excluded value should never be greater than
        stop = len(movevals) + 1
        while nval < stop:
            if not nval in movevals:
                break
            nval+=1
        # end mex()
        g.append(nval)
        # print n, movevals, nval
    return g

def sub12(n):
    moves = list()
    if n-1>0: moves.append(n-1)
    if n-2>0: moves.append(n-2)
    return moves

def sub23(n):
    moves = list()
    if n-3>0: moves.append(n-3)
    if n-2>0: moves.append(n-2)
    return moves

def Sub12PlusGrundy(n):
    moves = [n-1,n-2]
    for i in range(1,n):
        if i<(n-i):
            moves.append((i, n-i))
    return moves
