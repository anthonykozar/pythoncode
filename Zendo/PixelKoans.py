# PixelKoans.py
#
# Routines for working with Pixel koans

# Pixel koan input data format:
#    [id#, nature, pixel values]
#    id# is a unique integer (assigned by SDG)
#    nature is 1 for HAS, 0 for HAS NOT
#    pixel values is a string of letters representing colors
#      starting from the top left pixel with a slash '/'
#      separating each row
#
# E.g. [16281, 0, "WWBBB/BBWBB/BBBWW/BBBBB/BBBBB"]

class PixelKoan(object):
    def __init__(self, SDGid, nature, pixelstring):
        self.id = SDGid
        self.nature = bool(nature)
        self.setPixels(pixelstring)
    
    def setPixels(self, pixelstring):
        self._pixels = [list(e) for e in pixelstring.split('/')]
        self._pixelstring = pixelstring
        self.checkColumns()
    
    def checkColumns(self):
        #Note: str.split always produces an array with at least 1 element
        numcols = len(self._pixels[0])
        for row in self._pixels[1:]:
            if len(row) != numcols:
                raise ValueError, "Inconsistent row length in pixel data"
        self._cols = numcols
    
    def pixel(self, row, col):
        # rows and cols are numbered from 1!
        return self._pixels[row-1][col-1]
    
    def numRows(self):
        return len(self._pixels)
    
    def numCols(self):
        return self._cols
    
    rows = property(numRows)
    cols = property(numCols)

    def __str__(self):
        return self._pixelstring

    def __repr__(self):
        return "PixelKoan(%d,%d,'%s')" % (self.id, int(self.nature), self._pixelstring)


# Creates a dict of PixelKoan objects indexed by their SDG ids
# koanarray is a list of koan data in the input format described above. 
def KoanDataToDict(koanarray):
    koandict = {}
    for k in koanarray:
        koanid = k[0]
        koandict[koanid] = PixelKoan(*k)
    return koandict

# For each color in colors, counts how many HAS & HAS NOT koans have a pixel 
# of that color at (row,col).  colors can be a string or list of letters.
# Returns a tuple of 3 arrays: (hascounts, notcounts, totalcounts).
# Each array contains the counts for each color in the same order as colors. 
def CountColorsInCellPosition(koandict, colors, row, col):
    colors = list(colors)
    numcolors = len(colors)
    hascounts = [0] * numcolors
    notcounts = [0] * numcolors
    totalcounts = [0] * numcolors
    for koan in koandict.itervalues():
        try:
            color = koan.pixel(row, col)
            coloridx = colors.index(color)
            totalcounts[coloridx] += 1
            if koan.nature:
                # HAS koan
                hascounts[coloridx] += 1
            else:
                notcounts[coloridx] += 1
        except IndexError:
            pass  # ignore row or col out of range
        except ValueError:
            pass  # ignore color not in colors

    return (hascounts, notcounts, totalcounts)

def PrintCountsForCellPosition(koandict, colors, row, col):
    counts = CountColorsInCellPosition(koandict, colors, row, col)
    print "Cell (%d,%d)" % (row, col)
    print "       ",
    for c in colors: print "%3s" % c,
    print
    print "Has:   ",
    for i in counts[0]: print "%3d" % i,
    print
    print "Not:   ",
    for i in counts[1]: print "%3d" % i,
    print
    print "Total: ",
    for i in counts[2]: print "%3d" % i,
    print
    print


