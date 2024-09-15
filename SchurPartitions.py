# Schur Partitions
# June 9, 2024

# Tries to partition the integers 1 to N (or some other arbitrary set) into k parts such that
# none of the parts contains three integers x, y, z with x+y=z. (x and y can be the same).
import copy
import operator

# parameter op allows for generalizing the partitioning criteria to any arbitrary commutative binary operation
# i.e. if @ is an operation, then none of the parts can contain three integers x, y, z with x@y=z.
def SchurPartition(maxorset, numparts, op = operator.add, dcopy = copy.deepcopy):
    # add n to set p and add the sums of n with each element of p to s (including n itself)
    def addnum(n, p, s):
        p.add(n)
        for m in p:
            s.add(op(n, m))
    
    # recursive function that searches for a solution
    # returns the solution parts if all numbers have been added to parts, 
    # else it returns False if the current branch of the search failed
    def dosearch(nums, parts, sums):
        if len(nums) == 0:
            return parts
        n = nums[0]
        for i in xrange(len(parts)):
            if n not in sums[i]:
                ps = dcopy(parts)
                ss = dcopy(sums)
                addnum(n, ps[i], ss[i])
                res = dosearch(nums[1:], ps, ss)
                if res: return res
        return False
    
    # prepare list of nums and sets for the partition and their sums    
    if type(maxorset) == int:
        nums = list(xrange(1, maxorset+1))
    else:
        nums = list(maxorset)
    nums.sort()
    parts = [set() for i in xrange(numparts)]
    sums = [set() for i in xrange(numparts)]
    
    return dosearch(nums, parts, sums)
