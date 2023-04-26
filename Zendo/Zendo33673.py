# Zendo game #33673

HAS = ['ABABAABAB', 'ABBBAABAB', 'ABCBAABAB', 'ABEANTREE', 'AKOANADAY', 'AKOANADAZ',
       'ALOAFADAY', 'AMOMENTUM', 'ARTHEOUSY', 'ELUEPEFEZ', 'OMOMOMTOM', 'PIPIEPIPE',
       'PIPIEPIPI', 'PIPIFPIPI', 'PIPIPPIPI', 'POPOPPOPO', 'UKUUNUDUY', 'YADANAOKA']

NOT = ['AAAAAAAAA', 'AAAAAAAAB', 'AAAABAAAA', 'ABABABABA', 'ABACDCABA', 'ABACDEABA',
       'ABBBAABBB', 'ABCABCABC', 'ABCBCACAB', 'ABCBCACCC', 'ABCDEFGHI', 'AKOANADAU',
       'ASHEALTHY', 'BAAAAAAAA', 'BLPBOBEBZ', 'BLUETOOOT', 'BLUETOOTH', 'CDCDCCDCD',
       'EEEFFFGGG', 'ISHEALTHY', 'KAOANADAU', 'KOANADAYA', 'KUUNUDUYU', 'NAAAAOYKD',
       'PIPIPIPIP', 'QRQRQRQRQ', 'TOMORROWS', 'UMMMMMMMM']

# Returns a string with every vowel in the koan replaced by 'v' and
# every consonant replaced by 'c'.
def VCProfile(koan):
    profile = ""
    for letter in koan:
        if letter in 'AEIOU':
            profile += 'v'
        else:
            profile += 'c'
    return profile

def VCCount(profile):
#    v = 0
#    c = 0
#    for letter in profile:
#        if letter is 'v':
#            v += 1
#        else:
#            c += 1
    return (profile.count('v'), profile.count('c'))

# Reverse a string
def strreverse(s):
    out = ''
    for c in s:
        out = c + out
    return out

def GenerateAllBinaryStrings(length):
    numstr = 2**length
    out = list()
    for i in range(numstr):
        unpaddedstr = bin(i)[2:]
        out.append('0'*(length-len(unpaddedstr)) + unpaddedstr)
    return out


hasp = map(VCProfile, HAS)
notp = map(VCProfile, NOT)
hasset = set(hasp)
notset = set(notp)
revhasset = set(map(strreverse, hasset))
revnotset = set(map(strreverse, notset))

print set.intersection(hasset, notset)
print set.intersection(revhasset, revnotset)
print set.intersection(revhasset, notset)
print set.intersection(hasset, revnotset)
