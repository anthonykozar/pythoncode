print "+/3",
for i in range(11):
    print "%2d" % i,
print
for i in range(11):
    print "%2d " % i,
    for j in range(11):
        if (i+j)%3 == 0:
            print "%2d" % (((i+j)/3)%7),
        else:
            print " .",
    print

def magicsqr(s):
    def prsum(a, b, c):
        print "%d+%d+%d=%d" % (a, b, c, a+b+c)
    prsum(s[0], s[1], s[2])
    prsum(s[3], s[4], s[5])
    prsum(s[6], s[7], s[8])
    prsum(s[0], s[3], s[6])
    prsum(s[1], s[4], s[7])
    prsum(s[2], s[5], s[8])
    prsum(s[0], s[4], s[8])
    prsum(s[2], s[4], s[6])
