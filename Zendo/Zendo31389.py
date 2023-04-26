Zendo31389Has = [1, 3, 5, 7, 9, 20, 24, 26, 42, 135, 136, 137,
                 176, 233, 234, 592, 693, 811, 852, 4410, 4592, 12345, 13579,
                 54321, 56789, 44444410]

Zendo31389HasNot = [2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21,
                    25, 36, 41, 43, 52, 144, 147, 243, 404, 1000, 4411, 23456,
                    44210, 59049, 67890, 86420, 123450, 4444410,
                    16777216, 33554432, 1122334455, 1000000000000]

def digitparitysequence(num):
    digits = str(num)
    pseq = ""
    for dgt in digits:
        if int(dgt)%2 == 1:
            pseq += "1"
        else:
            pseq += "0"
    return pseq

has = set(map(digitparitysequence, Zendo31389Has))
hnot = set(map(digitparitysequence, Zendo31389HasNot))

print "Has: ", has
print "Not: ", hnot
print "Intersection: ", has.intersection(hnot)

def classifysequences(hasSet, notSet, maxlen = 5, colwidth=10):
    print '%-*s%-*s%-*s' % (colwidth, 'Has', colwidth, 'Unknown', colwidth, 'Has Not')
    for k in range(1, maxlen+1):
        for i in range(2**k):
            binstr = '%0*d' % (k, int(bin(i)[2:]))
            if binstr in hasSet:
                print binstr
            elif binstr in notSet:
                print '%s%s' % (' '*(colwidth*2), binstr)
            else:
                print '%s%s' % (' '*colwidth, binstr)

print
classifysequences(has, hnot)
