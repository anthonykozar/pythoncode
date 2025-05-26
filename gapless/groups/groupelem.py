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
        # save a permutation list as primary representation of the permutation 
        if type(perm) != list or len(perm) < 1:
            raise ValueError("First parameter to Permutation() must be a non-empty list.")
        if type(perm[0]) == list:
            # expecting perm to be a list of cycles
            self.permlist = self.cyclesToPermList(perm, permlen)
            self.size = len(self.permlist)
        elif type(perm[0]) == int:
            self.size = self.validatePermList(perm, permlen)
            self.permlist = list(perm)
        else:
            raise TypeError("First parameter to Permutation() must be a list of ints or a list of lists.")

        # also save a list of cycles and cycle notation string with sorted elements
        self.cycles = self.permListToCycles(self.permlist)
        self.cyclestr = self.cyclesToString(self.cycles, self.size)

        GroupElement.__init__(self, self.cyclestr, group)
   
    # checks that perm is a list of integers from 1 to permlen and returns permutation size
    def validatePermList(self, perm, permlen):
        if permlen == AUTO_PERM_LEN:
            permlen = len(perm)
        elif permlen != len(perm):
            raise ValueError("Length of permutation list does not equal 'permlen' parameter")

        # check for correct values
        for i in range(1, permlen+1):
            if not i in perm:
                raise ValueError("Permutation list does not contain the value %d" % i)
        return permlen
    
    # checks that cycles contains positive elements and that permlen matches;
    # returns the permutation size
    def validateCycles(self, cycles, permlen):
        minelem = min(map(min, cycles))
        if minelem < 1:
            raise ValueError("Cycles contain a non-positive element")
        maxelem = max(map(max, cycles))
        if permlen == AUTO_PERM_LEN:
            permlen = maxelem
        if permlen < maxelem:
            raise ValueError("'permlen' parameter is smaller than the maximum element in cycles")
        return permlen

    # converts a list of cycles to a permutation list
    def cyclesToPermList(self, cycles, permlen = AUTO_PERM_LEN):
        permlen = self.validateCycles(cycles, permlen)
        permlist = [0]*permlen

        def setimage(a,b):
            # map a -> b in permlist
            if permlist[a-1] == 0:
                permlist[a-1] = b
            else:
                raise ValueError("Duplicate element in cycles")

        for cycle in cycles:
            preimg = cycle[0]
            idx = 1
            cyclen = len(cycle)
            while idx < cyclen:
                img = cycle[idx]
                setimage(preimg, img)
                preimg = img
                idx += 1
            setimage(preimg, cycle[0])

        # any remaining zeros in permlist are single cycles, 
        # so map them to themselves
        for i in range(permlen):
            if permlist[i] == 0:
                setimage(i+1, i+1)
        return permlist

    # converts a permutation list to a list of cycles
    def permListToCycles(self, permlist, incl1cycles = False):
        permlen = len(permlist)
        cycles = []
        checkedvalues = set()
        for i in range(1, permlen+1):
            idx = i - 1
            if not idx in checkedvalues:
                # start a new cycle
                value = i
                curcycle = []
                looping = False
                while not looping:
                    if idx in checkedvalues:
                        # this value has already occurred in some cycle
                        # so we should be at the end of the cycle
                        if incl1cycles or len(curcycle) > 1:
                            cycles.append(curcycle)
                        looping = True
                    else:
                        # add and mark this value as checked
                        curcycle.append(value)
                        checkedvalues.add(idx)
                        # get the image of value
                        nextvalue = permlist[idx]
                        # prepare to check next value
                        value = nextvalue
                        idx = nextvalue - 1
        if cycles == []:
            # use [[n]] as the identity element for n elements
            cycles = [[permlen]]
        
        return cycles
    
    # Converts a list of cycles to a str ("cycle notation"). Does not sort
    # the cycles into ascending order, so if a "canonical" represention is
    # needed use the output of permListToCycles(). When useCommas == False,
    # spaces are inserted automatically between elements if the size of the
    # permuation is > 9, but this can be forced for smaller permutations by
    # setting useSpaces = True.
    def cyclesToString(self, cycles, permlen = AUTO_PERM_LEN, incl1cycles = False, useSpaces = False, useCommas = False):
        permlen = self.validateCycles(cycles, permlen)

        # determine the element separator
        if useCommas and useSpaces:
            sep = ', '
        elif useCommas and not useSpaces:
            sep = ','
        elif not useCommas and (useSpaces or permlen > 9):
            sep = ' '
        else:
            sep = ''

        # convert explicit cycles to a string
        cyclenotation = ''
        for cyc in cycles:
            cyclenotation += '(' + sep.join(map(str, cyc)) + ')'

        # add implicit single cycles if requested
        if incl1cycles:
            cycelems = set(reduce(operator.add, cycles))
            allelems = set(xrange(1, permlen+1))
            missingelems = list(allelems - cycelems)
            missingelems.sort()
            for e in missingelems:
                cyclenotation += '(' + str(e) + ')'
        
        return cyclenotation
    
    def __mul__(self, other):
        return self.composePerms(self, other)
    
    # Calculate the composition of two permutations
    def composePerms(self, perm1, perm2, firstpos = 1):
        plist1 = perm1.permlist
        plist2 = perm2.permlist
        permlen = len(plist1)
        if permlen != len(plist2):
            raise ValueError("Permutation lengths do not match")

        # compute an array that is the composition of plist1 * plist2
        plist3 = [plist2[ plist1[i]-1 ] for i in range(permlen)]
        return Permutation(plist3, permlen)

