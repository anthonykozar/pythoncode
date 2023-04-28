# Digit patterns in arithmetical operations
# on certain numbers.

def printfn(s):
    print s

def openoutfile(filename, pathprefix = "/storage/emulated/0/"):
    pathname = pathprefix + filename
    f = open(pathname, 'w')
    if not f:
        print "Could not open file " + pathname
    return f

# repsquares() outputs the squares of the numbers formed by
# concatenating repfunc(k) copies of repstr
# with optional prefix & suffix strings where
# k ranges from 1 to maxreps. If repfunc is
# not provided, then k is used unchanged.
def repsquares(maxreps, repstr, prefix = '', suffix = '', repfunc = None, outfunc = printfn):
    if repfunc == None:
        repfunc = lambda x: x
    for k in xrange(1, maxreps+1):
        n = int(prefix + repstr*repfunc(k) + suffix)
        outfunc(n**2)


f = openoutfile("/Documents/python/repsquares.txt")
def fwrite(s, fout = f):
    fout.write(str(s)+'\n')

MAXREPS = 50
for i in range(1,10):
    fwrite("Squares of numbers with the form %d+\n" % i)
    repsquares(MAXREPS, str(i), outfunc=fwrite)
    fwrite("\n")

f.close()
