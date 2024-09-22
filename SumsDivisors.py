# Sums of Divisors
#
# Perfect, deficient, abundant, pseudoperfect, weird, and practical numbers.
#
# Anthony Kozar
# circa Nov. 23, 2022
# Sept. 15 & 19-21, 2024

def divisors(num):
    return [1] + [n for n in xrange(2, num/2+1) if num % n == 0] + [num]

# Returns None if no sublist exists that sums to targetsum.
def findsublistwithsum(nums, targetsum):
    nums.sort()
    totalsum = sum(nums)
    if totalsum < targetsum:
        return None
    elif totalsum == targetsum:
        return nums
    else:
        sublist = []
        backupstates = []
        needed = targetsum
        idx = len(nums) - 1
        while needed > 0:
            while idx >= 0 and nums[idx] > needed: idx -= 1
            if idx >= 0:
                backupstates.append((idx-1, needed, list(sublist)))
                sublist.append(nums[idx])
                needed -= nums[idx]
                if needed == 0:
                    sublist.reverse()
                    return sublist
                idx -= 1
            elif len(backupstates) > 0:
                idx, needed, sublist = backupstates.pop()
            else:
                return None
    print "Warning: findsublistwithsum() reached the end."
    return None

# The following functions return True or False depending on if num is perfect, deficient, abundant, pseudoperfect, or weird, respectively.
# divs is an optional parameter to pass in the list of divisors of num.
def isperfect(num, divs = None, divisors = divisors):
    if divs == None:
        divs = divisors(num)
    return sum(divs) == 2*num

def isdeficient(num, divs = None, divisors = divisors):
    if divs == None:
        divs = divisors(num)
    return sum(divs) < 2*num

def isabundant(num, divs = None, divisors = divisors):
    if divs == None:
        divs = divisors(num)
    return sum(divs) > 2*num

# Pseudoperfect (or semiperfect) numbers are equal to the sum of a subset (possibily all) of their proper divisors.
def ispseudoperfect(num, divs = None, divisors = divisors, findsublistwithsum = findsublistwithsum):
    if divs == None:
        divs = divisors(num)
    dsum = sum(divs) - num
    if dsum == num: return True
    else: return dsum > num and findsublistwithsum(divs[0:-1], num) != None

# Weird numbers are abundant numbers that are not pseudoperfect (i.e. there does NOT exist a subset of their divisors
# that add up to themselves).
def isweird(num, divs = None, divisors = divisors, findsublistwithsum = findsublistwithsum):
    if divs == None:
        divs = divisors(num)
    dsum = sum(divs) - num
    return dsum > num and findsublistwithsum(divs[0:-1], num) == None


# "Practical numbers" are positive integers for which all smaller positive integers are equal to a sum of some of its proper divisors.
# https://en.m.wikipedia.org/wiki/Practical_number

# Verify that num satisfies the definition of a practical number.
def verifypracticalbydef(num, divisors = divisors, findsublistwithsum = findsublistwithsum):
    divs = divisors(num)
    for n in xrange(1, num):
        if findsublistwithsum(divs, n) == None:
            return False
    return True

# A complete sequence is a sequence of natural numbers such that every natural number can be represented as a sum of elements in the
# sequence using each value at most once.  (If there are duplicates in the sequence, each can be used once).
# An ordered sequence a[n] is complete if and only if a[0] = 1 and a[k] <= sum(a[0]...a[k-1]) + 1. I'm pretty sure that these
# conditions are enough to guarantee that a finite sequence can make any number up to the total sum of the sequence.
# seq should be sorted
def iscompleteseq(seq):
    if seq[0] != 1: return False
    psum = 1
    for ak in seq[1:]:
        if ak > psum + 1: return False
        psum += ak
    return True

# A more efficient way to determine if a number is practical.
# iscompleteseq() is probably sufficient but we can avoid calling divisors in simple cases.
def ispractical(num, divisors = divisors, iscompleteseq = iscompleteseq):
    if num == 1 or num == 2:
        return True
    elif num%4 == 0 or num%6 == 0:
        return iscompleteseq(divisors(num))
    else:
        return False

# Find a practical number that is a multiple of num
def findpracticalmultiple(num, ispractical = ispractical):
    foundpracnum = False
    m = 1
    while not foundpracnum:
        pnum = m*num
        if ispractical(pnum):
            foundpracnum = True
        else:
            m += 1
    return pnum

'''
# Find the smallest multiple of each number up to 1000 that is practical
for n in xrange(2,1001):
    pn = findpracticalmultiple(n)
    print n, pn/n, pn

# Practical multiples of prime numbers appear to be strictly non-decreasing!
from findprimes import findprimes4
primes = findprimes4(1000, False)
for n in primes:
    pn = findpracticalmultiple(n)
    print n, pn/n, pn
'''

'''
from collections import defaultdict
multipliermap = defaultdict(list)
for n in xrange(2,1001):
    pn = findpracticalmultiple(n)
    multipliermap[pn/n].append(n)
multipliers = multipliermap.keys()
multipliers.sort()
counts = [(m, len(multipliermap[m])) for m in multipliers]
pracmultipliers = filter(ispractical, multipliers)
notpracmultipliers = [m for m in multipliers if not ispractical(m)]
'''
