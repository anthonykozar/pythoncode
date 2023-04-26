# Wythoff.py
#
# A collection of functions using Sprague-Grundy theory to
# calculate the nim values of Wythoff's Game/Wyt Queen 
# generalized in various ways to N heaps/dimensions.
#
# Anthony Kozar
# November 12-27, 2018
# October 3- , 2019

import copy
import operator

#### Helper functions for creating and using N-dimensional arrays

# Create a numdims-dimensional array with dimensions of size dsize
def CreateNDimArray(numdims, dsize, defaultval = None):
    a = [defaultval]*dsize
    for d in range(numdims-1):
        a = [copy.deepcopy(a) for i in range(dsize)]
    return a

# Get the element or subarray at the given indices from an N-dimensional array
def GetNDimElement(arr, indices):
    subarr = arr
    for d in indices:
        subarr = subarr[d]
    return subarr

# Set the element or subarray at the given indices in an N-dimensional array
def SetNDimElement(arr, indices, value):
    subarr = arr
    # get the lowest-level subarray containing the element to be changed
    for d in indices[:-1]:
        subarr = subarr[d]
    subarr[indices[-1]] = value

# Return a list of the next set of indices for iterating over an N-dimensional array 
# with dimensions all of size dsize.  Eg. NextIndices((1,0,9), 10) returns [1,1,0]
def NextIndices(indices, dsize):
    numdims = len(indices)
    indices = list(indices) # copy indices to a new list
    for i in xrange(numdims-1, -1, -1):
        if indices[i] < dsize-1:
            indices[i] += 1
            break
        else:
            indices[i] = 0
            if i == 0:
                return None # signal done as we've wrapped around to (0,...,0)
            continue        # increment next index too
    return indices

# Return a list of tuples of all sets of indices for an N-dimensional array
# with dimensions all of size dsize.
def GenerateIndicesList(numdims, dsize):
    indtuples = []
    if numdims == 0 or dsize == 0:
        return indtuples
    indices = [0]*numdims
    while indices != None:
        indtuples.append(tuple(indices))
        indices = NextIndices(indices, dsize)
    return indtuples

# A generator for all sets of indices for an N-dimensional array with
# dimensions all of size dsize.
def NDimIndices(numdims, dsize):
    if numdims == 0 or dsize == 0:
        return
    indices = [0]*numdims
    while indices != None:
        yield tuple(indices)
        indices = NextIndices(indices, dsize)
    return


####

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

# Return move options for Wythoff Any/Wyt Queen in N dimensions
def WythoffAnyMoves(heaps):
    numheaps = len(heaps)
    moves = list()
    # remove any number of counters from a single heap
    for h in range(numheaps):
        for i in range(heaps[h]):
            # make a new mutable copy of heaps each time
            heapslist = list(heaps)
            heapslist[h] = i
            moves.append(tuple(heapslist))
    # TO DO: remove the same number of counters from any set of 2 or more heaps
    # remove the same number of counters from all heaps
    maxremovable = min(heaps)
    for i in range(1, maxremovable+1):
        heapslist = map(lambda n: n-i, heaps)
        moves.append(tuple(heapslist))
    return moves

# Return move options for "Wythoff All" with N heaps
def WythoffAllMoves(heaps):
    numheaps = len(heaps)
    moves = list()
    # remove any number of counters from a single heap
    for h in range(numheaps):
        for i in range(heaps[h]):
            # make a new mutable copy of heaps each time
            heapslist = list(heaps)
            heapslist[h] = i
            moves.append(tuple(heapslist))
    # remove the same number of counters from all heaps
    maxremovable = min(heaps)
    for i in range(1, maxremovable+1):
        heapslist = map(lambda n: n-i, heaps)
        moves.append(tuple(heapslist))
    return moves

# Return move options for "Wythoff Pairs" with N heaps
def WythoffPairsMoves(heaps):
    numheaps = len(heaps)
    moves = list()
    # remove any number of counters from a single heap
    for h in range(numheaps):
        for i in range(heaps[h]):
            # make a new mutable copy of heaps each time
            heapslist = list(heaps)
            heapslist[h] = i
            moves.append(tuple(heapslist))
            # print heapslist
    # remove the same number of counters from any pair of heaps
    for h1 in range(numheaps-1):
        for h2 in range(h1+1, numheaps):
            # print "\rh1 = %d  h2 = %d" % (h1, h2)
            # make a new mutable copy of heaps each time
            heapslist = list(heaps)
            maxremovable = min(heaps[h1], heaps[h2])
            for i in range(1, maxremovable+1):
                heapslist[h1] = heaps[h1] - i
                heapslist[h2] = heaps[h2] - i
                moves.append(tuple(heapslist))
                # print heapslist
    return moves

# Calculate the nim values for Wythoff's Game/Wyt Queen in numheaps dimensions
def WythoffsGame(numheaps = 2, maxheap = 10):
    finalpos = tuple([0]*numheaps)
    # create a numheaps-dimensional array with dimensions of size maxheap+1
    g = CreateNDimArray(numheaps, maxheap+1)
    SetNDimElement(g, finalpos, 0)
    for x in range(maxheap+1):
        for y in range(maxheap+1):
            if x==0 and y==0: continue
            moves = WythoffAllMoves((x,y))
            movevals = [GetNDimElement(g, mv) for mv in moves]
            nval = mex(movevals)
            SetNDimElement(g, (x,y), nval)
    return g

