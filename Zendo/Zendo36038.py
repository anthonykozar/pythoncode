# Zendo #36038

HAS = ["*", "***", "*****", "**666666**", "*\"6\"*", "*\"MY\"*", "*>*", "*6*",
       "*6kwk6*", "*666*", "\"", "\"66\"", "\"MY\"", ">", ">>>", "6", "6kwk6",
       "66", "666", "A", "I", "k", "kkkwwwwwwkkk", "kwk", "M*Y", "MAY", "MMAAYY",
       "MMMAAAYYY", "MMYMYY", "MY", "U", "UUU", "UwU", "w", "YAM", "YUM"]

NOT = ["_", "_k_", "!", "...", "'", "**>", "*6AMUkw", "*6B*B6*", "//",
       "\"*6>IkU", "\"666***MAY\"", "\"ma\"", "&", "#", "^_^",
       "</html>", "<>", "$66", "$666", "000", "3", "6******", "6kw",
       "8", "444", "567", "77777", "123456789", "a", "AMUY", "AMY",
       "amy66", "AYM", "B", "BOW", "E", "I'M_STUMPED", "I>", "K", "KAY",
       "kkkwwwwwwkkkk", "kUUw", "KwkMAY", "M", "M+A+Y+B+E", "MAM",
       "MARCH", "MAW", "may", "MAY>kwk", "MI6", "Mk6", "MYA", "OUIE",
       "P", "pwp", "U*", "uWu", "xXx", "Y", "YMA"]


def evall(fn, haslist = HAS, hasnot = NOT):
    print "HAS"
    print "---"
    map(fn, haslist)
    print "\nHAS NOT"
    print "-------"
    map(fn, hasnot)
    print

def printASCIIcodes(s):
    print '%15s  ' % s,
    for c in s:
        print ord(c),
    print

def printASCIIhexcodes(s):
    print '%15s  ' % s,
    for c in s:
        print hex(ord(c))[2:],
    print

def printASCIIdifferences(s):
    print '%15s  ' % s,
    last = 0
    for c in s:
        cur = ord(c)
        print cur-last,
        last = cur
    print

# evall(printASCIIhexcodes)

def ASCIIto7bitBinary(c):
    binstr = bin(ord(c))[2:]
    # pad to 7 bits
    binstr = '0'*(7-len(binstr)) + binstr
    return binstr

def isPalindrome(s):
    r = list(s)
    r.reverse()
    r = "".join(r)
    return s == r

# find printable ASCII characters with 7-bit binary codes that are palindromes
print "Characters that have the Buddha nature on their own:"
for i in xrange(33,127):
    binstr = ASCIIto7bitBinary(chr(i))
    if isPalindrome(binstr):
        print chr(i), "  ", binstr

print
print

# find printable ASCII character pairs whose 7-bit binary codes are mirrors of each other
print "Characters that don't have the Buddha nature but are HAS-able:"
for i in xrange(33,127):
    binstr = ASCIIto7bitBinary(chr(i))
    r = list(binstr)
    r.reverse()
    r = "".join(r)
    rn = int(r, 2)
    if binstr != r and rn > 32 and rn < 127:
        print chr(i), "  ", binstr, "  ", chr(rn), "  ", r

print
print

# find printable ASCII characters that are in neither of the above groups
print "Characters that are not HAS-able:"
for i in xrange(33,127):
    binstr = ASCIIto7bitBinary(chr(i))
    r = list(binstr)
    r.reverse()
    r = "".join(r)
    rn = int(r, 2)
    if rn <= 32 or rn == 127:
        print chr(i), "  ", binstr
