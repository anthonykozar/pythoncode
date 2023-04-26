# Calculations related to rooted trees

# OEIS Sequence A000081: Number of rooted trees with n nodes
# http://oeis.org/A000081
A000081 = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, 12486, 32973,87811, 235381,
           634847, 1721159, 4688676, 12826228, 35221832, 97055181, 268282855, 743724984,
           2067174645, 5759636510, 16083734329, 45007066269, 126186554308, 354426847597]

def PrintSequenceInfo(seq):
    # Prints the following table for sequence a(n):
    #
    #   n            a(n)    a(n)-a(n-1)    a(n)/a(n-1)
    # -------------------------------------------------
    # [ 2]              1              0          1.000

    print "  n            a(n)    a(n)-a(n-1)    a(n)/a(n-1)"
    print "-------------------------------------------------"
    print "[%2s] %14s" % (0, seq[0])
    print "[%2s] %14s %14s" % (1, seq[1], seq[1]-seq[0])
    for i in range(2, len(seq)):
        print "[%2s] %14s %14s %14.3f" % (i, seq[i], seq[i]-seq[i-1], float(seq[i])/seq[i-1])


# An efficient method for computing the sequence.
# Adapted from Maple code at http://oeis.org/A000081
# submitted by Joe Riel (joer(AT)san.rr.com), Jun 23 2008.

# Original Maple code:
#   a := proc(n) local k; a(n) := add(k*a(k)*s(n-1, k), k=1..n-1)/(n-1) end proc:
#   a(0) := 0: a(1) := 1: s := proc(n, k) local j; s(n, k) := add(a(n+1-j*k), j=1..iquo(n, k));

def NumRootedTreesSequence(maxnodes, trace = False):
    ntrees = [0, 1]
    for n in range(2,maxnodes+1):
        nextsum = 0
        # compute a(n)
        if (trace): print "Computing a(%s)..." % n
        for k in range(1,n):
            # compute s(n-1, k)
            if (trace): print "  Computing s(%s,%s)..." % (n-1, k)
            s = 0
            if (trace): ss = "    s ="
            for j in range(1, ((n-1)/k)+1):
                s += ntrees[n-j*k]
                if (trace): ss += (" a(%s) +" % (n-j*k))
            if (trace):
                print ss
                print "    s = %s" % s
            nextsum += k * ntrees[k] * s
            if (trace): print "  accum %s = %s * ntrees[%s] * %s" % (k * ntrees[k] * s, k, k, s)
        ntrees.append(nextsum/(n-1))
        if (trace): print "a(%s) = %s" % (n, nextsum/(n-1))
    return ntrees

def TestAlg1():
    ntrees = NumRootedTreesSequence(30)
    print ntrees
    print
    PrintSequenceInfo(ntrees)

# The following is Sage code which is also Python ??? (with libraries)
# for calculating the nth member of the sequence.
# Also from http://oeis.org/A000081
# submitted by Peter Luschny, Jul 18 2014, after Maple code by Alois P. Heinz
# def a(n):
#     if n < 2: return n
#     return add(add(d*a(d) for d in divisors(j))*a(n-j) for j in (1..n-1))/(n-1)
#
# [a(n) for n in (0..30)]

# My adaptation DOESN'T WORK!
def divisors(k):
    d = [1]
    for i in range(2,k):
        if (k%i == 0):
            d.append(i)
    d.append(k)
    return d

def a(n):
    if n < 2: return n
    return sum(sum(d*a(d) for d in divisors(j))*a(n-j) for j in range(1, n))/(n-1)

def TestAlg2():
    print [a(n) for n in range(0, 9)]

