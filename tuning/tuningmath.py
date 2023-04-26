# Musical tuning math

import math
import fractions
from fractions import Fraction

def ratio2cents(ratio):
    return 1200 * math.log(ratio,2)

def cents2ratio(cents):
    return 2**(cents / 1200.0)

# transpose cents to the range [0,1200] by adding or subtracting octaves (1200) 
def centsmod(cents):
	while cents < 0:
		cents = cents + 1200
	while cents > 1200:
		cents = cents - 1200
	return cents

# transpose ratios to the range [1/1,2/1] by by adding or subtracting octaves
def ratiomod(ratio):
	if ratio <= 0:
		print "Bad ratio in centsmod():", ratio
		return ratio
	while ratio < Fraction(1,1):
		ratio = ratio * 2
	while ratio > Fraction(2,1):
		ratio = ratio / 2
	return ratio

# calculate interval from ratio A to B
def interval(fromA,toB):
    return toB / fromA

# calculate beats per second between freq and (freq + cents)
def beatspersec(freq, cents):
    return freq * cents2ratio(cents) - freq

# calculate seconds per beat between freq and (freq + cents)
def secperbeat(freq, cents):
    return 1.0 / (freq * cents2ratio(cents) - freq)

# To find a rational approximation of x:
#   Fraction(x).limit_denominator(maxdenom)

# scale should be a list of ratios
def printscale(scale):
    for ratio in scale:
        print "%15s   %8.3f" % (ratio, ratio2cents(ratio))

# scale should be a list of ratios
def printintervals(scale):
    last = Fraction(1,1)
    for ratio in scale:
        intvl = interval(last,ratio)
        print "%15s  %15s   %8.3f" % (ratio, intvl, ratio2cents(intvl))
        last = ratio

# example definitions of scales
scalestep = Fraction('8/7')
scaledegs = [scalestep**i for i in range(-5,6)]
scale = map(ratiomod, scaledegs)
scale.sort()

justmajor = map(Fraction, [ '1/1', '9/8', '5/4', '4/3', '3/2', '5/3', '15/8', '2/1'])
