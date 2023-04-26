size = 5
seen = [0]*(size+1)
queue = range(1, size+1)

def flashcard(q,s,rpt=10):
    print q
    for i in xrange(rpt):
        n = q[0]
        q = q[1:]
        s[n] += 1
        q.insert(s[n],n)
        print q
    print 'Counts:', s
