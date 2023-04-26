# Zendo #36762

import operator

def digitset(n):
    s = str(n)
    digits = ""
    for d in xrange(10):
        sd = str(d)
        if sd in s:
            digits += sd
    return digits

HAS = [653, 1829, 1927, 2918, 4096, 7192, 8192, 19683, 32768, 35556,
       65536, 270131, 409600000, 88888888199999999922]

HASNOT = [19, 32, 82, 216, 567, 625, 1234, 2048, 2401, 4211,
          6192, 8208, 8402, 9192]

def pow2digitsets(maxpow, printshortsets = False):
    a = []
    n = 0
    twoN = 1
    while n <= maxpow:
        digits = digitset(twoN)
        if printshortsets and len(digits) < 5:
            print "%6d  %31d  %s" % (n, twoN, digits)
        a.append(digits)
        n += 1
        twoN *= 2
    return a

def sortchars(s):
    chars = list(s)
    chars.sort()
    return reduce(operator.add, chars)

def Draw5sGuess(koans):
    sets = pow2digitsets(31)
    for k in koans:
        digits = digitset(k)
        if digits in sets:
            print k, digits
        else:
            digmod = sortchars(digits.replace('7', '8'))
            if digmod in sets:
                print k, digmod
            else:
                digmod = sortchars(digits.replace('9', '4'))
                if digmod in sets:
                    print k, digmod
                else:
                    digmod = sortchars(digits.replace('5', '6'))
                    if digmod in sets:
                        print k, digmod
    return

# The last N digits of powers of 2 are cyclic beginning
# with 2^N and having a period of 4*5^(N-1).  See
# https://www.exploringbinary.com/patterns-in-the-last-digits-of-the-positive-powers-of-two/
# for more details.

# Returns an array of the complete cycle of last N digits of powers of 2
def pow2lastdigits(lastNdigits):
    a = []
    mod = 10**lastNdigits
    twoN = 2**lastNdigits  # 2**N is always < 10**N
    period = 4 * 5**(lastNdigits-1)
    for n in xrange(period):
        a.append(twoN)
        twoN = (2*twoN) % mod
    return a

def zeropad(n, length):
    s = str(n)
    pad = length - len(s)
    if pad > 0:
        s = '0'*pad + s
    return s

# Find all digit sets of last N digits of pow2 that contain fewer than M distinct elements
def smallsets(N, M):
    return filter(lambda x: len(x) < M, map(lambda n: digitset(zeropad(n,N)), pow2lastdigits(N)))

# Return an array containing only the unique elements of arr.
# Input: arr should be a sorted array
def unique(arr):
    newarr = []
    if len(arr) > 0:
        last = None
        for e in arr:
            if e != last:
                newarr.append(e)
                last = e
    return newarr

# Returns a list of the digits in num
def digitlist(num):
    return map(int, str(num))

# Count the number of unique values btw 0-9 in arr 
def countuniquedigits(arr):
    hasdigit = [False]*10
    for d in arr:
        hasdigit[d] = True
    count = 0
    for b in hasdigit:
        if b:  count += 1
    return count

# Find the maximum # of final digits of num with fewer than M distinct elements.
def findmaxfinaldigits(num, M):
    digits = digitlist(num)
    numdigits = len(digits)
    numunique = 0
    ndigits = 1
    while (numunique < M and ndigits <= numdigits):
        numunique = countuniquedigits(digits[numdigits-ndigits:])
        # print numdigits, ndigits, digits[numdigits-ndigits:], numunique
        if numunique == M:
            return ndigits-1
        ndigits += 1
    return ndigits-1

# Search for large powers of 2 where the last N digits contain fewer than M distinct elements.
# (Just prints results instead of creating a huge array like pow2lastdigits() above).
def search4smallsets(startpower, endpower, minN, maxN, M):
    mod = 10**maxN
    curpow = startpower
    twoN = 2**startpower          # 2**N is always < 10**N
    while (curpow <= endpower):
        maxdigits = findmaxfinaldigits(twoN, M)
        if (maxdigits >= minN):
            lastdigits = twoN % (10**maxdigits)
            print "2^%d ends with %d unique out of %d digits ...%d" % (curpow, M-1, maxdigits, lastdigits)
        twoN = (2*twoN) % mod     # only retain the last maxN digits
        curpow += 1
    return
