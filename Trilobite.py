# Trilobite.py
#
# will be an interpreter for the esolang Trilobite
# 
# Anthony Kozar
# April 7, 2025

def binaryOp1(op, x, y):
    return op[int(x)*3 + int(y)]

# FIXME: DOESN'T WORK IF width is smaller than length of x or y (and they are different lengths?)
def binaryOp(op, x, y, width=None, binaryOp1=binaryOp1):
    autowidth = False
    if width == None:
        autowidth = True
        width = max(len(x), len(y))
    sx = '0'*(width-len(x)) + x
    sy = '0'*(width-len(y)) + y
    res = "".join([binaryOp1(op,sx[i],sy[i]) for i in xrange(width)])
    if autowidth:
        return trimzeros(res)
    else:
        return res[-width:]

# returns (x+y)%3 for each trit
def KGS(x, y, width=None, binaryOp=binaryOp):
    return binaryOp("012120201", x, y, width)

# returns floor((x+y)/3) for each trit
def LI_(x, y, width=None, binaryOp=binaryOp):
    return binaryOp("000001011", x, y, width)

# check my algorithm for base-3 addition
