for n in xrange(0,41,2):
    p2 = 2**n
    num = (p2-1)**(n+1) + (p2+1)**(n+1)
    den = p2*2
    if num%den == 0:
        res = num/den
    else:
        res = float(num)/float(den)
    print "(%d/2)^%d + (%d/2)^%d =" % (p2-1, n+1, p2+1, n+1), res

for n in xrange(100,501,2):
    p2 = 2**n
    num = (p2-1)**(n+1) + (p2+1)**(n+1)
    den = p2*2
    if num%den != 0:
        print "(%d/2)^%d + (%d/2)^%d is not an integer" % (p2-1, n+1, p2+1, n+1)
