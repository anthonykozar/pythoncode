# An algorithm to randomly tile rectangles with 1x2 bricks.
# Doesn't always work yet as it sometimes isolates one of the bottom corner squares so that a brick cannot be placed there. Would it always work if this issue was fixed?

def randombricks(width, height):
    import random
    def placevertical(bricks, row, col, tryHoriz = False):
        if bricks[row][col] == ' ' and bricks[row+1][col] == ' ':
            bricks[row][col] = '^'
            bricks[row+1][col] = 'v'
            return True
        elif tryHoriz:
            return placehorizontal(bricks, row, col)
        else:
            print "placevertical(%d,%d) failed" % (row,col)
            return False
    
    def placehorizontal(bricks, row, col, tryVert = False):
        if bricks[row][col] == ' ' and bricks[row][col+1] == ' ':
            bricks[row][col] = '<'
            bricks[row][col+1] = '>'
            return True
        elif tryVert:
            return placevertical(bricks, row, col)
        else:
            print "placehorizontal(%d,%d) failed" % (row,col)
            return False
    
    # create a 2D array of spaces
    bricks = []
    for row in xrange(height):
        bricks.append([' '] * width)
    # iterate over the diagonals, adding bricks with random orientations
    numdiag = 2*width - 1
    for diag in xrange(numdiag):
        diaglen = min(diag+1, numdiag-diag)
        firstrow = max(0, diag-width+1)
        for row in xrange(firstrow, firstrow + diaglen):
            col = diag - row
            if bricks[row][col] == ' ':
                if col == width-1:
                    placevertical(bricks, row, col)
                elif row == height-1:
                    placehorizontal(bricks, row, col)
                else:
                    placef = random.choice([placevertical, placehorizontal])
                    placef(bricks, row, col,  True)
    return bricks

def printbricks(bricks):
    for row in bricks:
        print ''.join(row)
