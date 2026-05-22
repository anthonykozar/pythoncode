# SequenceConstraints.py
#
# Anthony Kozar
# May 21, 2026

# Base class for all constraints
# Subclasses should override test() to implement their own constraint(s).
# This class just tests that the sequence is nonempty.
class Constraint(object):
    def __init__(self):
        pass
    
    # seq is a list of integers
    # Returns True if seq satisfies the constraint and False if it doesn't.
    def test(self, seq):
        return len(seq) > 0

class BinaryRelation(Constraint):
    TYPE_ADJACENT = 1
    TYPE_NOT_ADJACENT = 2
    TYPE_LESS_THAN = 3
    TYPE_GREATER_THAN = 4
    
    def __init__(self, ctype, idx1, idx2, result = None):
        self.type = ctype
        self.idx1 = idx1
        self.idx2 = idx2
        self.result = result
    
    def test(self, seq):
        # check that indices are not too high
        if self.idx1 >= len(seq) or self.idx2 >= len(seq):
            return False
        # check relation by type
        if self.type == self.TYPE_ADJACENT:
            return (seq[self.idx1] == seq[self.idx2] + 1) or (seq[self.idx1] == seq[self.idx2] - 1)
        elif self.type == self.TYPE_NOT_ADJACENT:
            return (seq[self.idx1] != seq[self.idx2] + 1) and (seq[self.idx1] != seq[self.idx2] - 1)
        elif self.type == self.TYPE_LESS_THAN:
            return seq[self.idx1] < seq[self.idx2]
        elif self.type == self.TYPE_GREATER_THAN:
            return seq[self.idx1] > seq[self.idx2]
        else:
            raise ValueError("Unknown constraint type %s in BinaryRelation object." % str(self.type))

class SequenceConstraints(Constraint):
    MODE_RESET = 1
    MODE_REPLACE = 2
    MODE_MERGE = 2
    
    def __init__(self, constraintstr = ""):
        self.setConstraints(constraintstr, mode = self.MODE_RESET)
    
    # creates multiple constraints by parsing an input string
    def setConstraints(self, constraintstr, mode = MODE_REPLACE):
        if mode == self.MODE_RESET:
            self._numoptions = {}
            self._numforbidden = {}
            self._relations = []
        # interpret the string arg
        i = 0
        seqidx = 0
        # readingset = False
        s = constraintstr
        while i < len(s):
            if s[i] == '_':
                seqidx += 1
            elif s[i].isdigit():
                opt = set([int(s[i])])
                self._numoptions[seqidx] = opt
                seqidx += 1
            elif s[i] == '(':
                # read a set of single-digit options and/or forbidden numbers
                i += 1
                opt = set()
                readforb = False
                while s[i] != ')' and i < len(s):
                    if s[i] == '~':
                        readforb = True
                        forb = set()
                    elif s[i].isdigit():
                        if readforb:
                            forb.add(int(s[i]))
                        else:
                            opt.add(int(s[i]))
                    i += 1
                if len(opt) > 0:
                    self._numoptions[seqidx] = opt
                if readforb and len(forb) > 0:
                    self._numforbidden[seqidx] = forb
                seqidx += 1
            elif s[i] == '|':
                # nums before and after | must be adjacent integers
                self._relations.append(BinaryRelation(BinaryRelation.TYPE_ADJACENT, seqidx-1, seqidx))
            elif s[i] == '!':
                # nums before and after ! cannot be adjacent
                self._relations.append(BinaryRelation(BinaryRelation.TYPE_NOT_ADJACENT, seqidx-1, seqidx))
            elif s[i] == '<':
                # num before < must be less than the num after
                self._relations.append(BinaryRelation(BinaryRelation.TYPE_LESS_THAN, seqidx-1, seqidx))
            elif s[i] == '>':
                # num before > must be greater than the num after
                self._relations.append(BinaryRelation(BinaryRelation.TYPE_GREATER_THAN, seqidx-1, seqidx))
            i += 1
        return self
    
    def test(self, seq):
        for i in self._numoptions:
            if not seq[i] in self._numoptions[i]:
                return False
        for i in self._numforbidden:
            if seq[i] in self._numforbidden[i]:
                return False
        for rel in self._relations:
            if not rel.test(seq):
                return False
        return True
    
    def enumeratePermutations(self, permlen, permelements = None):
        from itertools import permutations
        if permelements == None:
            permelements = xrange(1, permlen+1)
        for p in permutations(permelements, permlen):
            if self.test(p):
                print p

'''
c = SequenceConstraints("(12)(14)(356)(24)(15)(356)")
c.enumeratePermutations(6)

c = SequenceConstraints("_|_|(~1)!7!(45)|(3456)!(~6)!_")
c.enumeratePermutations(8)
'''

def countnoadjaciences(permlen):
    from itertools import permutations
    def noadj(p):
        for i in xrange(1, len(p)):
            if (p[i]+1 == p[i-1]) or (p[i]-1 == p[i-1]):
                return False
        return True
    count = 0
    for p in perm(xrange(permlen)):
        if noadj(p): count += 1
    return count