Zendo36463 = [
    [16226, 0, "WWWWW/WWWWW/WWWWW/WWWWW/WWWWW"],
    [16228, 0, "BBWBB/BBWBB/WWWWW/BBWBB/BBWBB"],
    [16238, 0, "BBBBB/BWBBB/BBWBB/BBBWB/BBBBB"],
    [16248, 0, "BBBBB/BBBWB/BBWBB/BWBBB/BBBBB"],
    [16277, 0, "BBBBB/WWBBB/BBWBB/BBBWW/BBBBB"],
    [16281, 0, "WWBBB/BBWBB/BBBWW/BBBBB/BBBBB"],
    [16296, 0, "BBBBB/BBWWW/BBWWW/BBWWW/BBBBB"],
    [16310, 0, "BBBBB/BBWBW/BBBWB/BBWBW/BBBBB"],
    [16317, 0, "BBWWW/BBWWW/BBWWW/BBBBB/BBBBB"],
    [16328, 0, "BBWBW/BBBWB/BBWBW/BBBBB/BBBBB"],
    [16342, 0, "BBBBB/BBBBB/WWWBB/WWWBB/WWWBB"],
    [16353, 0, "BBBBB/BBBBB/BBWBB/BBBWB/BBBBW"],
    [16371, 0, "BBBBB/BBBBB/WBWBB/BWBBB/WBWBB"],
    [16415, 0, "BBBBB/BBBBB/BBWBW/BBBWB/BBWBW"],
    [16477, 0, "BBBWB/BBBBB/BBBBB/BBBBB/BBBBB"],
    [16478, 0, "BBBWW/BBBBW/BBBBW/WBBBW/WBBWB"],
    [16524, 0, "WWWWW/WBWBW/WWBWW/WBWBW/WWWWW"],
    [16532, 0, "WWWWB/WWWWW/WWWWW/WWWWW/WWWWW"],
    [16549, 0, "BBBWB/BBBBW/BBBBB/BBBBW/BBBWB"],
    [16563, 0, "BWWWW/WBWWW/WWBWW/WWWWW/WWWWW"],
    [16569, 0, "BBBBB/BBBBB/BBBBB/BBBBB/BBBWB"],
    [16620, 0, "WWWBB/WWWBB/WWWBB/WWWBB/WWWBB"],
    [16643, 0, "BBBWB/BBBWB/BBBWB/WWWBW/BBBWB"],
    [16687, 0, "WWWBW/WWWBW/WWWWW/BBWWW/WWWWW"],
    [16690, 0, "BBBBB/BWBWB/BBWBW/BWBWB/BBWBW"],
    [16700, 0, "BBBBB/BWBWB/BBWBB/BBBWB/BBBBB"],
    [16702, 0, "BBBBB/BBBBB/BBWBB/BWBBB/WBBBB"],
    [16737, 0, "BBBBB/BBBBB/BBBBB/BBBBW/BBBWB"],
    [16740, 0, "BBBBB/BBBBB/WBBBB/BWBBB/BBWBB"],
    [16763, 0, "BBBBB/BBWBB/BWBBB/WBBBB/BBBBB"],
    [16776, 0, "WWWBW/WWWWB/WWBWW/BWWWB/WBWBW"],
    [16225, 1, "BBBBB/BBBBB/BBBBB/BBBBB/BBBBB"],
    [16227, 1, "BBBBB/BWBWB/BBWBB/BWBWB/BBBBB"],
    [16256, 1, "WBWBB/BWBBB/WBWBB/BBBBB/BBBBB"],
    [16267, 1, "BBBBB/BBBBB/BBWBB/BBBBB/BBBBB"],
    [16286, 1, "BBBBB/BWBBB/BBWBB/BBBBB/BBBBB"],
    [16288, 1, "BBBBB/BWWWB/BWWWB/BWWWB/BBBBB"],
    [16320, 1, "BBBBB/BBBBB/BBBBB/BBBBB/BWWBB"],
    [16367, 1, "BBBBB/BWBWB/BBWBB/BBBBB/BBBBB"],
    [16375, 1, "BWBBB/BBBBB/BBBBB/BBBBB/BBBBB"],
    [16402, 1, "BBBBB/BWBWB/BBWWB/BWWWB/BBBBB"],
    [16417, 1, "BBWBB/BBBBB/BBBBB/BBBBB/BBBBB"],
    [16418, 1, "BBBBB/BWBWB/BBWBB/BWBWB/BBBBW"],
    [16472, 1, "WWWBB/WWWBB/WWWBB/BBBBB/BBBBB"],
    [16493, 1, "WBBBB/BWBBB/BBWBB/BBBBB/BBBBB"],
    [16498, 1, "BBBBB/BBBBB/BBBBB/BBBBB/BWBBB"],
    [16500, 1, "BBBBW/BBBBB/BBBBB/BBBBB/BBBBB"],
    [16507, 1, "BBWBB/BBWBB/WWBWW/BBWBB/BBWBB"],
    [16550, 1, "BBBBB/BBBBW/BBBBB/BBBBB/BBBBB"],
    [16605, 1, "BBBBB/WBBBB/BBBBB/BBBBB/BBBBB"],
    [16684, 1, "BBBBB/BWBBB/BBBBB/BBBBB/BBBBB"],
    [16722, 1, "BBBBB/BWBWB/BBWBB/BWBBB/BBBBB"],
    [16742, 1, "WWWWB/WWWWB/WWWWB/WWWWB/BBBBB"],
    [16793, 1, "WWWBB/WWWWB/WWBWB/BWWWB/BBBBB"]
]

koans = KoanDataToDict(Zendo36463)
