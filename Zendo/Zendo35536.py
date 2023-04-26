from factor import *

# Zendo #35536
HAS = [10103,10111,10211,10301,10501,10601,10711,11003,11113,11213,20101,21019,
       21023,21031,21101,41223,50119,51031,61001,101117,101119,111229,211129,1011001,
       9090919,10011101,17360207,17360227,18860131,63971203,85110917,85110923]
HASNOT = [10007,10061,10133,10139,10141,10399,11131,11311,12527,20023,20231,22229,
          23011,27103,29101,30011,31033,43013,44101,50021,50023,50051,
          50077,50159,56783,70999,90031,
          100003,103123,532333,576001,600011,1011137,1111151,
          7071619,8071319,8071619,8511091,
          17360237,17360257,17360267,17362207,18810229,
          82436227,85000007,99999113,99999971,99999989]

HASNOT_other = [1,2,3,8888,10113,20204,26101,30101,1234567,5323333,28406943,
                71901158,85110916]

def MapHas_HasNot(fn, has = HAS, hasnot = HASNOT):
    print 'HAS'
    print '-------'
    map(fn, has)
    print ''
    print 'HAS NOT'
    print '-------'
    map(fn, hasnot)

def last4digits(num):
    return num % 10000

def last3digits(num):
    return num % 1000

def last2digits(num):
    return num % 100

def mod16(num):
    return num % 16

def rule(n):
    return 10000 - 5*last4digits(n) + 40*last3digits(n) - 300*last2digits(n)

def buildhashtable(hashfunc, arr):
    table = {}
    for i in arr:
        key = hashfunc(i)
        if table.has_key(key):
            table[key].append(i)
        else:
            table[key] = [i]
    return table

def printhashtable(table, title = ""):
    if title:
        print "%s:" % title
    keys = table.keys()
    keys.sort()
    for k in keys:
        print k, "==>", table[k]
    print

# print tables of koans sorted by last 4, 2, and 3 digits
has4table = buildhashtable(last4digits, HAS)
not4table = buildhashtable(last4digits, HASNOT)
printhashtable(has4table, "HAS")
printhashtable(not4table, "NOT")
has2table = buildhashtable(last2digits, HAS)
not2table = buildhashtable(last2digits, HASNOT)
printhashtable(has2table, "HAS")
printhashtable(not2table, "NOT")
has3table = buildhashtable(last3digits, HAS)
not3table = buildhashtable(last3digits, HASNOT)
printhashtable(has3table, "HAS")
printhashtable(not3table, "NOT")


######### OLD CODE ###########

# Returns a list of the digits in odd-numbered places starting from the right.
def oddplacedigits(num):
    numstr = str(num)
    numdigits = len(numstr)
    return [int(numstr[i]) for i in xrange(numdigits-1, -1, -2)]

# Returns a list of the digits in even-numbered places starting from the right.
def evenplacedigits(num):
    numstr = str(num)
    numdigits = len(numstr)
    return [int(numstr[i]) for i in xrange(numdigits-2, -1, -2)]

def printOddEvenPlaceSums(num):
    print str(num)+": ", sum(oddplacedigits(num)), sum(evenplacedigits(num))

def printOddEvenPlaceSumsMinMax(num):
    print ("%8s: " % str(num)), sum(oddplacedigits(num)), sum(evenplacedigits(num)),
    print min(oddplacedigits(num)), max(evenplacedigits(num))

# MapHas_HasNot(printOddEvenPlaceSumsMinMax, HAS, filter(isprime, HASNOT))
