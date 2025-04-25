# Trilobite.py
#
# will be an interpreter for the esolang Trilobite
# 
# Anthony Kozar
# April 7, 2025

from numbases import baseconvert

BASE = 3

def createmaps(chars, base = BASE, width = 3, baseconvert = baseconvert):
    ch2num = {}
    num2ch = {}
    for i in xrange(len(chars)):
        numstr = baseconvert(i, base).zfill(width)
        ch2num[chars[i]] = numstr
        num2ch[numstr] = chars[i]
    return ch2num, num2ch

# make maps between the "operator characters" and base-3 numbers
OPALPHABET = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
OPCHARMAP, OPNUMMAP = createmaps(OPALPHABET)

# Convert a Trilobite name into an operator table
def name2op(name, OPCHARMAP = OPCHARMAP):
    numseq = [OPCHARMAP[c] for c in name]
    return "".join(numseq)[::-1]

# Convert an operator table into a Trilobite operator name
def op2name(op, width = 3, OPNUMMAP = OPNUMMAP):
    oprev = op[::-1]
    numseq = [oprev[i:i+width] for i in xrange(0, len(oprev), width)]
    charseq = [OPNUMMAP[s] for s in numseq]
    return "".join(charseq)

def trimzeros(numstr):
    return numstr.lstrip('0')

def binaryOp1(op, x, y):
    return op[int(x)*BASE + int(y)]

# FIXME: DOESN'T WORK IF width is smaller than length of x or y (and they are different lengths?)
def binaryOp(op, x, y, width=None, binaryOp1=binaryOp1):
    autowidth = False
    if width == None:
        autowidth = True
        width = max(len(x), len(y))
    sx = x.zfill(width)
    sy = y.zfill(width)
    res = "".join([binaryOp1(op,sx[i],sy[i]) for i in xrange(width)])
    if autowidth:
        return trimzeros(res)
    else:
        return res[-width:]

# returns (x+y)%3 for each trit
def KGU(x, y, width=None, binaryOp=binaryOp):
    return binaryOp("012120201", x, y, width)

# returns floor((x+y)/3) for each trit
def LI_(x, y, width=None, binaryOp=binaryOp):
    return binaryOp("000001011", x, y, width)

# Shift the trits of val left n positions, padding with zeros on the right.
def SHIFTL(val, n, width=None):
    return val + '0'*n

# Check my algorithm for base-3 addition:
# DEFINE(add, (x,y), 
#   SELECT(TESTNZ(y, Z(y)), x, 
#     add(KGU(x,y), SHIFTL(LI_(x,y),1)), 
#     add(KGU(x,y), SHIFTL(LI_(x,y),1))))
def add3(x, y, width=None):
    if y == '0' * len(y):
        return x
    else:
        return add3(KGU(x, y, width),
            SHIFTL(LI_(x, y, width), 1, width))

RUNTESTS = 4

def testadd(m, n):
    m3 = baseconvert(m, BASE)
    n3 = baseconvert(n, BASE)
    r3 = add3(m3, n3)
    r = int(r3, BASE)
    return (m3, n3, r3, r)

if RUNTESTS & 1:
    print add3('2'*27, '1')
    
if RUNTESTS & 2:
    truecount = 0
    falsecount = 0
    for m in xrange(729):
        for n in xrange(729):
            m3, n3, r3, r = testadd(m, n)
            if r != m+n:
                print m,n,m3,n3,r3,r
                falsecount += 1
            else:
                truecount += 1
    print "Equal:", truecount, "Not equal:", falsecount

if RUNTESTS & 4:
    from random import randrange
    for i in xrange(20):
        m = randrange(1, int('1000000', BASE))
        n = randrange(1, int('1000000', BASE))
        m3, n3, r3, r = testadd(m, n)
        print m,n,m3,n3,r3,r, r == m+n
