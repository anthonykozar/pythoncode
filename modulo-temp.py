print "+/3",
for i in range(11):
    print "%2d" % i,
print
for i in range(11):
    print "%2d " % i,
    for j in range(11):
        if (i+j)%3 == 0:
            print "%2d" % (((i+j)/3)%7),
        else:
            print " .",
    print

def magicsqr(s):
    def prsum(a, b, c):
        print "%d+%d+%d=%d" % (a, b, c, a+b+c)
    prsum(s[0], s[1], s[2])
    prsum(s[3], s[4], s[5])
    prsum(s[6], s[7], s[8])
    prsum(s[0], s[3], s[6])
    prsum(s[1], s[4], s[7])
    prsum(s[2], s[5], s[8])
    prsum(s[0], s[4], s[8])
    prsum(s[2], s[4], s[6])

def partitions(n, maxpartsize = None, debug = False, indent = "", partitions = partitions):
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
            totalparts += partitions(n - maxpartsize, None, debug, indent + "  ")
        else:
            for k in xrange(1, nummaxparts+1):
                leftover = n - k*maxpartsize
                if debug:
                    s = (str(maxpartsize)+" ")*k
                    print(indent + "  %s: " % s)
                if leftover > 0:
                    totalparts += partitions(leftover, min(leftover,  maxpartsize-1), debug, indent + "  ")
                else:
                    totalparts += 1
                    if debug: print(indent + "    1")
        maxpartsize -= 1
    if debug: print(indent + "total: %d" % totalparts)
    return totalparts
