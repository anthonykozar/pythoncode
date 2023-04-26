# THROWBACK procedure from
# "Coding Fun: Rearranging All The Numbers" in
# Popular Computing #55, Oct. 1977, Vol. 5, No. 10
# See <https://oeis.org/A155167/a155167.pdf> for a copy.

import math

# Display the array at each step and stop when the "leader" (the initial
# value in the array) is stopAtFirst or when maxsteps is reached.
def showprocess(stopAtFirst, maxsteps = 1000):
    steps = 0
    a = range(3,4+stopAtFirst)
    while a[0] != stopAtFirst and steps < maxsteps:
        first = a.pop(0)
        a.insert(first, first)
        steps += 1
        print steps, a
    return a

# Find the sequence where the (N-3)th value is the number of steps
# until N first appears as the leader. (A155167 in OEIS)
# The "first indices sequence"
def makefirstidxsequence(maxN):
    steps = 0
    a = range(3,4+maxN)
    leader = 4
    firstidxseq = []
    while a[0] != maxN:
        first = a.pop(0)
        a.insert(first, first)
        steps += 1
        if a[0] == leader:
            firstidxseq.append(steps)
            leader += 1
    return firstidxseq

# Find the sequence of leaders at each step (including the "zeroeth step").
def makeleadersequence(maxsteps, maxN = 40):
    steps = 0
    a = range(3,4+maxN)
    leaderseq = a[0:1]
    while steps < maxsteps:
        first = a.pop(0)
        if first > maxN:
            print "Aborted: maxN needs to be increased!"
            return leaderseq
        a.insert(first, first)
        steps += 1
        leaderseq.append(a[0])
    return leaderseq

# Find the sequence of step numbers where N is the leader.
def makeNsequence(N, maxN, maxsteps = 1000):
    steps = 0
    a = range(3,4+maxN)
    leader = N
    Nseq = []
    while a[0] != maxN and steps <= maxsteps:
        if a[0] == N:
            Nseq.append(steps)
        first = a.pop(0)
        a.insert(first, first)
        steps += 1
    return Nseq

# Find all indices where 'value' occurs.
# Given the leader sequence as input, this produces the "N-indices sequence".
def FindAllIndices(value, array):
    indices = []
    for i in xrange(len(array)):
        if array[i] == value:
            indices.append(i)
    return indices

# One way to obtain the "first indices", leader, and "N-indices" sequences
# while only running the procedure once:
#   leaders = makeleadersequence(1000000, 48)
#   Nindices = [FindAllIndices(i, leaders) for i in xrange(49)]
#   firstindices = map(lambda x: x[0], Nindices[4:])
### map(len, Nindices)

# First differences transform
def FirstDiffs(seq, includeFirstTerm = False):
    diffs = [seq[i] - seq[i-1] for i in range(1,len(seq))]
    if includeFirstTerm:
        diffs = seq[0:1] + diffs
    return diffs

def PrintInColumns(seq, columns = 9, colwidth = 2):
    count = 0
    for a in seq:
        print "%-*d" % (colwidth, a),
        count += 1
        if count == columns:
            print
            count = 0
    print "\n"

# Check that seq is cyclic with period length 'pdlen'.
def CheckPeriod(seq, pdlen):
    if len(seq) < 2*pdlen:
        print "Warning: sequence is shorter than 2 periods."
    period = seq[:pdlen]
    for i in xrange(pdlen, len(seq)):
        if seq[i] != period[i % pdlen]:
            return False
    return True

# The N-indices sequences have interesting patterns.  The
# differences of the indices for each N appear to repeat periodically.
# The period lengths for these sequences appear to be 1, 3, 9, 27, ...
# for N = 3, 4, 5, 6, ...
#   Nidxdiffs = map(FirstDiffs, Nindices)
#   PrintInColumns(Nidxdiffs[4][:27], 3)
#   PrintInColumns(Nidxdiffs[5][:81], 9)
#   PrintInColumns(Nidxdiffs[6][:243], 27)
#
#   for N in range(3,12):
#       periodlen = 3**(N-3)
#       result = CheckPeriod(Nidxdiffs[N], periodlen)
#       print N, periodlen, result

# Check that seq is a palindrome
def IsPalindrome(seq):
    lastidx = len(seq) - 1
    halflen = len(seq) // 2
    for i in xrange(halflen):
        if seq[i] != seq[lastidx - i]:
            return False
    return True

# One cycle of the differences of each N-indices sequence forms a
# palindrome if the last value is omitted.  Confirmed up to N = 13.
#   for i in range(4, 14):
#	print i, 3**(i-3) - 1, IsPalindrome(Nidxdiffs[i][:3**(i-3) - 1])

############

