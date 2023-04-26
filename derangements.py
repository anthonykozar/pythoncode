# From <https://rosettacode.org/wiki/Permutations/Derangements#Python>

from itertools import permutations
import math


def derangements(n):
    'All deranged permutations of the integers 0..n-1 inclusive'
    return [ perm for perm in permutations(range(n))
             if all(indx != p for indx, p in enumerate(perm)) ]
