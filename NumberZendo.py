# NumberZendo.py

# Code to help play Number Zendo.

from factor import *
from digits import *
from numbases import *

HAS = [5,10,13,15,17,20,25,30,34,39,40,50,60,65,78,85,125,130,765,1105]
HASNOT = [1,2,3,4,6,7,21,35,45,95,110,115,124,135,190,775]

def factorall(haslist = HAS, hasnot = HASNOT):
    print "HAS"
    print "---"
    map(printfactors, haslist)
    print "\nHAS NOT"
    print "-------"
    map(printfactors, hasnot)
    print

def evaluateNum(num):
    print str(num)+": ",    # final comma prevents newline
    print "(" + str(sumdigits(num)) + ")",
    pfactor(num)
    print                   # writes a newline

def zendo30231(koan):
    val = base12to10(koan)
    print val, "   ", val / 7.0

def evall():
    print "::HAS::\n"
    map(evaluateNum, HAS)
    print "\n\n::HAS NOT::\n"
    map(evaluateNum, HASNOT)
    print "\n\n"
    print "::HAS::\n"
    map(bases, HAS)
    print "\n\n::HAS NOT::\n"
    map(bases, HASNOT)
    print
    print map(lambda x: x+1, HAS)
    print map(lambda x: x+1, HASNOT)

def checkmods():
    for i in range(2,24):
        print "HAS    %% %s: " % i,
        print map(lambda x: x%i, HAS)
        print "HASNOT %% %s: " % i,
        print map(lambda x: x%i, HASNOT)

def checkmods2(has, hnot, mods):
    for i in mods:
        print "HAS    %% %s: " % i,
        print map(lambda x: x%i, has)
        print "HASNOT %% %s: " % i,
        print map(lambda x: x%i, hnot)
        print

def bases(num):
    print num, baseconvert(num,2), baseconvert(num,8), baseconvert(num,16)

def allbases():
    for i in range(2,10):
        print "Base %s" % i
        print "HAS: ",
        print map(lambda x: baseconvert(x,i), HAS)
        print "HASNOT: ",
        print map(lambda x: baseconvert(x,i), HASNOT)
        print

def printfactorsums():
    print "::HAS::\n"
    map(printfactorsum, HAS)
    print "\n\n::HAS NOT::\n"
    map(printfactorsum, HASNOT)
    print "\n\n"

def evaluateNum_RvrsNum(num):
    line = "(" + str(sumdigits(num)) + ")"
    line += (5 - len(line))*" "    # pad with spaces
    line += str(num) + ":  " + pfactorstr(num)
    line += (40 - len(line))*" "    # pad with spaces
    rvrs = reversedigits(num)
    line += str(rvrs) + ":  " + pfactorstr(rvrs)
    print line

def evalrvrs():
    print "::reverse HAS::\n"
    map(evaluateNum_RvrsNum, map(reversedigits, HAS))
    print "\n\n::reverse HAS NOT::\n"
    map(evaluateNum_RvrsNum, map(reversedigits, HASNOT))
    print "\n\n"

def counteachdigit(num):
    digits = str(num)
    counts = [0,0,0,0,0,0,0,0,0,0]
    for dgt in digits:
        counts[int(dgt)] += 1
    return counts

def printcounts(num, counts):
    line = str(num)
    line += (10 - len(line))*" "    # pad with spaces
    for i in counts:
        if i == 0:
            s = ""
        else:
            s = str(i)
        s += (3 - len(s))*" "       # pad with spaces
        line += s

    # count even and odd digits
    even = odd = 0
    for i in [0,2,4,6,8]:
        even += counts[i]
        odd  += counts[i+1]
    es = str(even)
    es += (5 - len(s))*" "
    os = str(odd)
    os += (5 - len(s))*" "
    line += es + os

    # non-zero even digits
    nz = even - counts[0]
    line += str(nz)
    
    print line

def evalcounts():
    print "::HAS::\n"
    print "koan      0  1  2  3  4  5  6  7  8  9  evn  odd  nzevn"
    print "----      -  -  -  -  -  -  -  -  -  -  ---  ---  -----"
    map(lambda n: printcounts(n,counteachdigit(n)), HAS)
    print "\n\n::HAS NOT::\n"
    print "koan      0  1  2  3  4  5  6  7  8  9  evn  odd  nzevn"
    print "----      -  -  -  -  -  -  -  -  -  -  ---  ---  -----"
    map(lambda n: printcounts(n,counteachdigit(n)), HASNOT)

def deriveseq(maxval, printvalues = False):
    YES = {}
    NO = {}
    putInYes = True
    for n in xrange(0, maxval + 1):
        s = sortdigits(n)
        if s in YES:
            if printvalues: print n
            pass
        elif s in NO:
            if printvalues: print ' '*10, n
            pass
        elif putInYes:
            YES[s] = n
            putInYes = False
            if printvalues: print n
        else:
            NO[s] = n
            putInYes = True
            if printvalues: print ' '*10, n
    return YES, NO

def isInYes(num):
    s = sortdigits(num)
    return s in YES
def isInNo(num):
    s = sortdigits(num)
    return s in NO

# Divide n by each repunit from 11 up to the length of n
def divrepunits(n):
    limit = 1 + len(str(n))
    nflt = 1.0 * n
    for k in xrange(2, limit):
        repunit = int("1"*k)
        print "%-*d  %f" % (limit, repunit, nflt/repunit)

# koans for old Zendo games

# HAS = [300,330,600,660,990,12001,28585,33660,33663,36360,36369,47471,58582,58584,3366990]
# HASNOT = [131,171,230,240,360,417,630,666,909,1200,1234,3330,3366,9981,258258,369963]

# Zendo #30239
# HAS = [11,15,32,57,75,192,194,197,321,480,1024,16777216]
# HASNOT = [1,2,4,5,8,9,16,23,25,30,202,404]

# Zendo #33286
# HAS = [2468, 23456, 23465, 24680, 35246, 42635, 65432, 234567, 876543,
#        2233456, #273747576, 23234546265,]
# ]
# HASNOT = [111, 125, 192, 6543, 12345, 13456, 22222,]
