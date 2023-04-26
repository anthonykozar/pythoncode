# Tag system emulator
#
# https://esolangs.org/wiki/Tag_system
# https://en.wikipedia.org/wiki/Tag_system
#
# Anthony Kozar
# May 30, 2019


# Example: Computation of Collatz sequences (from Wikipedia)
#    2-tag system 
#    Alphabet: {a,b,c} 
#    Production rules:
#         a  -->  bc
#         b  -->  a
#         c  -->  aaa
# A positive integer n is represented by the word aa...a with n a's.
Collatz_rules = { 'a': 'bc', 'b': 'a', 'c': 'aaa' }

def onlyintegers(s):
    i = len(s)
    if s == 'a' * i:
        print i

double = {'1':'abb', 'a':'$', 'b':'11'}

def PrintState(s):
    print s

def EmulateTagSystem(m, haltsymbol, rules, startstr, outfunc = PrintState):
    outfunc(startstr)
    state = startstr
    first = state[0]
    while len(state) >= m and first != haltsymbol:
        state = state[m:] + rules[first]
        outfunc(state)
        first = state[0]

# Ex. calls
EmulateTagSystem(2, '$', Collatz_rules, 'aaa')
EmulateTagSystem(2, '$', Collatz_rules, 'aaa', onlyintegers)
# EmulateTagSystem(2, '$', Collatz_rules, 'aaaaaaa', onlyintegers)
# EmulateTagSystem(2, '$', Collatz_rules, 'a'*15, onlyintegers)
# EmulateTagSystem(2, '$', Collatz_rules, 'a'*800, onlyintegers)
