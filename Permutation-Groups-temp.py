from sympy.combinatorics import Permutation
from sympy import init_printing
init_printing(perm_cyclic= True , pretty_print=False)
P = Permutation

def multbytransposes(p, sn):
    for i in range(sn-1):
        for j in range(i+1, sn):
            q = P(i,j, size=sn)
            print(q, p*q)

def conjbytransposes(p, sn):
    for i in range(sn-1):
        for j in range(i+1, sn):
            q = P(i,j, size=sn)
            print(q, q*p*q)
