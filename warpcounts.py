
threads = 0
while (threads < 720):
    gold = threads % 23
    tie = threads % 30
    if (tie == 0):
        print "T"
    
    if (gold == 0):
        print "G   ",
        threads += 1
    else:
        goldleft = 23 - gold
        tieleft = 30 - tie
        if (goldleft < tieleft):
            white = goldleft
        else:
            white = tieleft
        print "%-4d" % white,
        threads += white

print
print threads
