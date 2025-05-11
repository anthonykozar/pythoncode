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

# Group should probably inherit from a Set class (or built-in set?)
class Group(object):
    # 'elements' should be a list of GroupElement objects that determines 
    # the order of the elements used in the operator table and in any group ring vectors.
    # 'operatorTable' should be a list of lists of the GroupElement objects in 
    # 'elements'. Each sublist is one row of the group's Cayley table. The result 
    # of the group operation a*b should be at operatorTable[a][b].
    def __init__(self, name, elements, operatorTable, operatorSymbol = ""):
        self.name = name
        self.elemlist = elements
        self.operatorTable = operatorTable
        self.operatorName = operatorSymbol
        self.order = len(self.elemlist)
        self._makeMaps()
    
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
    def doOperation(self, left, right):
        if left.group == self and right.group == self:
            li = self.name2indexmap[left.name]
            ri = self.name2indexmap[right.name]
            return self.operatorTable[li][ri]
        else:
            raise ValueError("Group element is not a member of this group.")

class CyclicGroup(Group):
    def __init__(self, order):
        #FIXME: name = u'\N{DOUBLE-STRUCK CAPITAL Z}' + '_' + str(order)
        name = 'Z_' + str(order)
        elems = [CyclicGroupElement(i, self) for i in range(order)]
        op = [[elems[(a+b)%order] for b in range(order)] for a in range(order)]
        Group.__init__(self, name, elems, op, '+')

