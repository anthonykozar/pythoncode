# Some useful code for exploring the open cover of the rationals on (0,1)
# that is described in this video:
#
# Music and measure theory
# https://m.youtube.com/watch?v=cyW5z-M2yzw
#
# January 28, 2021

def enumerateRationals(maxdenom):
  Q =[]
  for d in range(2,maxdenom+1):
    for n in range(1,d):
      reduced = True
      for i in range(2,d):
        if n%i==0 and d%i==0:
          reduced = False
      if reduced:
        Q.append((n, d))
  return Q

def ratio2float(ratio):
  return (1.0*ratio[0])/ratio[1]

def makecover(values, startwidth=0.25, mult=0.5, printintervals = False):
  cover = []
  radius = 0.5*startwidth
  for v in values:
    interval = (v-radius,v+radius)
    cover.append(interval)
    if printintervals:
      print "(%.12f,%.12f)" % interval
    radius *= mult
  return cover

def isbetween(val, interval):
  return val > interval[0] and val < interval[1]

def overlaps(interval1, interval2):
 return isbetween (interval1[0], interval2) or isbetween (interval1[1], interval2) or isbetween (interval2[0], interval1) or isbetween (interval2[1], interval1)

cov = makecover(map(ratio2float, enumerateRationals(20)))

def findOverlaps(intervals):
  for i in range(1, len(intervals)):
    for j in range(i):
      if overlaps(intervals[i], intervals[j]):
        print "(%.12f,%.12f) overlaps" % intervals[i],
        print "(%.12f,%.12f)" % intervals[j]

def sumIntervals(intervals):
  sum = 0
  for iv in intervals:
    sum += iv[1] - iv[0]
  return sum

