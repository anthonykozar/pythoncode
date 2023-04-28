from ModMath import *

# show how the final digits of 2**10**n
# "converge" to the 10-adic constant
# ...893380022607743740081787109376.
prec = 30
mp = 10**prec
b = 2
for i in xrange(31):
    b = modpow(b, 10, mp)
    print("%2d  %*d" % (i, prec, b))
print("\n")

# b**10**n appears to converge to the same 
# number for any integer b ending in 2, 
# 4, 6, or 8!?!
# If b ends in 5, the limit is
# ...106619977392256259918212890625.
# And any integer ending in 1, 3, 7, or 9 
# eventually leads to ...000000000000001 !!

# Calculate the limit of b**exp**n.
# MAKE SURE IT CONVERGES FIRST OR THIS
# FUNCTION WILL NEVER END!
def make10adicconstant(b, precision, exp = 10, modpow = modpow):
    last = None
    precmod = 10**precision
    while b != last:
        last = b
        b = modpow(last, exp, precmod)
    return b

b2 = make10adicconstant(2, prec)
b3 = make10adicconstant(3, prec)
b5 = make10adicconstant(5, prec)
print("b2 = lim(2**10**n) = ...%d" % b2)
print("b3 = lim(3**10**n) = ...000%d" % b3)
print("b5 = lim(5**10**n) = ...%d" % b5)
print("b2+b5 = %d" % modadd(b2, b5, mp))
print("b2*b5 = %d" % modmult(b2, b5, mp))
b2e5 = make10adicconstant(2, prec, 5)
print("b2e5 = lim(2**5**n) = ...%d" % b2e5)
print("b2e5*b5 = %d" % modmult(b2e5, b5, mp))
print("-b2 = b5-1 = ...%d" % modneg(b2, mp))
print("-b2 * b5 = %d" % modmult(modneg(b2, mp), b5, mp))
print("b5*(b5-1) = %d" % modmult(b5, b5-1, mp))
print("-b2e5 = ...%d" % modneg(b2e5, mp))
print("-b2e5 * b5 = %d" % modmult(modneg(b2e5, mp), b5, mp))
