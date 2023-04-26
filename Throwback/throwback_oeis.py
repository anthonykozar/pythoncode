# Michael S. Branicky, Sep 11 2022

from collections import deque
from itertools import count, islice
def tgen(): yield from count(3) # generator of sequence to throwback
def agen(): # generator of terms
    g = tgen()
    a = deque([next(g)])
    while True:
        leader = a.popleft()
        yield leader
        while leader > len(a): a.append(next(g))
        a.insert(leader, leader)

print(list(islice(agen(), 100)))

def makeleadersequence(maxsteps, maxN = 40):
    steps = 0
    a = list(range(3,4+maxN))
    leaderseq = a[0:1]
    while steps < maxsteps:
        first = a.pop(0)
        if first > maxN:
            print("Aborted: maxN needs to be increased!")
            return leaderseq
        a.insert(first, first)
        steps += 1
        leaderseq.append(a[0])
    return leaderseq
