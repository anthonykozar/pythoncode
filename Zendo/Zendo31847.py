Zendo31847Has = [
[[0,0,0], [0,0,0], [0,0,0]], 
[[0,0,0], [0,1,0], [0,0,0]], 
[[1,0,0], [0,0,0], [0,0,0]], 
[[1,0,0], [0,1,0], [0,0,0]], 
[[1,0,0], [0,1,0], [1,1,0]], 
[[1,0,0], [0,1,0], [3,0,0]], 
[[1,0,0], [0,1,0], [4,4,0]], 
[[1,0,0], [1,1,0], [0,1,0]], 
[[1,0,0], [2,0,0], [0,0,1]], 
[[1,0,2], [0,1,2], [0,0,0]], 
[[1,0,3], [0,1,2], [0,0,0]], 
[[1,1,0], [0,0,1], [1,1,1]], 
[[1,1,0], [0,1,1], [1,2,1]], 
[[1,1,0], [0,1,2], [0,0,0]], 
[[1,1,0], [0,1,2], [1,2,2]], 
[[1,1,1], [1,1,1], [1,1,1]], 
[[1,1,1], [1,1,1], [4,4,4]], 
[[1,1,1], [2,2,2], [2,2,2]], 
[[1,1,1], [2,2,2], [3,3,3]], 
[[1,2,1], [2,4,2], [3,2,1]], 
[[1,2,3], [1,2,3], [1,2,3]], 
[[1,2,3], [3,2,1], [4,4,4]], 
[[1,4,0], [0,0,1], [0,0,0]], 
[[2,0,0], [0,2,0], [4,0,0]], 
[[2,0,0], [1,0,0], [0,0,1]], 
[[2,2,2], [2,2,2], [2,2,2]], 
[[2,2,2], [3,3,3], [4,4,4]], 
[[3,0,0], [0,3,0], [0,0,0]], 
[[3,3,3], [3,3,3], [3,3,3]], 
[[4,0,0], [0,4,0], [1,0,0]], 
[[4,4,4], [1,1,1], [1,2,3]], 
[[4,4,4], [4,4,4], [4,4,4]], 
]

Zendo31847HasNot = [
[[0,0,1], [0,1,0], [1,0,0]], 
[[0,1,1], [2,1,0], [3,3,4]], 
[[0,1,1], [2,1,3], [3,3,1]], 
[[0,1,2], [1,2,3], [2,3,4]], 
[[0,1,2], [3,0,1], [2,3,0]], 
[[0,2,0], [1,0,0], [2,4,0]], 
[[0,2,0], [2,4,0], [1,0,0]], 
[[1,0,0], [0,1,0], [0,0,1]], 
[[1,0,0], [0,1,0], [2,1,0]], 
[[1,0,0], [0,1,0], [2,2,0]], 
[[1,0,0], [0,2,0], [2,4,0]], 
[[1,0,1], [0,1,1], [2,2,4]], 
[[1,0,2], [0,1,2], [2,2,3]], 
[[1,1,0], [0,1,1], [1,0,1]], 
[[1,1,0], [0,1,2], [2,4,4]], 
[[1,1,0], [0,1,2], [3,1,1]], 
[[1,1,0], [0,1,2], [4,3,3]], 
[[1,1,0], [3,1,2], [1,0,1]], 
[[1,2,3], [2,3,1], [3,1,2]], 
[[2,0,0], [0,1,0], [0,0,1]], 
[[2,0,0], [0,2,0], [0,0,2]], 
[[2,1,1], [1,3,1], [2,1,3]], 
[[2,3,2], [3,0,3], [4,3,2]], 
[[2,3,4], [1,1,0], [0,1,4]], 
[[2,4,0], [0,2,0], [1,0,0]], 
[[2,4,0], [1,0,0], [0,2,0]], 
[[3,0,0], [0,3,0], [0,0,3]], 
[[3,1,0], [0,3,0], [4,0,0]], 
[[3,1,1], [1,3,1], [1,1,3]], 
[[4,0,0], [0,4,0], [0,0,4]], 
[[4,0,1], [1,4,0], [0,1,4]], 
]

import numpy as np
from numpy.linalg import det as det

# hasmatrices = map(np.array, Zendo31847Has)

# make an augmented matrix from the input with constants of zero
def augment(matrix):
    augmented = list()
    for row in matrix:
        augrow = list(row)
        augrow.append(0)
        augmented.append(augrow)
    return augmented

# print the determinants and traces of a list of matrices
def dets_traces(matrices):
    for m in matrices:
        matrix = np.array(m)
        # using %4.0f instead of %4d prevents rounding errors!
        print "%s  %4.0f  %4.0f" % (m, det(matrix), np.trace(matrix))

# print the ranks of a list of matrices & ranks of their augmented matrices
def ranks(matrices):
    for m in matrices:
        matrix = np.array(m)
        b = np.array([0,0,0])
        sol = np.linalg.lstsq(matrix, b) # returns a 4-tuple
        rank = sol[2] # rank is the 3rd value
        augmatrix = augment(matrix)
        sol = np.linalg.lstsq(augmatrix, b)
        augrank = sol[2]
        print "%s  %4.0f  %4.0f" % (m, rank, augrank)

def sortmatrixelements(matrix):
    elems = [x[i] for x in matrix for i in range(len(x))]
    elems.sort()
    return elems

# returns rowa - rowb (where rowa & rowb are 3-element vectors, mod 5)
def subrows(rowa, rowb):
    result = [0,0,0]
    for i in range(3):
        result[i] = (rowa[i] - rowb[i]) % 5
    return result

# returns scalar*row (where row is a 3-element vector, mod 5)
def scalerow(row, scalar):
    result = [0,0,0]
    for i in range(3):
        result[i] = (row[i] * scalar) % 5
    return result

def checkhypothesis(matrices):
    for m in matrices:
        matchesHypothesis = False
        otherrows = [[1,2],[0,2],[0,1]]
        for rownum in range(3):
            r1 = m[rownum]
            r2 = m[otherrows[rownum][0]]
            r3 = m[otherrows[rownum][1]]
            for i in range(5):
                for j in range(5):
                    if (i+j < 5):
                        # calculate r1 - i*r2 - j*r3
                        result = subrows(subrows(r1,scalerow(r2,i)), scalerow(r3,j))
                        print i, j, result
                        if result == [0,0,0]:
                            print m, "r1 - %d*r2 - %d*r3 == [0,0,0]" % (i,j)
                            matchesHypothesis = True
                            break
                if matchesHypothesis: break
            if matchesHypothesis: break

# returns the number of elements in matrix that match value
def countmatchingelements(matrix, value):
    count = 0
    for row in matrix:
        for elem in row:
            if elem == value:
                count += 1
    return count

def printrowsums(matrices):
    for m in matrices:
         sums = map(sum, m)
         sums = map(lambda x: x%5, sums)
         print m, "  ", sums

