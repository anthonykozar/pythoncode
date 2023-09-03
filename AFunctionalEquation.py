# A "Notorious Functional Equation"
# from Michael Penn's video
# https://m.youtube.com/watch?v=TdilUmlZX7I
#
# Let f: N -> N (excluding 0) such that
#   f(x^2 + y^2) = f(x)f(y) and
#   f(x^2) = (f(x))^2
#
# f(x) = 1 is one possible solution. 
# (f(x) = 0 would work too if allowed).
# Are there any other f that satisfy the
# equations?

# Define f(n)=f_n as a member of f, then
# add all additional f(x) that can be inferred
# by the functional equations (x <= MAXX).
def definefvalue(f, n, f_n, MAXX):
    f[n] = f_n
    queue = [n]
    def addfvalue(a, f_a):
        if f.has_key(a) and f[a] != f_a:
            print "addvalue(%d,%d) called but f[%d] already equal to %d" % (a, f_a, a, f[a])
            return
        if a <= MAXX and not f.has_key(a):
            f[a] = f_a
            queue.append(a)
            # print "f[%d] = %d" % (a, f_a)
    
    while len(queue) > 0:
        x = queue[0]
        queue.remove(x)
        x2 = x*x
        addfvalue(x2, f[x] * f[x])
        domain = f.keys()
        for y in domain:
            z = x2 + y*y
            addfvalue(z, f[x] * f[y])

f={}
# f(1) must be 1 => f(2^n) = 1 for all n
#   => f(5) = 1 => f(25) = 1
definefvalue(f, 1, 1, 1000)
# f(4) = 1 and f(25) = f(9+16) = 1 => f(3) = 1
definefvalue(f, 3, 1, 1000)
# f(3) = 1 => f(9) = 1 => f(10) = 1 
#   => f(100) = f(36+64) = 1 => f(6) = 1
definefvalue(f, 6, 1, 1000)
# f(25) = 1 => f(50) = 1 => f(7) = 1
definefvalue(f, 7, 1, 1000)
k = f.keys()
k.sort()
print k

# and so on for 11, 12, 14, 15, 19, and all n???
