import math
import operator

HAS = [5,10,13,15,17,20,25,30,34,39,40,50,60,65,78,85,125,130,765,1105]
HASNOT = [1,2,3,4,6,7,21,35,45,95,110,115,124,135,190,775]

def pfactor(num):
    limit = int(math.sqrt(num))
    for p in xrange(2,limit+1):
        if num < 2:
            break
        while num % p == 0:
            print p,
            num = num / p
    if num > 1:
        print num
    else:
        print

def pfactorlist(num):
    limit = int(math.sqrt(num))
    factors = []
    for p in xrange(2,limit+1):
        if num < 2:
            break
        while num % p == 0:
            factors.append(p)
            num = num / p
    if num > 1:
        factors.append(num)
    return factors

def printfactors(num):
    print str(num)+": ",
    pfactor(num)

def factorall(haslist = HAS, hasnot = HASNOT):
    print "HAS"
    print "---"
    map(printfactors, haslist)
    print "\nHAS NOT"
    print "-------"
    map(printfactors, hasnot)
    print

def pfactormax(n):
    return max(pfactorlist(n))

def tryfactors(num, factors):
    for p in factors:
        if num < 2:
            break
        while num % p == 0:
            print p,
            num = num / p
    if num != 1:
        print num, '**'
    else: print

def isprime(n): return len(pfactorlist(n)) == 1

def notprime(n): return len(pfactorlist(n)) > 1

# return the next prime greater than num
def nextprime(num):
    start = num + 1 + num%2  # start with an odd number
    for n in xrange(start, 2*start, 2):
	if isprime(n):
	    return n

# Interesting number sequences for factoring
repunits = [(10**n - 1)/9 for n in xrange(2,25)]

# for i in xrange(len(repunits)):
#     for j in xrange(i-1):
#         if (repunits[i] % repunits[j]) == 0:
#             print repunits[i], "=", repunits[j], "*", repunits[i]/repunits[j]

mersenne = [2**n - 1 for n in xrange(2,64)]
dblmersenne = [2**(2**n) - 1 for n in xrange(1,9)]
fermat = [2**(2**n) + 1 for n in xrange(0,8)]

# The factors of the nth dblmersenne number are the first n fermat numbers!!
# for f in dblmersenne:
#     print f, ":",
#     tryfactors(f, fermat)

def intersect(setA, setB):
    return filter(lambda x: x in setB, setA)

def sumdigits(num):
    digits = str(num)
    sum = 0
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            sum += int(dgt)
    return sum

def digitalroot(num):
    while num > 9:
        num = sumdigits(num)
    return num

def digitproduct(num):
    digits = str(num)
    product = 1
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            product *= int(dgt)
    return product

def persistance(num):
    pers = 0
    while num > 9:
        num = digitproduct(num)
        pers += 1
    return pers

def displaypersistance(num):
    pers = 0
    print num,
    while num > 9:
        num = digitproduct(num)
        pers += 1
        print "->", num,
    print
    return pers

def countpersistances(max):
    counts = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in xrange(1,max+1):
        counts[persistance(i)] += 1
    return counts

def countdigits(numberOrString):
    # if numberOrString is 
    digits = str(numberOrString)
    founddecimalpt = False
    leading = True
    trailingzerocount = 0
    count = 0
    for dgt in digits:
        # 0 requires special handling
        if dgt == '0':
            # ignore leading zeros before the decimal point
            if not leading:
                count += 1
                if founddecimalpt:
                    # count number of consecuetive zeros after the decimal point
                    trailingzerocount += 1
        # digits other than 0
        elif dgt.isdigit():
            count += 1
            leading = False
            trailingzerocount = 0
        elif dgt == '.':
            founddecimalpt = True
            leading = False
            trailingzerocount = 0
        elif dgt == '+' or dgt == '-':
            pass # ignore
        else:
            print "Invalid character: %s" % dgt
    # ignore trailing zeros after the decimal point
    if trailingzerocount > 0:
        count -= trailingzerocount
    return count

def reversedigits(num):
    digits = str(num)
    rvrs = ""
    for dgt in digits:
        # print dgt,
        rvrs = dgt + rvrs
    return int(rvrs)

def sortdigits(num):
    digits = list(str(num))
    digits.sort()
    inorder = reduce(operator.add, digits)
    return inorder

def digitsalldiff(n):
    sortedstr = sortdigits(n)
    for i in xrange(len(sortedstr) - 1):
        if sortedstr[i] == sortedstr[i+1]:
            return False
    return True

def evaluateNum(num):
    print str(num)+": ",    # final comma prevents newline
    print "(" + str(sumdigits(num)) + ")",
    pfactor(num)
    print                   # writes a newline

def base16to10(hexnumstr):
    return int(str(hexnumstr), 16)

def base12to10(num):
    return int(str(num), 12)

def rebase(num, base):
    return int(str(num), base)

def zendo30231(koan):
    val = base12to10(koan)
    print val, "   ", val / 7.0

# interpret an integer or numeric string as "base -2" and convert to base 10
def baseneg2to10(num):
    digits = list(str(num))
    digits.reverse()
    placevals = [int(digits[i])*((-2)**i) for i in range(len(digits))]
    return sum(placevals)

def baseconvert(val,base):
    if base > 26:
        return "Error: base > 26"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basestr = ""
    while val > 0:
        rmndr = val % base
        val = val // base
        basestr = digits[rmndr] + basestr
    if basestr == "":
        basestr = "0"
    return basestr

def bases(num):
    print num, baseconvert(num,2), baseconvert(num,8), baseconvert(num,16)

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

def allbases():
    for i in range(2,10):
        print "Base %s" % i
        print "HAS: ",
        print map(lambda x: baseconvert(x,i), HAS)
        print "HASNOT: ",
        print map(lambda x: baseconvert(x,i), HASNOT)
        print

def factorsum(num):
    return reduce(operator.add, pfactorlist(num))

def printfactorsum(num):
    factors = pfactorlist(num)
    print num, factors, reduce(operator.add, factors)

def printfactorsums():
    print "::HAS::\n"
    map(printfactorsum, HAS)
    print "\n\n::HAS NOT::\n"
    map(printfactorsum, HASNOT)
    print "\n\n"

def pfactorstr(num):
    factors = ""
    for p in xrange(2,num):
        if num < 2:
            break
        while num % p == 0:
            factors += str(p) + " "
            num = num / p
    return factors

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

# here are our koans
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

