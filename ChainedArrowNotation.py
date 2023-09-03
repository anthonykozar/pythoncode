import sys
from copy import deepcopy

DEBUG = True

# a -> b -> ... -> c is represented as the list [a, b, ..., c].
# Parenthesized subchains like a -> ... -> (b -> ... -> c) -> ... -> d are represented as sublists: [a, ..., [b, ..., c], ..., d].
# E.g.
a = [5,[4,3,[2,1]],3,2,[5,8]]

def printelem(e):
    if type(e) == list:
        sys.stdout.write("(")
        printchain(e, False)
        sys.stdout.write(")")
    else:
        sys.stdout.write(str(e))

def printchain(ch, newline = False):
    for e in ch[:-1]:
        printelem(e)
        sys.stdout.write(" -> ")
    printelem(ch[-1])
    if newline: print

def hasnestedchain(ch):
    for e in ch:
        if type(e) == list:
            return True
    return False

# Expands a chain of length 4 or more by
# applying the recursive rule
# a ... x -> y -> z+1 becomes
#   a ... x  when y = 1, else
#   f^(y-1)(a ... x) where
#   f(chain) = chain -> (chain) -> z
def expandchain(ch, lenlimit = 1000):
    if DEBUG:
        print "expandchain: ",
        printchain(ch, True)
    if len(ch) < 4:
        return ch
    head = ch[:-2]
    y = ch[-2]
    z = ch[-1] - 1
    expch = deepcopy(head)
    while y > 1:
        expch = deepcopy(head) + [expch, z]
        y -= 1
    return expch

# Simplifies a chain by removing trailing 
# 1's, evaluating nested chains with lengths
# up to maxevallen, and optionally expanding
# chains with lengths of 4 or more.
def simplifychain(ch, maxevallen = 2, expand = True, lenlimit = 1000, showsteps = True):
    if DEBUG:
        print "simplifychain: ",
        printchain(ch, True)
    newch = deepcopy(ch)
    reevaluate = True
    while reevaluate:
        reevaluate = False
        if hasnestedchain(newch):
            # simplify nested chains in reverse order
            for i in xrange(len(newch)):
                if type(newch[i]) == list:
                    newch[i] = simplifynestedchain(newch[i], maxevallen, expand, lenlimit)
                    if showsteps: printchain(newch, True)
            reevaluate = True
        # remove trailing 1's
        while newch[-1] == 1:
            newch = newch[:-1]
            reevaluate = True
            if showsteps: printchain(newch, True)
        if expand and len(newch) > 3:
            newch = expandchain(newch)
            reevaluate = True
            if showsteps: printchain(newch, True)
    return newch

def simplifynestedchain(ch, maxevallen, expand, lenlimit):
    if DEBUG:
        print "simplifynestedchain: ",
        printchain(ch, True)
    while True:
        if not hasnestedchain(ch) and len(ch) <= maxevallen:
            return evalchain(ch)
        else:
            res = simplifychain(ch, maxevallen, expand, lenlimit, False)
            if res == ch:
                return ch
            ch = res

def evalchain(ch, exponlimit = 40):
    if DEBUG:
        print "evalchain: ",
        printchain(ch, True)
    if not hasnestedchain(ch):
        chlen = len(ch)
        if chlen == 1:
            return ch[0]
        elif chlen == 2:
            if ch[1] < exponlimit:
                return ch[0]**ch[1]
            else:
                print "exponent limit exceeded: %d^%d" % (ch[0], ch[1])
                return None
        elif chlen == 3:
            pass
    
    return None

simplifychain([3,3,1,3,2])
