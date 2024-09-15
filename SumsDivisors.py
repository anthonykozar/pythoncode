# Sums of Divisors
#
# Abundant, pseudoperfect, weird, and practical numbers.
#
# Anthony Kozar
# circa Nov. 23, 2022

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
