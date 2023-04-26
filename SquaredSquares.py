# Routines for generating the "tablecode" describing
# squared squares and rectangles.
#
# Anthony Kozar
# Aug. 16, 2022

# This code represents squared squares and rectangles as
# lists of tuples.  A square is a 3-tuple (x, y, sidelength)
# where x and y are the positions of the top-left corner of
# the square relative to the top-left corner of the entire figure
# which is (0,0).  A rectangle is a 4-tuple (x, y, width, height).

def compareSqrsRects(r1, r2):
    # compare Y coords
    if r1[1] < r2[1]:
        return -1          # r1 < r2
    elif r1[1] > r2[1]:
        return 1           # r1 > r2
    else:                  # r1.y == r2.y
        # compare X coords
        if r1[0] < r2[0]:
            return -1      # r1 < r2
        if r1[0] > r2[0]:
            return 1       # r1 > r2
        else:
            return 0       # r1 == r2

# Grid dissection divides a square into N X N smaller, equal squares.

# An "L-dissection" creates small squares along the top & left edges and
# one large square filling the bottom-right of the original square.
def Ldissection(sqr, subdivisions):
    if subdivisions < 2:
        return [sqr]
    left, top, side = sqr
    smside, rem = divmod(side, subdivisions)
    if rem != 0:
        raise ValueError, "subdivisions %d does not divide side length %d" % (subdivisions, side)
    subsqrs = [(left, top, smside), (left + smside, top + smside, (subdivisions-1)*smside)]
    for i in xrange(1, subdivisions):
        subsqrs.append((left + i*smside, top, smside))
        subsqrs.append((left, top + i*smside, smside))
    return subsqrs

##def Ldissection(levels, rowsum = 0):
##    for row in range(levels):
##        rowsum = 0
##        sqrsize = 120/(levels-row)
##        print sqrsize,
##        rowsum += sqrsize
##        if row == 0:
##            while rowsum < 120:
##                print sqrsize,
##                rowsum += sqrsize
##            print
##        else:

# An "O-dissection" creates small squares along all four edges and
# one large square filling the center of the original square.
def Odissection(sqr, divs):
    left, top, side = sqr
    right = left + side
    bottom = top + side
    smside = side / divs
    subsqrs = [(left + smside, top + smside, (divs-2)*smside)]
    for i in xrange(divs-1):
        ltoff = i*smside
        rboff = (i+1)*smside
        subsqrs.append((left + ltoff, top, smside))
        subsqrs.append((right - smside, top + ltoff, smside))
        subsqrs.append((right - rboff, bottom - smside, smside))
        subsqrs.append((left, bottom - rboff, smside))
    return subsqrs

# A "cross-dissection" creates small squares in a plus-sign shape
# along the horizontal & vertical lines passing thru the center of
# the original square.  Four equal squares are left in the corners.
def crossdissection(sqr, divs, divsize = 1):
    left, top, side = sqr
    smside = side / divs
    subsqrs = []
    
    return subsqrs

def sqrsize(sqr):
    return sqr[2]

def sqrleft(sqr):
    return sqr[0]

def sqrtop(sqr):
    return sqr[1]

def sqrright(sqr):
    return sqr[0] + sqr[2]

def sqrbottom(sqr):
    return sqr[1] + sqr[2]

def largestsqr(sqrs):
    return max(sqrs, key=sqrsize)

def replacesubsqr(sqrs, subsqr, replacement):
    sqrs.remove(subsqr)
    sqrs += replacement
    return sqrs

def shiftsqrs(sqrs, xoffset, yoffset):
    return [(s[0]+xoffset,s[1]+yoffset,s[2]) for s in sqrs]

def scalesqrs(sqrs, factor, pincorner = False):
    if not pincorner:
        return [(s[0]*factor, s[1]*factor, s[2]*factor) for s in sqrs]
    else:
        leftbound = sqrleft(min(sqrs, key=sqrleft))
        topbound = sqrtop(min(sqrs, key=sqrtop))
        return [((s[0]-leftbound)*factor + leftbound,
                 (s[1]-topbound)*factor + topbound,
                 s[2]*factor) for s in sqrs]

def sqrs2tablecode(sqrs):
    sqrs.sort(compareSqrsRects)
    numsqrs = len(sqrs)
    totalwidth = sqrright(max(sqrs, key=sqrright)) - sqrleft(min(sqrs, key=sqrleft))
    totalheight = sqrbottom(max(sqrs, key=sqrbottom)) - sqrtop(min(sqrs, key=sqrtop))
    sizes = map(sqrsize, sqrs)
    tcode = ("%d %d %d " % (numsqrs, totalwidth, totalheight)) + " ".join(map(str, sizes))
    return tcode
