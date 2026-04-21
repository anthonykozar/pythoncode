
# A triangular deck with "2 axes"
# (same as a double-N domino set)
for i in xrange(1,11):
    for j in xrange(1,i+1):
        print (j,i),
    print

# James Ernest's "pyramid deck" with 3 axes?
for i in xrange(1,11):
    for j in xrange(1,i+1):
        print (j,i,10-i+j),
    print
