# This code was in a 2012 version of factor.py that I found.

import itertools

def makerunlengthsequence(start, end, runlength, startHAS = True, printOut = False):
    HASlist = []
    NOTlist = []
    BuddhaNature = startHAS
    count = 0
    currunlen = runlength  # eventually allow runlength to be a generator
    for i in range (start, end+1):
        if BuddhaNature:
            HASlist.append(i)
            if printOut: print i
        else:
            NOTlist.append(i)
            if printOut: print '\t', i
        count += 1
        if count == currunlen:
            BuddhaNature = not BuddhaNature
            count = 0
            currunlen = runlength
    return HASlist, NOTlist

HAS22275 = [1,2,3,4,5,6,21,22,34,56,57,1353,1383]
HASNOT22275 = [10,11,12,13,15,42,58,63,222,383,461,1235,1323,1338,1373,1461,1464,2766]

def checkrunlengthsequence(HASlist, NOTlist, start, end, runlength, startHAS = True):
    BuddhaNature = startHAS
    count = 0
    currunlen = runlength  # eventually allow runlength to be a generator
    for i in range (start, end+1):
        if i in HASlist:
            if BuddhaNature:
                print i
            else:
                print '\t', i, "**"
        if i in NOTlist:
            if BuddhaNature:
                print i, "**"
            else:
                print '\t', i
        count += 1
        if count == currunlen:
            BuddhaNature = not BuddhaNature
            count = 0
            currunlen = runlength

def makerunlengthsequenceGEN(start, end, runlenGenerator, startHAS = True, printOut = False):
    HASlist = []
    NOTlist = []
    BuddhaNature = startHAS
    count = 0
    currunlen = runlenGenerator.next()
    for i in range (start, end+1):
        if BuddhaNature:
            HASlist.append(i)
            if printOut: print i
        else:
            NOTlist.append(i)
            if printOut: print '\t', i
        count += 1
        if count == currunlen:
            BuddhaNature = not BuddhaNature
            count = 0
            currunlen = runlenGenerator.next()
    return HASlist, NOTlist

# examples
# makerunlengthsequenceGEN(1, 45, (n for n in range(1,11)), True, True)
# makerunlengthsequenceGEN(1, 64, (10 - n for n in range(20)), True, True)
# makerunlengthsequenceGEN(1, 100, (n for n in range(10, 1, -1) + range(1, 11)), True, True)
# makerunlengthsequenceGEN(1, 100, (n for n in itertools.cycle(range(10, 1, -1) + range(1, 10))), True, True)

# Generator combinators from
# http://www.ibm.com/developerworks/linux/library/l-cpyiter/index.html
def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

def weave(*iterables):
    "Intersperse several iterables, until all are exhausted"
    iterables = map(iter, iterables)
    while iterables:
        for i, it in enumerate(iterables):
            try:
                yield it.next()
            except StopIteration:
                del iterables[i]

# examples
# [x for x in chain(range(1,10), range(10,0,-1))]
# [x for x in weave(range(10), range(10,0,-1))]
