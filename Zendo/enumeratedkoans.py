import math

def deriveseq(maxval, printvalues = False):
    YES = []
    NO = []
    putInYes = True
    count = 1
    n = k = 1
    while count <= maxval:
        if putInYes:
            YES.append(count)
            if printvalues: print count
        else:
            NO.append(count)
            if printvalues: print ' '*10, count

        count += 1
        k += 1
        if k > n:
            n += 1
            k = 1
            putInYes = not putInYes

    return YES, NO

def eqcheck(N):
    return math.ceil((-1 + math.sqrt(1+8*N)) / 2)
