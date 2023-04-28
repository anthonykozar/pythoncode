def catcongruence(p, q):
    q2 = q*q
    ppow = 1
    for i in xrange(q-1):
        ppow *= p
        if ppow >= q2:
            ppow %= q2
    return ppow

# This hung the Android interpreter
for n in xrange(1,2002,4):
    if catcongruence(2,n) == 1:
        print n

catcongruence(2,1093)
