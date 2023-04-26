from math import *

def eta_sequence(x, length=40, start=0, returnMultiples=False):
    last = int(start*x)
    if (returnMultiples):  seq = [last]
    else:  seq = []
    for n in range(start+1, length+start+1):
        cur = int(n * x)
        if (returnMultiples):  seq.append(cur)
        else:  seq.append(cur - last)
        last = cur
    return seq

auto = -1

# chunksize 0 or None will print the sequence without spaces
def printseq(seq, chunksize=auto):
    first = seq[0]
    last = seq[0]
    for i in range(len(seq)):
        if chunksize == -1: #auto:
            if seq[i] == first and last != first:
                sys.stdout.write(' ')
            last = seq[i]
        sys.stdout.write(str(seq[i]))
        if chunksize > 0 and (i+1)%chunksize == 0:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

def chunks(seq):
    chunks = []
    chunk = ""
    first = seq[0]
    last = seq[0]
    for i in range(len(seq)):
        if seq[i] == first and last != first:
            chunks.append(chunk)
            chunk = ""
        chunk += str(seq[i])
        last = seq[i]
    return chunks

def chunklengths(seq):
    return map(len, chunks(seq))

def runlengths(seq, val):
    count = 0
    runs = []
    for e in seq:
        if e == val:
            count += 1
        else:
            runs.append(count)
            count = 0
    return runs

# interesting examples

phi = (1.0 + sqrt(5.0))/2.0
sqrt2 = sqrt(2.0)
log3_2 = log(3.0)/log(2.0)
log5_4 = log(5.0)/log(4.0)

"""
An example you can copy and paste:

s2 = eta_sequence(sqrt2,500)
printseq(s2)
c2 = chunklengths(s2)
r2 = runlengths(c2,2)
printseq(r2)
r2 == s2[0:len(r2)]
"""
