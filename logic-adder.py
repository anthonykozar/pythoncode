def addu(a, b):
    s = a^b
    c = a&b
    while c != 0:
        a=s
        b=2*c
        s = a^b
        c = a&b
    return s

def prbin(a,b):
    print bin(a), bin(b)
    print bin(a^b), bin(a&b)
    print bin(a+b)

cnt = 0
for a in xrange(1000):
    if a%100==0: print cnt
    for b in xrange(1000):
        if addu(a,b) != a+b:
            print a,b
        else: cnt+=1
print cnt