# Calculate the nim values for Wythoff's Game/Wyt Queen in 3 dimensions
def WythoffsGame3(numheaps = 3, maxheap = 10):
    finalpos = tuple([0]*numheaps)
    # create a numheaps-dimensional array with dimensions of size maxheap+1
    g = CreateNDimArray(numheaps, maxheap+1)
    SetNDimElement(g, finalpos, 0)
    for x in range(maxheap+1):
        for y in range(maxheap+1):
            for z in range(maxheap+1):
                if x==0 and y==0 and z==0: continue
                moves = WythoffAllMoves((x,y,z))
                movevals = [GetNDimElement(g, mv) for mv in moves]
                nval = mex(movevals)
                SetNDimElement(g, (x,y,z), nval)
    return g

# Calculate the nim values for a game parameterized by numheaps natural
# numbers with moves defined by the function movesfunc((n1,n2,...nn)).
def NimValues(movesfunc, numheaps = 2, maxheap = 10):
    # create a numheaps-dimensional array with dimensions of size maxheap+1
    g = CreateNDimArray(numheaps, maxheap+1)
    # iterate over all indices for the array g
    for indices in NDimIndices(numheaps, maxheap+1):
        moves = movesfunc(indices)
        movevals = [GetNDimElement(g, mv) for mv in moves]
        if None in movevals:
            print "NimValues(): Undefined position in movevals!"
            print "indices: ", indices
            print "moves: ", moves
            print "movevals: ", movevals
        nval = mex(movevals)
        SetNDimElement(g, indices, nval)
    return g

def KingRookMoves(heaps):
    numheaps = len(heaps)
    moves = list()
    # remove any number of counters from a single heap
    for h in range(numheaps):
        for i in range(heaps[h]):
            # make a new mutable copy of heaps each time
            heapslist = list(heaps)
            heapslist[h] = i
            moves.append(tuple(heapslist))
    # remove one counter from all heaps
    maxremovable = min(heaps)
    if maxremovable > 0:
        heapslist = map(lambda n: n-1, heaps)
        moves.append(tuple(heapslist))
    return moves

# Return move options for a Nim variant where a move is required to
# remove at least 1 bead from two different heaps.
def TwoMoveNimMoves(heaps):
    numheaps = len(heaps)
    if numheaps < 2:
        print "TwoMoveNimMoves(): less than 2 heaps!"
    moves = list()
    # remove any number of counters from two heaps
    for h1 in range(numheaps-1):
        for h2 in range(h1+1, numheaps):
            for i1 in range(heaps[h1]):
                for i2 in range(heaps[h2]):
                    # make a new mutable copy of heaps each time
                    heapslist = list(heaps)
                    heapslist[h1] = i1
                    heapslist[h2] = i2
                    moves.append(tuple(heapslist))
    return moves

####

def Print2DArray(arr):
    for row in arr:
        for col in row:
            print "%2d" % col,
        print

def Print3DArray(arr):
    for x in arr:
        for y in x:
            for z in y:
                print "%2d" % z,
            print
        print

# Check a 3D array for symmetrical values when the indices are permuted.
# NOTE: This function assumes that all dimensions of the array have the same size.
def Check3DSymmetry(arr):
    count = 0
    for x in range((len(arr))):
        for y in range((len(arr))):
            for z in range((len(arr))):
                mismatchfound = False
                if arr[x][y][z] != arr[x][z][y]:
                    print "Mismatch A at [%d][%d][%d]: %2d %2d" % (x,y,z,arr[x][y][z],arr[x][z][y])
                    mismatchfound = True
                if arr[x][y][z] != arr[y][x][z]:
                    print "Mismatch B at [%d][%d][%d]: %2d %2d" % (x,y,z,arr[x][y][z],arr[y][x][z])
                    mismatchfound = True
                if arr[x][y][z] != arr[y][z][x]:
                    print "Mismatch C at [%d][%d][%d]: %2d %2d" % (x,y,z,arr[x][y][z],arr[y][z][x])
                    mismatchfound = True
                if arr[x][y][z] != arr[z][x][y]:
                    print "Mismatch D at [%d][%d][%d]: %2d %2d" % (x,y,z,arr[x][y][z],arr[z][x][y])
                    mismatchfound = True
                if arr[x][y][z] != arr[z][y][x]:
                    print "Mismatch E at [%d][%d][%d]: %2d %2d" % (x,y,z,arr[x][y][z],arr[z][y][x])
                    mismatchfound = True
                if not mismatchfound:
                    count += 1
    print "%d matches verified" % count

# Check that a 3D array matches the values of the Grundy function of 3-pile Nim.
# NOTE: This function assumes that all dimensions of the array have the same size.
def Check3DArrayIsNim(arr):
    count = 0
    for x in range((len(arr))):
        for y in range((len(arr))):
            for z in range((len(arr))):
                if arr[x][y][z] != (x ^ y ^ z):
                    print "Mismatch at [%d][%d][%d]: %2d %2d" % (x,y,z,arr[x][y][z],(x ^ y ^ z))
                else:
                    count+=1
    print "%d matches verified" % count

# Check that an N-dimensional array matches the values of the Grundy function of N-pile Nim.
# Optionally, all values can be XORed with xorconst (useful for subarrays).
# NOTE: This function assumes that all dimensions of the array have the same size.
def CheckNDimArrayIsNim(arr, numdims, xorconst = 0, printMismatches = False):
    equalcount = 0
    uneqlcount = 0
    # iterate over all indices for the array
    for indices in NDimIndices(numdims, len(arr)):
        arrval = GetNDimElement(arr, indices)
        nimval = reduce(operator.xor, indices) ^ xorconst
        if arrval != nimval:
            uneqlcount += 1
            if printMismatches:
                print "Mismatch at %s: %2d %2d" % (indices, arrval, nimval)
        else:
            equalcount += 1
    print "%d matches, %d non-matches" % (equalcount, uneqlcount)
