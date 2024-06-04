# Langford Pairings
# See https://en.m.wikipedia.org/wiki/Langford_pairing
# and https://m.youtube.com/watch?v=Lju6aYms2EA

def countsolutions(n, printsolutions = True, trace = False):
    blank = '.'
    def printarr(arr):
        s = ''
        for e in arr:
            if type(e) == int and e >= 10:
                s += '(' + str(e) + ')'
            else: s += str(e)
        print s,
    
    def placenum(arr, k, n, printsols, trace):
        # try placing a pair of k's in each position of arr, calling placenum(k-1) when successful.
        numsols = 0
        pairoffset = k+1
        for i in xrange(2*n - pairoffset):
            if arr[i] == blank and arr[i+pairoffset] == blank:
                arr2 = arr[:]
                arr2[i] = k
                arr2[i+pairoffset] = k
                if k == 1:
                    numsols += 1
                    if printsols or trace:
                        printarr(arr2)
                        print
                else:
                    if trace:
                        printarr(arr2)
                    numsols += placenum(arr2, k-1, n, printsols, trace)
        if trace and numsols == 0:
            print ' X'
        elif trace:
            print
        return numsols
    
    emptyarr = [blank] * (2*n)
    return placenum(emptyarr, n, n, printsolutions, trace)

# Make an "infinite" Langford Pairing.
# Returns a pair of lists. The first is the beginning of the infinite pairing and
# the second contains the indices at which the first members of each pair k are placed.
def infinitepairing(length):
    i = k = 1
    a = {}
    b = []
    while i <= length:
         while a.has_key(i):
             i += 1
         a[i] = k
         a[i+k+1] = k
         b.append(i)
         k += 1
    return ([a[i] for i in range(1, length+1)], b)

""" Here is a surprising link to the eta sequence for the golden ratio!

a,b = infinitepairing(2000000)
bd = FirstDiffs(b)
e = eta_sequence(phi,len(bd)+2)
e[2:] == bd

Returns True
"""

if __name__ == '__main__':
    import sys
    
    for arg in sys.argv[1:]:
        n = int(arg)
        if n > 0:
            print "Searching for solutions for %d" % n
            c = countsolutions(n, True, True)
            print "%d solutions found" % c
            print
