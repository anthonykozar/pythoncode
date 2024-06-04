# Checking & exploring some stuff from the video
# "6 Minutes of Fascinating Math"
# https://m.youtube.com/watch?v=XxrywM_NRJ0
# Oct. 31, 2023

n = 1
for i in xrange(1, 51):
    n2 = n+i+1
    s1 = sum(xrange(n,n2))
    s2 = sum(xrange(n2,n2+i))
    if s1 == s2:
        print "sum(%d,%d) = sum(%d,%d)" % (n, n2-1, n2, n2+i-1)
    else:
        print "FAILS: sum(%d,%d) != sum(%d,%d)" % (n, n2-1, n2, n2+i-1)
    n += 2*i + 1

def sumdigits(num):
    digits = str(num)
    sum = 0
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            sum += int(dgt)
    return sum

def digitalroot(num, sd = sumdigits):
    while num > 9:
        num = sd(num)
    return num

from collections import defaultdict

counts = defaultdict(int)
for e in xrange(2,21):
    print str(e) + ":",
    for n in xrange(1000):
        if sumdigits(n**e) == n:
            counts[n] += 1
            print n,
    print
print counts

counts = defaultdict(int)
for e in xrange(2,21):
    print str(e) + ":",
    for n in xrange(1000):
        if sumdigits(n**e) == n:
            sd = sumdigits(n)
            counts[sd] += 1
            print sd,
    print
print counts

def listdigitsumsofpowers(e, maxbase = 1000):
    counts = defaultdict(int)
    # print str(e) + ":",
    for n in xrange(maxbase):
        sd = sumdigits(n**e)
        counts[sd] += 1
    print counts
