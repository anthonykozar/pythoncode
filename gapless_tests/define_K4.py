# define_K4.py
#
# Part of the Gapless test suite.
#
# Define K_4, the "Klein 4" group and test its properties.
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

from gapless.groups import *

def ReportTestResult(cond, testdescr):
    if cond:
        print("[PASS]", testdescr)
    else:
        print("[FAIL]", testdescr)

e = GroupElement("e")
a = GroupElement("a")
b = GroupElement("b")
ab = GroupElement("ab")
op = [[e,a,b,ab],[a,e,ab,b],[b,ab,e,a],[ab,b,a,e]]
k4 = Group("K_4", [e,a,b,ab], e, op)

ReportTestResult(list(map(str, k4.elemlist)) == ['e', 'a', 'b', 'ab'], "Element names set and returned by str()")

ReportTestResult(all([el.group == k4 for el in k4.elemlist]), "'group' attribute of elements set correctly")

opresults = [[e*e,e*a,e*b,e*ab], [a*e,a*a,a*b,a*ab], [b*e,b*a,b*b,b*ab], [ab*e,ab*a,ab*b,ab*ab]]

ReportTestResult(opresults == k4.operatorTable, "Multiplying all pairs of elements matches the operator table")
