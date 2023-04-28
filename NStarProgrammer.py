# Three Star Programmer and related interpreters

# interpreter by user Quintopia
# see https://esolangs.org/wiki/Three_Star_Programmer
# import sys,collections
# n=list(map(int,sys.stdin.read().split()))
# d=collections.defaultdict(int)
# i=0
# while 1:d[d[d[n[i]]]]+=1;sys.stdout.write(chr(d[3]%256)if d[1]%2else"");i=(i+1)%len(n);#print[d[k]for k in sorted(d.keys())]

import sys,collections

def run3star(program, maxloops = 5):
    d=collections.defaultdict(int)
    i=0
    loopcount = 0
    while loopcount < maxloops:
        d[d[d[program[i]]]]+=1
        # sys.stdout.write(chr(d[3]%256)if d[1]%2else"")
        i+=1
        if i >= len(program):
            i = i %len(program)
            loopcount += 1
        print[d[k]for k in sorted(d.keys())]

# version for defective Android Python
def run3star(prog, mem, maxloops = 5):
    i=0
    loopcount = 0
    while loopcount < maxloops:
        print prog[i],
        mem[mem[mem[prog[i]]]]+=1
        # sys.stdout.write(chr(d[3]%256)if d[1]%2else"")
        i+=1
        if i >= len(prog):
            i = i %len(prog)
            loopcount += 1
        print "[",
        j=0
        for k in sorted(mem.keys()):
            while j < k:
                print 0,
                j+=1
            print mem[k],
            j+=1
        print "]"

# run3star([0,1,2,3], collections.defaultdict(int), 10)
