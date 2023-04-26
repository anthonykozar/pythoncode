import operator

alphabet="abcdefghijklmnopqrstuvwxyz"

HAS = ['aa', 'abscissas', 'dad', 'deeded', 'kook', 'loll', 'muumuu', 'pullup',
       'referee', 'renaissance', 'rotisserie', 'senescence', 'skedaddled',
       'subcommittee', 'subcommittees', 'synonyms', 'tattletale']

HASNOT = ['a', 'abbesses', 'aimlessness', 'automation', 'baroque', 'circadian',
          'deduce', 'effervescent', 'erroneously', 'error', 'gigawatt',
          'grammar', 'inconspicuousness', 'master', 'mississippi', 'mondo',
          'oversimplification', 'resistance', 'rotisseries', 'tattletales',
          'tests', 'three', 'torturous', 'tree', 'trees', 'up']

def addletters(s):
    sum = 0
    for c in s:
        val = alphabet.find(c) + 1
        sum = sum + val
    return sum

def reversestr(s):
    # return reduce(operator.add, [s[c] for c in range(len(s)-1, -1, -1)])
    return s[-1::-1]

def PrintStrAndReverse(s):
    print s
    print s[-1::-1]

def mirror(s):
    newstr = ""
    for c in s:
        idx = 25 - alphabet.find(c)  # reverse letters in alphabet
        newstr = newstr + alphabet[idx]
    return newstr

def sortletters(koan):
    return reduce(operator.concat, sorted(koan))

def CheckZendo35003(koan):
    last = len(koan) / 2
    has = False
    for i in range(last):
        # print koan[i], koan[-(i+1)]
        if koan[i] == koan[-(i+1)]:
            has = True
            break
    return has

def evalkoan(s):
    print s, '  ',
    print CheckZendo35003(s)

map(evalkoan, HAS)
print '-------------------------------'
map(evalkoan, HASNOT)
