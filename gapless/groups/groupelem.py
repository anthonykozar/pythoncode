# module gapless.groups.groupelem

# Part of the Gapless project.
#
# (c) 2025 Anthony M. Kozar Jr.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import operator

class GroupElement(object):
    # 'name' must be a unique string for each
    # element in the same group.
    def __init__(self, name, group = None):
        self.name = name
        self.group = group
    
    def __str__(self):
        return self.name

    def __mul__(self, other):
        return self.group.doOperation(self, other)
    
    def setGroup(self, group):
        self.group = group

class CyclicGroupElement(GroupElement):
    def __init__(self, numericval, group = None):
        self.val = numericval
        self.name = str(numericval)
        self.group = group

AUTO_PERM_LEN = -1

# To create a permutation on N elements that maps 1 -> a, 2 -> b, ..., N -> z, 'perm' 
# should be either a list [a,b,...,z] or a list of cycles such as [[1,2,4],[3,7]].
# In the first case, each value from 1 to N must occur in the list exactly once. In
# the second case, cycles of length one may be omitted.
class Permutation(GroupElement):
    def __init__(self, perm, permlen = AUTO_PERM_LEN, group = None):

def PermutationToCycleNotation(permstr, firstpos = 1, incl1cycles = False):
    permlist = map(int, list(permstr))
    permlen = len(permlist)
    output = ""
    # create an array with permlen elements initialized to False
    checkedvalues = [False] * permlen

    for i in range(firstpos, permlen+firstpos):
        idx = i - firstpos
        if not checkedvalues[idx]:
            # start a new cycle
            value = i
            cyclestr = ''
            looping = False
            while not looping:
                if checkedvalues[idx]:
                    # this value has already occurred in some cycle
                    # so we should be at the end of the cycle
                    if incl1cycles or len(cyclestr) > 1:
                        output += '(' + cyclestr + ')'
                    looping = True
                else:
                    # add and mark this value as checked
                    cyclestr += str(value)
                    checkedvalues[idx] = True
                    # get the image of value 
                    nextvalue = permlist[idx]
                    # prepare to check next value
                    value = nextvalue
                    idx = nextvalue - firstpos

    if output == '': output = '(1)'
    if printcycles: print output,
    return output

# Find the composition of two permutations
def ComposePerms(permstr1, permstr2, firstpos = 1):
    plist1 = map(int, list(permstr1))
    plist2 = map(int, list(permstr2))
    permlen = len(plist1)
    if permlen != len(plist2):
        print "ComposePerms(): permutation lengths do not match!"
        return

    # compute an array that is the composition of plist1 * plist2
    plist3 = [plist2[ plist1[i] - firstpos ] for i in range(permlen)]
    # convert the result to a string
    return reduce(operator.add, map(str, list(plist3)))
