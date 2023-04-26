# CantorSet.py
#
# Calculate the numerators of some of the (end-)points within the Cantor set
#
# See http://oeis.org/A306556
#
# Anthony Kozar
# June 20, 2020

# Input: a list of pairs [(a,b), ...]
# Output: a list of pairs [(3a,3a+b-a), (3a+2b-2a,3b), ...]
def CantorCut(pairs):
    output = []
    for p in pairs:
        a = p[0]
        b = p[1]
        output.append((3*a,2*a+b))
        output.append((a+2*b,3*b))
    return output

# Return the numerators of the interval endpoints of the nth iteration of the
# process for constructing the Cantor Set.  (The denominator is 3**n).
# Note: CantorNumerators(n) is always the first half of CantorNumerators(n+1).
def CantorNumerators(n):
    intervals = [(0,1)]
    for i in xrange(n):
        intervals = CantorCut(intervals)
    return intervals

# Return a list of all non-list/tuple elements within a hierarchy of
# nested lists/tuples.  Eg. values([0,[1,2],[3,[4,5]]]) -> [0,1,2,3,4,5]
def values(iterable):
    output = []
    for elem in iterable:
        if type(elem) == list or type(elem) == tuple:
            output.extend(values(elem))
        else:
            output.append(elem)
    return output

# Return the complement of a list of integers between [0,maxint]
def complement(ints, maxint):
    comp = []
    for n in xrange(maxint):
        if not n in ints:
            comp.append(n)
    return comp


# Make a list of all "Cantor integers" up to 1,000,000.
# This list has 8192 elements.  There are no Cantor integers
# between 3**12 = 531,441 and 1,000,000.
cints = values(CantorNumerators(12))

# Test:  N in cints

def baseconvert(val,base):
    if base > 26:
        return "Error: base > 26"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basestr = ""
    while val > 0:
        rmndr = val % base
        val = val // base
        basestr = digits[rmndr] + basestr
    if basestr == "":
        basestr = "0"
    return basestr

def base3(n):
    return baseconvert(n, 3)

cintsb3 = map(base3, values(CantorNumerators(5)))
