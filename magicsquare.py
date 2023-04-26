# Magic Square Solvers

# Anthony Kozar
# June 18, 2012

import copy

# This is a very naive approach to solving a 3x3 magic square.
# I am implementing it because I want to use a backtracking
# algorithm to solve some problem.

gNumSquaresChecked = 0

def solvemagicsquare3(displaysearch = False, debug = False):
    global gNumSquaresChecked
    gNumSquaresChecked = 0
    sqrvalues = [[0,0,0],[0,0,0],[0,0,0]]
    solution, found = backtracksearchsquare3(sqrvalues, 0, 0, displaysearch, debug)
    print "Checked", gNumSquaresChecked, "possible squares."
    if found:
        print "A solution is ", solution
    else:
        print "No solution found!"
    return found

def backtracksearchsquare3(sqrval, row, col, displaysearch = False, debug = False):
    sqrcopy = copy.deepcopy(sqrval)
    newval = sqrcopy[row][col]
    # try all values between 1 and 9 that are not already in use
    while newval < 9:
        newval += 1
        if not sqrcontainsvalue(sqrcopy, newval):
            if debug:
                print "Incrementing row: ", row, "col: ", col           
            sqrcopy[row][col] = newval
            if displaysearch:
                print "Checking square ", sqrcopy
            allmatch, sqrIsFull = checksums3(sqrcopy)
            if allmatch and sqrIsFull:
                return sqrcopy, True
            elif allmatch and not sqrIsFull:
                # move to next column or row
                newrow = row
                newcol = col + 1
                if newcol == 3:
                    newcol = 0
                    newrow = row + 1
                    if newrow == 3:
                        # all values filled-in but no solution found!
                        return sqrcopy, False
                if debug:
                    print "newrow: ", newrow, "newcol: ", newcol
                # search for next value
                solution, found = backtracksearchsquare3(sqrcopy, newrow, newcol, displaysearch, debug)
                if found:
                    # this square works!, so pass it back up
                    return solution, found
            elif not allmatch:
                # newval doesn't work in this square, so continue 
                # trying new values in current row and col
                continue
        # else skip newval
    
    # if we have tried all values for this row and col without success,
    # then we need to backtrack
    return sqrcopy, False

def sqrcontainsvalue(sqrval, val):
    for row in range(3):
        for col in range(3):
            if sqrval[row][col] == val:
                return True
    return False

# checksums3() can check a partially-filled-in 3x3 square to
# see if its sums all match.  Rows, columns, and diagonals
# containing a 0 (zero) are not checked.  checksums3() returns
# two boolean values: whether all sums match, and whether all
# sums in the square were checked.
def checksums3(sqrval, debug = False):
    global gNumSquaresChecked
    gNumSquaresChecked += 1
    if (gNumSquaresChecked % 1000) == 0:
        print gNumSquaresChecked
    sumtomatch = 0
    allsumschecked = True
    allsumsmatch = True
    # check the horizontal rows
    for row in range(3):
        rowsum = 0
        skipthissum = False
        for col in range(3):
            # if any value in the row is 0, skip this sum
            if sqrval[row][col] == 0:
                skipthissum = True
                allsumschecked = False
                if debug:
                    print "Skipping row ", row
                break
            else:
                rowsum += sqrval[row][col]
        if skipthissum == True:
            continue
        if sumtomatch == 0:
            # this is the first sum, so just set value to match
            sumtomatch = rowsum
        else:
            if rowsum != sumtomatch:
                if debug:
                    print "Non-matching sum in row ", row, rowsum, sumtomatch
                return False, False

    # check the vertical columns
    for col in range(3):
        colsum = 0
        skipthissum = False
        for row in range(3):
            # if any value in the column is 0, skip this sum
            if sqrval[row][col] == 0:
                skipthissum = True
                allsumschecked = False
                if debug:
                    print "Skipping column ", col
                break
            else:
                colsum += sqrval[row][col]
        if skipthissum == True:
            continue
        if sumtomatch == 0:
            # this is the first sum, so just set value to match
            sumtomatch = colsum
        else:
            if colsum != sumtomatch:
                if debug:
                    print "Non-matching sum in column ", col, colsum, sumtomatch
                return False, False

    # check the tl-br diagonal
    diagsum = 0
    skipthissum = False
    for row in range(3):
        # if any value in the diagonal is 0, skip this sum
        if sqrval[row][row] == 0:
            skipthissum = True
            allsumschecked = False
            if debug:
                print "Skipping tl-br diagonal"
            break
        else:
            diagsum += sqrval[row][row]
    if not skipthissum:
        if sumtomatch == 0:
            # this is the first sum, so just set value to match
            sumtomatch = diagsum
        else:
            if diagsum != sumtomatch:
                if debug:
                    print "Non-matching sum in tl-br diagonal ", diagsum, sumtomatch
                return False, False

    # check the tr-bl diagonal
    diagsum = 0
    skipthissum = False
    for row in range(3):
        # if any value in the diagonal is 0, skip this sum
        if sqrval[row][2-row] == 0:
            skipthissum = True
            allsumschecked = False
            if debug:
                print "Skipping tr-bl diagonal"
            break
        else:
            diagsum += sqrval[row][2-row]
    if not skipthissum:
        if sumtomatch == 0:
            # this is the first sum, so just set value to match
            sumtomatch = diagsum
        else:
            if diagsum != sumtomatch:
                if debug:
                    print "Non-matching sum in tr-bl diagonal ", diagsum, sumtomatch
                return False, allsumschecked

    if debug:
        print "All sums are equal to ", sumtomatch
    return allsumsmatch, allsumschecked
