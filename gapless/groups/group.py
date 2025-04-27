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

from groupelem import GroupElement

# Group should probably inherit from a Set class (or built-in set?)
class Group(object):
    def __init__(self, name, elements, operatorTable, operatorSymbol = ""):
        self.name = name
        self.elemlist = elements
        self.operatorTable = operatorTable
        self.operatorName = operatorSymbol
        self.order = len(self.elemlist)

