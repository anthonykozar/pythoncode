# Zendo game #38224
# AKHTBN iff its binary representation is a prefix of the binary complement of the infinite Fibonacci word, 101101011011010110101101101011... (See https://oeis.org/A044432 and https://oeis.org/A005614).

def makeFibWord(length):
    w = "10"
    lastw = "1"
    while len(w) < length:
        temp = w
        w += lastw
        # print w
        lastw = temp
    return w[:length]

# Substitute characters in s according
# to the transforms in tr.
def subst(s, tr):
    out=""
    for c in s:
        out+=tr[c]
    return out

# Morphism for the infinite Fibbonaci word
fb={'0':'01','1':'0'}

# Morphism for the binary complement of the
# infinite Fibonacci word, A005614. Start
# with 1, apply 0->1, 1->10, iterate, ...
fbcompl={'0':'1','1':'10'}
def makeFibWord2(length, sub = subst):
    w = "1"
    while len(w) < length:
        w = sub(w, {'0':'1','1':'10'})
        # print w
    return w[:length]

# make the a[] sequence according to 
# Draw5's first guess
def makeAseq(length):
    aseq = [1]
    idx = 0
    while len(aseq) < length:
        aseq += [2]*aseq[idx] + [1]
        idx += 1
    return aseq[:length]

# make the B sequence from an a sequence
# according to Draw5's guess
def makeBseq(aseq):
    bseq = []
    for i in aseq:
        bseq += [1]*i + [0]
    return bseq

a = makeAseq(100)
b = makeBseq(a)
fibword = map(int, makeFibWord(len(b)))
print "b == fibword is", b == fibword