# What if 1 & 2 are included at the beginning of the process?
def showprocess2(stopAtFirst, maxsteps = 1000):
    steps = 0
    a = range(1,4+stopAtFirst)
    while a[0] != stopAtFirst and steps < maxsteps:
        first = a.pop(0)
        a.insert(first, first)
        steps += 1
        print steps, a
    return a

# Find the first indices sequence for the starting sequence of
# start, start+1, start+2, ...
def makefirstidxsequence2(maxN, start = 1):
    steps = 0
    a = range(start, start+maxN+1)
    leader = start+1
    firstidxseq = []
    while a[0] != maxN:
        first = a.pop(0)
        a.insert(first, first)
        steps += 1
        if a[0] == leader:
            firstidxseq.append(steps)
            leader += 1
    return firstidxseq

# Find the sequence of leaders at each step (including the "zeroeth step")
# for the starting sequence of start, start+1, start+2, ...
def makeleadersequence2(maxsteps, start = 1, maxN = 40):
    steps = 0
    a = range(start, start+maxN+1)
    leaderseq = a[0:1]
    while steps < maxsteps:
        first = a.pop(0)
        if first > maxN:
            print "Aborted: maxN needs to be increased!"
            return leaderseq
        a.insert(first, first)
        steps += 1
        leaderseq.append(a[0])
    return leaderseq

# For THROWBACK starting with 2:
#   leaders = makeleadersequence2(1000000, 2)
#   Nindices = [FindAllIndices(i, leaders) for i in xrange(35)]
#   firstindices = map(lambda x: x[0], Nindices[3:])
#   Nidxdiffs = map(FirstDiffs, Nindices)
#
#   for N in range(2, 13):
#       periodlen = 2**(N-2)
#       result = CheckPeriod(Nidxdiffs[N], periodlen)
#       print N, periodlen, result
#
#   for i in range(3, 14):
#       print i, 2**(i-2) - 1, IsPalindrome(Nidxdiffs[i][:2**(i-2) - 1])


# For THROWBACK starting with N:
N = 3
leaders = makeleadersequence2(1000000, N, N*20)
Nindices = [FindAllIndices(i, leaders) for i in xrange(max(leaders)+1)]
firstindices = map(lambda x: x[0], Nindices[N+1:])
Nidxdiffs = map(FirstDiffs, Nindices)

for i in range(N, 13):
    periodlen = N**(i-N)
    result = CheckPeriod(Nidxdiffs[i], periodlen)
    print i, periodlen, result

for i in range(N+1, 14):
    print i, N**(i-N) - 1, IsPalindrome(Nidxdiffs[i][:N**(i-N) - 1])

############

# What if we start with an arbitrary sequence?
def showprocess3(seq, stopAtFirst, maxsteps = 100):
    steps = 0
    a = seq[:]  # make a copy of seq
    seqlen = len(a)
    while a[0] != stopAtFirst and steps < maxsteps:
        first = a.pop(0)
        if first >= seqlen:
            print "Exiting early..."
            return leaderseq
        a.insert(first, first)
        steps += 1
        print steps, a
    return a

# Find the sequence of leaders at each step (including the "zeroeth step")
# for an arbitrary starting sequence.  The computation ends early if the
# leader would be "thrown" back past the end of the array.
def makeleadersequence3(seq, maxsteps):
    steps = 0
    a = seq[:]  # make a copy of seq
    seqlen = len(a)
    leaderseq = a[0:1]
    while steps < maxsteps:
        first = a.pop(0)
        if first >= seqlen:
            print "Exiting early..."
            return leaderseq
        a.insert(first, first)
        steps += 1
        leaderseq.append(a[0])
    return leaderseq

############

# A087165 appears to be related to the leader sequence
def makeA087165(length = 100):
    a = []
    for n in xrange(1, length+1):
        if n%4 == 1:
            val = 1
        else:
            val = a[n - int(math.ceil(n/4.0)) - 1] + 1
            # print (n, n - int(math.ceil(n/4.0)), a[n - int(math.ceil(n/4.0)) - 1]),
        a.append(val)
        # print val
    return a

# make the leader sequence with a recurrence similar to A087165?
def makeleaderbyrecurrence(length = 100):
    a = []
    for n in xrange(0, length):
        if n%4 == 0:
            val = 3
        else:
            val = a[n - int(math.ceil(n/4.0))] + 1
            # print (n, n - int(math.ceil(n/4.0)), a[n - int(math.ceil(n/4.0)) - 1]),
        a.append(val)
        # print val
    return a

def makeA155167recurrence(length = 50):
    a = [1]
    for n in xrange(1, length):
        a.append((4*a[n-1] + 3) // 3)
    return a
