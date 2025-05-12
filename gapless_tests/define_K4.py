# define_K4.py
#
# Part of the Gapless test suite.
#
# Define K_4, the "Klein 4" group and test its properties.

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
k4 = Group("K_4", [e,a,b,ab], op)

ReportTestResult(list(map(str, k4.elemlist)) == ['e', 'a', 'b', 'ab'], "Element names set and returned by str()")

ReportTestResult(all([el.group == k4 for el in k4.elemlist]), "'group' attribute of elements set correctly")

opresults = [[e*e,e*a,e*b,e*ab], [a*e,a*a,a*b,a*ab], [b*e,b*a,b*b,b*ab], [ab*e,ab*a,ab*b,ab*ab]]

ReportTestResult(opresults == k4.operatorTable, "Multiplying all pairs of elements matches the operator table")
