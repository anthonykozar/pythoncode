# Map all Game of Life state transitions for small, finite grids
#
# Anthony Kozar
# February 18, 2014


# from factor.py
def baseconvert(val,base):
    if base > 26:
        return "Error: base > 26"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basestr = ""
    while val > 0:
        # rmndr = val % base
        # val = val // base
        val, rmndr = divmod(val, base)
        basestr = digits[rmndr] + basestr
    return basestr


def int2binarylist(val,numbits):
    bitlist = []
    while numbits > 0:
        # rmndr = val % 2
        # val = val // 2
        val, rmndr = divmod(val, 2)
        bitlist.insert(0, rmndr)
        numbits = numbits - 1
    return bitlist

def binarylist2int(bitlist):
    num = bitlist[0]
    for bit in bitlist[1:]:
        num = num*2 + bit
    return num

def PrintArrayAs2D(array, numrows, numcols):
    for row in range(numrows):
        for col in range(numcols):
            print array[row*numcols + col],
        print

def PrintSideBySide(numcols, *arrays):
    # find the number of rows needed for the longest array
    largestsize = 0
    for arr in arrays:
        size = len(arr)
        if size > largestsize:  largestsize = size
    numrows = largestsize // numcols    # ignores remainder!
    for row in range(numrows):
        for arr in arrays:
            for col in range(numcols):
                idx = row*numcols + col
                if idx < len(arr):
                    print arr[idx],
                else:
                    print "-",
            print "   ",
        print

# print the Life grid that corresponds to integer val
def PrintGrid(val, numbits = 16, numcols = 4):
    bitlist = int2binarylist(val,numbits)
    numrows = numbits // numcols    # ignores remainder!
    PrintArrayAs2D(bitlist, numrows, numcols)

# print the Life grids for integers val1 & val2 side-by-side 
def PrintTwo(val1, val2, numbits = 16, numcols = 4):
    bits1 = int2binarylist(val1, numbits)
    bits2 = int2binarylist(val2, numbits)
    str1 = hex(val1)
    print str1, ' '*(2*numcols+2-len(str1)), hex(val2)
    PrintSideBySide(numcols, bits1, bits2)

# Concatenate the lists of listoflists
def CatLists(listoflists):
    # return reduce(lambda x, y: x+y, listoflists)
    return sum(listoflists, [])


# GetStdNeighborhood()
#
# Returns a 3x3 array of the cell states in the standard
# neighborhood around (and including) the cell at (cellrow,cellcol).
# Neighborhoods at the edge of the grid are clipped and noneValue is
# returned in the positions of missing cells.
#
# Rows and cols are numbered from 0 to numrows-1 and numcols-1
# cellstates should be a 1-dim array with the values of cells
# in this order: row0col0 ... row0coln-1, row1col0 ... row1coln-1,
# ..., rown-1col0 ... rown-1coln-1.

def GetStdNeighborhood(cellrow, cellcol, cellstates, numrows, numcols, noneValue = None):
    neighborhood = []
    for row in [cellrow-1,cellrow,cellrow+1]:
        rowstates = []
        for col in [cellcol-1,cellcol,cellcol+1]:
            if row < 0 or row > numrows-1 or col < 0 or col > numcols-1:
                state = noneValue
            else:
                state = cellstates[row*numcols + col]
            rowstates.append(state)
        neighborhood.append(rowstates)
    return neighborhood


# GetToroidalNeighborhood()
# ... maybe later


# LifeCellNextState()
#
# Returns the successor state for a single Life cell with the given neighborhood.
# (neighborhood should be a 3x3 array of 1s and 0s)

def LifeCellNextState(neighborhood):
    curstate = neighborhood[1][1]
    numneighbors = sum(CatLists(neighborhood)) - curstate
    if numneighbors == 3:
        newstate = 1
    elif numneighbors == 2 and curstate == 1:
        newstate = 1
    else:
        newstate = 0
    return newstate

# LifeArrayNextState()
#
# Returns the successor state for an array of Life cells.
# (cellstates should be a 1D array of 1s and 0s with numrows*numcols values)

def LifeArrayNextState(cellstates, numrows, numcols):
    newstates = []
    for row in range(numrows):
        for col in range(numcols):
            newstates.append(LifeCellNextState(GetStdNeighborhood(row, col, cellstates, numrows, numcols, 0)))
    return newstates


def Make4x4SuccessorTable():
    successors = []
    for i in range(65536):
        n = int2binarylist(i, 16)
        n = LifeArrayNextState(n,4,4)
        image = binarylist2int(n)
        successors.append(image)
        if (i%1000) == 0:
            print i,
        # print hex(i), hex(image)
    print
    return successors

# InvertMapping()
#
# Accepts an array representing a funcion from the integer range
# [0,len(mapping)-1] to itself and reverses the mapping by returning
# an array of lists such that array[i] is a list of all indices in
# the original 'mapping' that have the value i.

def InvertMapping(mapping):
    invmap = []
    # create empty lists for inverse images
    for i in range(len(mapping)):
        invmap.append([])
    # iterate over mapping and add each index to its image's list
    for i in range(len(mapping)):
        invmap[mapping[i]].append(i)
    return invmap


# Calculate successor and predecessor tables for 4x4 Life grids!
succ = Make4x4SuccessorTable()
pred = InvertMapping(succ)

# Calculate number of predecessors for each 4x4 Life grid
numpred = map(len, pred)


def PredecessorStats(predecessors):
    stats = dict()
    # iterate over predecessors mapping and count the number with 0,1,2, etc. predecessors
    for i in range(len(predecessors)):
        numpreds = len(predecessors[i])
        if numpreds in stats:
            stats[numpreds] = stats[numpreds] + 1
        else:
            stats[numpreds] = 1
    return stats

def PrintStats(stats, col1text='N', col2text='# patterns w/ N predecessors'):
    print col1text, '\t', col2text
    print "------------------------------------"
    for item in stats.items():
        print item[0], '\t', item[1]


# calculate histogram-like statistics
stats = PredecessorStats(pred)
PrintStats(stats)

# make a list of all 4x4 Life states with exactly one predecessor
# (these can be used as "reverse Life puzzles") 
unique = [i for i in range(len(pred)) if len(pred[i]) == 1]
