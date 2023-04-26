def fibseq(maxx):
    out=[1,1]
    i=0
    fibnext=2
    while fibnext<=maxx:
        out.append(fibnext)
        i+=1
        fibnext= out[i]+ out[i+1]
    return out

def fibrecurrence(a1, a2, terms = 20):
    out=[a1,a2]
    for i in xrange(2,terms):
        out.append(out[i-2]+ out[i-1])
    return out

# make a list of products of pairs of DIFFERENT elements of arr
def pairwiseproducts(arr):
    out=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            out.append(arr[i]*arr[j])
    return out

# make a list of sums of pairs of DIFFERENT elements of arr
def pairwisesums(arr):
    out=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            out.append(arr[i]+arr[j])
    return out

# maxx=3500
fp=pairwiseproducts(fibseq(1000))
fp=list(set(fp))
filter(lambda (x): x<=1000, fp)

# Print an addition table for pairs of elements in seq
def addtable(seq, colw = 4):
    # print row of indices
    print " "*colw*2 + "|",
    for i in range(len(seq)):
        print "%*d" % (colw, i),
    print

    # print row of seq values
    print " "*colw*2 + "|",
    for i in range(len(seq)):
        print "%*d" % (colw, seq[i]),
    print

    # print header separator
    print "-" * (colw+1) * (len(seq) + 2)

    # print a row for each value in seq
    for i in range(len(seq)):
        print "%*d%*d|" % (colw, i, colw, seq[i]),
        for j in range(len(seq)):
            print "%*d" % (colw, seq[i] + seq[j]),
        print