# List of rooted trees with 6 nodes
# Each sublist is one tree in the "parent array" format:
#   There is one integer for each node which are numbered 1 to n.
#   The value of the integer specifies the parent node of that node.
#   '0' is used for the root node which has no parent.
trees6 = [ [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 4],
    [0, 1, 2, 3, 4, 3],
    [0, 1, 2, 3, 4, 2],
    [0, 1, 2, 3, 4, 1],
    [0, 1, 2, 3, 3, 3],
    [0, 1, 2, 3, 3, 2],
    [0, 1, 2, 3, 3, 1],
    [0, 1, 2, 3, 2, 5],
    [0, 1, 2, 3, 2, 2],
    [0, 1, 2, 3, 2, 1],
    [0, 1, 2, 3, 1, 5],
    [0, 1, 2, 3, 1, 1],
    [0, 1, 2, 2, 2, 2],
    [0, 1, 2, 2, 2, 1],
    [0, 1, 2, 2, 1, 5],
    [0, 1, 2, 2, 1, 1],
    [0, 1, 2, 1, 4, 1],
    [0, 1, 2, 1, 1, 1],
    [0, 1, 1, 1, 1, 1]]

# List of rooted trees with 5 nodes
trees5 = [ [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 3],
    [0, 1, 2, 3, 2],
    [0, 1, 2, 3, 1],
    [0, 1, 2, 2, 2],
    [0, 1, 2, 2, 1],
    [0, 1, 2, 1, 4],
    [0, 1, 2, 1, 1],
    [0, 1, 1, 1, 1]]

# List of rooted trees with 4 nodes
trees4 = [ [0, 1, 2, 3],
    [0, 1, 2, 2],
    [0, 1, 2, 1],
    [0, 1, 1, 1]]

# "Level array" format is a list of integers, one per node,
# indicating the depth at which to add that node.  The depth
# of the root is 0, its children 1, their children 2, etc.
# The implied parent of a node in a level array is the most recent
# node in the list (before the current node) that has a depth value
# of one less than the current node.
def ParentArrayToLevelArray(parentArray):
    levelArray = []
    for nodeParent in parentArray:
        if (nodeParent == 0):
            levelArray.append(0)
        else:
            # level of node is level of parent + 1
            levelArray.append(levelArray[nodeParent-1]+1)
    return levelArray

def PrintTreeLevelArray(levelArray):
    node = 1
    for nodeLevel in levelArray:
        if (nodeLevel == 0):
            print "  %d" % node
        else:
            print "  "*nodeLevel + "- %d" % node
        node += 1

# Parameter 'trees' should be a list of parent arrays
def TestLevelArrays(trees):
    for tree in trees:
        print tree
        PrintTreeLevelArray(ParentArrayToLevelArray(tree))
        print

# Tree and Node classes

class Node(object):
    def __init__(self, parentNode = None, nodeName = ""):
        self.name = str(nodeName)
        self.children = []
        self.parent = parentNode
        if (self.parent == None):
            self.depth = 0
        else:
            self.parent.addChild(self)
            self.depth = self.parent.depth + 1

    def __str__(self):
        return self.name

    def addChild(self, childNode):
        self.children.append(childNode)
        return self
    
class Tree(object):
    def __init__(self, rootName = "", rootNode = None):
        if (rootNode == None):
            # create a root node if none supplied
            self.root = Node(None, rootName)
        else:
            self.root = rootNode
        self.nodes = [self.root]
    
    def __str__(self):
        return str(map(str, self.nodes))
    
    def createNode(self, parentNode, nodeName = ""):
        if (parentNode in self.nodes):
            newnode = Node(parentNode, nodeName)
            self.nodes.append(newnode)
        else:
            newnode = None
            if (isinstance(parentNode, Node)):
                raise KeyError, "parentNode is not a node in tree %s" % self
            else:
                raise TypeError, "parentNode is not of type Node"
        return newnode
    
    def printTree(self):
        print "  " + self.root.name
        self.printChildren(self.root)

    def printChildren(self, parent):
        for node in parent.children:
            print "  "*node.depth + "- " + node.name
            self.printChildren(node)
    
    def NewTreeFromParentArray(parentArray):
        # name the nodes 1 thru N
        newtree = Tree(1)
        for i in xrange(1, len(parentArray)):
            # this loop assumes the nodes within newtree.nodes
            # will remain in the order in which they are added
            newtree.createNode(newtree.nodes[parentArray[i]-1], i+1)
        return newtree
    NewTreeFromParentArray = staticmethod(NewTreeFromParentArray)
    

# Parameter 'trees' should be a list of parent arrays
def TestNewTree(trees):
    for tree in trees:
        print tree
        Tree.NewTreeFromParentArray(tree).printTree()
        print
