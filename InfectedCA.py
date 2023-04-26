# A simple cellular automaton simulating the spread of a disease.
# See this video @ 1:53 - https://www.youtube.com/watch?v=PbJaOaXthhk
#
# Feb. 16, 2023

# number the cells of a 5x5 grid from 0 to 24
a = []
b = []
for i in xrange(25):
    b.append(i)
    if i%5 == 4:
        a.append(b)
        b = []

# make a map from the cell numbers to lists of their orthogonally adjacent cells
adj = []
for r in xrange(5):
    for c in xrange(5):
        j = []
        if r > 0:
            j.append(a[r-1][c])
        if c > 0:
            j.append(a[r][c-1])
        if c < 4:
            j.append(a[r][c+1])
        if r < 4:
            j.append(a[r+1][c])
        adj.append(j)

# A simple cellular automaton simulating the spread of a disease.
# '1' = Infected cell, '0' = uninfected cell
# Rules:
#   Infected cells always remain infected in the next step.
#   An uninfected cell becomes infected if it has at least two
#   orthogonally adjacent neighbors that are infected.
#
# It's known to be impossible to infect all cells of a 5x5 grid
# starting with fewer than 5 infected cells.  Questions:
#   1. Is having at least one infected cell in every row and column
#   a necessary condition to infect the entire grid?
#   2. Is it a sufficient condition?

# Simulate one step of the spreading infection
# States are represented as strings of 25 zeros and ones.
def spread(state, adjacencies = adj):
    newstate = ""
    for i in xrange(len(state)):
        if state[i] == '1':
            newstate += '1'
        else:
            infected = sum(map(lambda j: int(state[j]), adjacencies[i]))
            if infected >= 2:
                newstate += '1'
            else:
                newstate += '0'
    return newstate

# A couple of example states
fourcorners = '0000001010000000101000000'
diagonal = '1000001000001000001000001'

# Print a state string as a 5x5 grid
def prstate(state):
    for i in xrange(0, 25, 5):
        print state[i:i+5]

# Run the simulation until there is no change in the state.
def simulate(startstate, printstates = True):
    laststate = ""
    curstate = startstate
    if printstates:
        prstate(curstate)
        print
    while laststate != curstate:
        laststate = curstate
        curstate = spread(curstate)
        if printstates:
            prstate(curstate)
            print
    return curstate

# The answer to question 2 is no.  This state is completely inert:
# 00100
# 10000
# 00001
# 01000
# 00010
inert = '0010010000000010100000010'

###############

# Simulate every combination of 5 infected cells to answer question 1.
# (I don't worry about duplicates due to symmetry since there are only
# 53,130 combinations).
allinfected = '1111111111111111111111111'

# Check if a state meets the condition of having at least one infected
# cell in every row and column.
def checkhypothesis(state):
    rows = set()
    cols = set()
    for i in range(len(state)):
        if state[i] == '1':
            rows.add(i//5)
            cols.add(i%5)
    complete = set(range(5))
    return rows == complete and cols == complete

# Convert a list of infected cell numbers to a state string
def infectedlist2state(infectedcells, numstates = 25):
    st = ''
    for i in xrange(numstates):
        if i in infectedcells:
            st += '1'
        else:
            st += '0'
    return st

from itertools import combinations

def checkcombos(numinfected, numstates = 25):
    hypall = []
    hypallcnt = 0
    hypnotcnt = 0
    nohypallcnt = 0
    nohypall = []
    for s in combinations(xrange(numstates), numinfected):
        st = infectedlist2state(s)
        hyptrue = checkhypothesis(st)
        finalstate = simulate(st, False)
        alltrue = (finalstate == allinfected)
        if hyptrue and alltrue:
            hypall.append(st)
            hypallcnt += 1
        elif hyptrue and not alltrue:
            hypnotcnt += 1
        elif (not hyptrue) and alltrue:
            nohypall.append(st)
            nohypallcnt += 1

    print "States satisfying hypothesis that cause total infection:", hypallcnt
    print "States satisfying hypothesis that don't cause total infection:", hypnotcnt
    print "States not satisfying hypothesis that cause total infection:", nohypallcnt

    return (hypall, nohypall)

# Results of checkcombos(5):
#   States satisfying hypothesis that cause total infection: 90
#   States satisfying hypothesis that don't cause total infection: 30
#   States not satisfying hypothesis that cause total infection: 1525
# So the answer to question 1 is no.  Having at least one infected cell
# in every row and column is NOT a necessary condition to infect the entire grid.

# checkcombos(4) confirms that there are no states with four infected cells
# that lead to total infection.

# New hypothesis: Having a bounding box of the initial infected cells equal to
# the entire grid is a necessary but insufficient condition for all cells to
# become infected.  (Obviously insufficient because four infected cells in the
# corners of the grid can't work).
