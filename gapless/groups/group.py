# module gapless.groups.group

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

from .groupelem import GroupElement
from .groupelem import CyclicGroupElement
from .groupelem import Permutation, AUTO_PERM_LEN

MAX_GROUP_SIZE = 10000

# Group should probably inherit from a Set class (or built-in set?)
class Group(object):
    # 'elements' should be a list of GroupElement objects that determines 
    # the order of the elements used in the operator table and in any group ring vectors.
    # 'operatorTable' should be a list of lists of the GroupElement objects in 
    # 'elements'. Each sublist is one row of the group's Cayley table. The result 
    # of the group operation a*b should be at operatorTable[a][b].
    def __init__(self, name, elements, identity, operatorTable, operatorSymbol = ""):
        self.name = name
        self.elemlist = list(elements)
        self.identity = identity
        self.operatorTable = self._copyTable(operatorTable)
        self.operatorName = operatorSymbol
        self.order = len(self.elemlist)
        self._claimElements()
        self._makeMaps()
    
    def _copyTable(self, table):
        return [list(a) for a in table]
    
    def _claimElements(self):
        for e in self.elemlist:
            if e.group == None:
                e.setGroup(self)
    
    def _makeMaps(self):
        self.name2elemmap = {}
        self.name2indexmap = {}
        for i in range(len(self.elemlist)):
            nm = self.elemlist[i].name
            self.name2elemmap[nm] = self.elemlist[i]
            self.name2indexmap[nm] = i
    
    def __str__(self):
        return self.name

    # default code to perform the group operation on two group elements
    # using self.operatorTable
    def doTableOperation(self, left, right):
        if left.group == self and right.group == self:
            li = self.name2indexmap[left.name]
            ri = self.name2indexmap[right.name]
            return self.operatorTable[li][ri]
        else:
            raise ValueError("Group element is not a member of this group.")
    
    def getIdentity(self):
        return self.identity
    
    def _getInverseFromTable(self, element):
        elidx = self.name2indexmap[element.name]
        # search the row corresponding to 'element' for the identity
        for i in range(len(self.operatorTable[elidx])):
            if self.operatorTable[elidx][i] == self.identity:
                # the element corresponding to this column is the inverse
                return self.elemlist[i]
        # operatorTable is not a proper group operation if there is no inverse
        raise ValueError("Group %s has no inverse for element %s" % (self.name, element.name))
    
    def getElementByName(self, name):
        if self.name2elemmap.has_key(name):
            return self.name2elemmap[name]
        else:
            raise ValueError("Group %s has no element with name %s" % (self.name, name))
    
    # Calculate the subgroup generated by a given set of GroupElements
    # that belong to this group. Raises a RuntimeError if more than
    # 'maxelems' elements are generated.
    #
    # WARNING: This method is called by the PermutationGroup constructor
    # before the Group constructor is called. Don't use any attributes
    # set by __init__() or _makeMaps().
    def generateSubgroup(self, generators, maxelems = MAX_GROUP_SIZE):
        # make a queue of elements to check
        elemsToCheck = list(generators)
        # make a dict mapping element names to GroupElements
        subgroup = {g.name:g for g in generators}
        while (len(elemsToCheck) > 0):
            p1 = elemsToCheck.pop(0)
            for p2 in subgroup.values():  # can't use itervalues() b/c subgroup changes
                p1p2 = p1 * p2
                if not subgroup.has_key(p1p2.name):
                    subgroup[p1p2.name] = p1p2
                    elemsToCheck.append(p1p2)
                # is this check redundant in all cases??
                p2p1 = p2 * p1
                if not subgroup.has_key(p2p1.name):
                    subgroup[p2p1.name] = p2p1
                    elemsToCheck.append(p2p1)
            if len(subgroup) > maxelems:
                raise RuntimeError("Generated group has more elements than maximum group size.")
        return subgroup.values()

    def leftCoset(self, elem, subgroup):
        return [elem*p for p in subgroup]
    
    def rightCoset(self, elem, subgroup):
        return [p*elem for p in subgroup]
    
    # If 'only1percoset' is True, then only
    # one element of each coset is returned.
    def allLeftCosets(self, subgroup, only1percoset = False):
        return self._findAllCosets(self.leftCoset, subgroup, only1percoset)
    
    # If 'only1percoset' is True, then only
    # one element of each coset is returned.
    def allRightCosets(self, subgroup, only1percoset = False):
        return self._findAllCosets(self.rightCoset, subgroup, only1percoset)
    
    def _findAllCosets(self, cosetfunc, subgroup, only1percoset):
        includedelems = list(subgroup)
        cosets = []
        numcosets = self.order / len(subgroup)
        if only1percoset:
            cosets.append(self.identity)
        else:
            cosets.append(list(subgroup))
        for el in self.elemlist:
            # find an element not in any coset yet
            elfound = False
            for el2 in includedelems:
                if el2 == el:
                    elfound = True
                    break
            if elfound: continue
            # make a coset with that element
            elcoset = cosetfunc(el, subgroup)
            if only1percoset:
                cosets.append(elcoset[0])
            else:
                cosets.append(elcoset)
            if len(cosets) == numcosets:
                break
            includedelems += elcoset
        return cosets

class CyclicGroup(Group):
    def __init__(self, order):
        #FIXME: name = u'\N{DOUBLE-STRUCK CAPITAL Z}' + '_' + str(order)
        name = 'Z_' + str(order)
        elems = [CyclicGroupElement(i, order, self) for i in range(order)]
        op = [[elems[(a+b)%order] for b in range(order)] for a in range(order)]
        Group.__init__(self, name, elems, elems[0], op, '+')

class PermutationGroup(Group):
    # 'generators' should be a list of Permutation objects or a list of values
    # that can be passed as the 'perm' parameter to the Permutation class
    # constructor (i.e. permutation lists or lists of cycles). 'permlen' will be
    # passed to the Permutation constructor too.
    def __init__(self, generators, permlen = AUTO_PERM_LEN):
        # convert a generator to a Permutation object if it isn't one
        def toGeneratorElement(gen):
            if type(gen) == Permutation: return gen
            else: return Permutation(gen, permlen)
        self.genelems = [toGeneratorElement(p) for p in generators]
        elems = self.generateSubgroup(self.genelems)
        # FIXME: need to put the elements in sorted order
        # find the identity element
        idstr = '(' + str(self.genelems[0]. size) + ')'
        for el in elems:
            if el.name == idstr:
                idelem = el
        # FIXME? do we need a mechanism in the Group class to specify when
        # an operator table is not used by a particular subclass?
        op = []
        if len(self.genelems) > 10:
            name = "Permutation group with %d generators" % len(self.genelems)
        else:
            gennames = ", ".join([el.name for el in self.genelems])
            name = "<" + gennames + ">"
        Group.__init__(self, name, elems, idelem, op, '')
