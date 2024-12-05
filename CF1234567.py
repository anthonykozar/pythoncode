from fractions import Fraction

# Evaluate the convergents of
# 1 + 1/(2 + 1/(3 + 1/(4 + 1/(5 + ...))))
def cf(last, fr = Fraction):
    x = fr(last,1)
    for i in xrange(last-1,0,-1):
        x = fr(i,1) + fr(1,1)/x
    return x

def cffloat(last):
    x = float(last)
    for i in xrange(last-1,0,-1):
        x = i + 1.0/x
    return x

# converges to about 1.43312742672
# what is this number?
for n in xrange(31):
    print cffloat(n)
