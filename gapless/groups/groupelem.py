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
        
