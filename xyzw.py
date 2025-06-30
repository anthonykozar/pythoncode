# Find integer solutions to the equation
#   x^2 + y^2 + z^2 + w^2 = xyzw
#
# using techniques from the Numberphile video
# "A simple equation that behaves weirdly".
# https://m.youtube.com/watch?v=a7BVL1MOCl4

# Anthony Kozar
# June 20, 2025

import operator

MAXVAL = 10000000
MAXSOLUTIONS = 10000

def product(alist):
    return reduce(operator.mul, alist)

def rootjump(vals, i):
    v = list(vals)
    vi = v[i]
    v[i] = 1
    vi = product(v) - vi
    v[i] = vi
    return v

def verifysolution(vals):
    sumsqrs = sum(map(lambda x:x*x, vals))
    prod = product(vals)
    return sumsqrs == prod

sol0 = (0,0,0,0)
sol1 = (2,2,2,2)

solutions = set([sol0, sol1])
solqueue = [(sol1,-1)]

while len(solqueue) > 0:
    s, lasti = solqueue.pop(0)
    for i in [0,1,2,3]:
        if i == lasti: continue
        t = rootjump(s, i)
        if verifysolution(t):
            ts = tuple(sorted(t))
            if max(t) < MAXVAL and not ts in solutions:
                solutions.add(ts)
                solqueue.append((t,i))
    if len(solutions) > MAXSOLUTIONS:
        break

print len(solutions), "solutions found"
if len(solutions) < 500:
    for s in sorted(solutions):
        print s

valueset = reduce(lambda a,b: set(a).union(set(b)), solutions)
print sorted(valueset)

# Find integer solutions to the equation
#   x^2 + y^2 + z^2 = xyz
# A comment on the video mentions this
# similar equation with starting solution
# (3,3,3).
