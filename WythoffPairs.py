# Wythoff Pairs
# Dec. 5, 2019

import math

PHI = (1.0 + math.sqrt(5.0))/2.0

# Return the nth Wythoff Pair
def NthWythoffPair(n):
    return (int(n*PHI), int(n*PHI*PHI))

pairs = [NthWythoffPair(n) for n in range(1,51)]

def ratio(pair): return float(pair[1])/float(pair[0])

# for p in pairs:
#     print p, ratio(p)

# pairs.sort(key=ratio)
# for p in pairs:
#     print p, ratio(p)

# pairs.sort(key=(lambda x: x[0]))

# Return True if pair is a Wythoff Pair
def TestPair(pair):
    if pair == (0,0): return True
    a = min(pair)
    b = max(pair)
    # a/PHI is always irrational so ceil(a/PHI) = int(a/PHI)+1
    ceil = int(a/PHI)+1
    return (a,b) == NthWythoffPair(ceil)


# Test DiEvAl's guess: AK (x,y) HTBN iff 0 <= max(x,y)*phi - min(x,y)*phi^2 < 1
def TestGuess(pair):
    a = min(pair)
    b = max(pair)
    d = b*PHI - a*PHI*PHI
    print pair, d
    bn = TestPair(pair)
    guess = (d >= 0.0 and d < 1.0)
    if bn != guess:
        print "Guess is wrong!", pair, d, bn, guess
    return guess
