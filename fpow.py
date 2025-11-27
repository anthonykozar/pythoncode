# A couple of different methods for computing
# arbitrary real powers of a real number.
#
# Anthony Kozar
# Aug. 27-28, 2025

# Compute x^y by using a binary representation
# of y and repeated square roots of x to 
# approximate x^y = x^n * x^(b1/2) * x^(b2/4)
#  * x^(b3/8) * x^(b4/16) * ... where n is the
# integer part of y and b1, b2, ... are the
# bits of the fractional part.
def fpow(x,y, precision = 1.0e-17):
    from math import sqrt
    n = int(y)
    z = x**n
    ex = y - n
    xrt = sqrt(x)
    rt = 0.5
    while ex > precision:
        if ex > rt:
            z *= xrt
            ex -= rt
        xrt = sqrt(xrt)
        rt *= 0.5
    return z

# Compute x^y by multiplying the ln(x) by y.
def fpow2(x,y):
    from math import log, exp
    return exp(y*log(x))
