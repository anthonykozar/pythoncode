# SequenceConstraints.py
#
# Anthony Kozar
# May 21, 2026

class SequenceConstraints(object):
    MODE_RESET = 1
    MODE_REPLACE = 2
    MODE_MERGE = 2
    
    def __init__(self, constraintstr = ""):
        self.setConstraints(constraintstr, mode = self.MODE_RESET)
    
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
            
            i += 1
        return self
    
    def test(self, seq):
        for i in self._numoptions:
            if not seq[i] in self._numoptions[i]:
                return False
        for i in self._numforbidden:
            if seq[i] in self._numforbidden[i]:
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
