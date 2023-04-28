def _partitions(n, maxpartsize, debug, indent, f):
    if maxpartsize == None or maxpartsize > n:
        maxpartsize = n
    if debug: print(indent + "part(%d,%d)" % (n, maxpartsize))
    totalparts = 0
    while maxpartsize > 0:
        nummaxparts = n // maxpartsize
        if maxpartsize == 1:
            totalparts += 1
            if debug: print(indent + "  all 1's: 1")
        elif maxpartsize == 2:
            totalparts += nummaxparts
            if debug: print(indent + "  2..2: %d" % nummaxparts)
        elif maxpartsize == n:
            totalparts += 1
            if debug: print(indent + "  %d: 1" % n)
        elif nummaxparts == 1:
            if debug: print(indent + "  %d: " % maxpartsize)
            totalparts += f["partitions"](n - maxpartsize, None, debug, indent + "  ", f)
        else:
            for k in xrange(1, nummaxparts+1):
                leftover = n - k*maxpartsize
                if debug:
                    s = (str(maxpartsize)+" ")*k
                    print(indent + "  %s: " % s)
                if leftover > 0:
                    totalparts += f["partitions"](leftover, min(leftover,  maxpartsize-1), debug, indent + "  ", f)
                else:
                    totalparts += 1
                    if debug: print(indent + "    1")
        maxpartsize -= 1
    if debug: print(indent + "total: %d" % totalparts)
    return totalparts

funcs = {"partitions": _partitions}

def partitions(n, maxpartsize = None, debug = False, indent = "", f = funcs):
    return f["partitions"](n, maxpartsize, debug, indent, f)

# generalized pentagonal numbers
pent = [k*(3*k - 1)/2 for k in xrange(1,41)]
npent = [k*(3*k + 1)/2 for k in xrange(1,41)]
gpent = pent + npent
gpent.sort()

# Calculate the partitions of 1 to n using Euler's recurrence formula 
# p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) ...
# where 1,2,5,7,... are the generalized pentagonal numbers
def partitionsrecurrence(n, pentnums = gpent):
    partcounts = [1] # 1 partition of 0
    for i in xrange(1, n+1):
        numparts = 0
        sign = 0 # pattern ++--++--...
        pentidx = 0
        partidx = i - pentnums[pentidx]
        while partidx >= 0:
            if sign < 2:
                numparts += partcounts[partidx]
            else:
                numparts -= partcounts[partidx]
            sign = (sign+1) % 4
            pentidx += 1
            partidx = i - pentnums[pentidx]
        partcounts.append(numparts)
    return partcounts[1:]

########
# number of columns to print different modulos of a sequence
cols = [72, 72, 8, 9, 16, 25, 72, 49, 32, 27, 25, 11, 72, 13, 56, 25, 64, 17, 54, 19, 20]

def PrintModuliInColumns(seq, mod, columns = 0):
    print "seq %% %d\n" % mod
    if columns == 0 and mod < len(cols):
        columns = cols[mod] # use default if none given
    count = 0
    for a in seq:
        print str(a % mod) + ",",
        count += 1
        if count == columns:
            print
            count = 0
    print "\n"
