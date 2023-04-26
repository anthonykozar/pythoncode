# Gaot++ Translator
#
# Converts Gaot++ code to and from Forth-like code
# that is easier to understand.
#
# See description of Gaot++ at
# https://esolangs.org/wiki/Gaot%2B%2B
#
# Anthony Kozar
# Nov. 24-27, 2021

import re

# bleet commands
# non-standard extension: "blet" is assumed to be a "no operation" command
BleetCmds = ['', 'noop', '+', '-', 'skip', 'exit', 'revip', 'skipnz', 'skipz',
             'printint', 'printch', 'readint', 'readch', 'dup', 'swap',
             'revstack', 'rot']

# regular expressions for baa and bleet commands
# non-standard extension: "ba" is used to represent pushing 0 on the stack
BaaPattern = re.compile('^ba+$')
BleetPattern = re.compile('^ble+t$')

def ConvertFromGaot(code):
    output = ''
    lines = code.splitlines()  # keep line breaks
    for line in lines:
        lineout = ''
        words = line.split()
        for word in words:
            if BaaPattern.match(word):
                numvalue = len(word) - 2
                lineout += str(numvalue) + ' '
            elif BleetPattern.match(word):
                commandidx = len(word) - 3
                if commandidx > 0 and commandidx < 17:
                    lineout += BleetCmds[commandidx] + ' '
                else:
                    print "Error: unknown bleet command: " + word
                    return output + lineout
            else:
                print "Error: illegal token: " + word
                return output + lineout
        lineout = lineout.strip() + '\n'
        output += lineout
    return output

# regular expression for non-negative integers
IntPattern = re.compile('^0|[1-9][0-9]*$')

def ConvertToGaot(code):
    output = ''
    lines = code.splitlines()  # keep line breaks
    for line in lines:
        lineout = ''
        words = line.split()
        for word in words:
            if IntPattern.match(word):
                numvalue = int(word)
                lineout += 'b' + 'a' * (numvalue+1) + ' '
            else:
                try:
                    bleetlen = BleetCmds.index(word, 1) # don't match ''
                    lineout += 'bl' + 'e'*bleetlen + 't '
                except ValueError:
                    print "Error: illegal token: " + word
                    return output + lineout
        lineout = lineout.strip() + '\n'
        output += lineout
    return output

# generate a random Gaot program
def RandomGaotProgram(size = 10):
    import random
    
    output = ''
    for i in range(size):
        baacmd = random.choice([True, False])
        if baacmd:
            output += 'b' + 'a' * (random.randrange(20)+1) + ' '
        else:
            output += 'bl' + 'e' * random.randrange(1,len(BleetCmds)) + 't '

    return output.strip()

def TestConversions():
    # test baa command conversion 
    baas = ' '.join(['b'+('a'*(i+1)) for i in range(20)])
    if baas == ConvertToGaot(ConvertFromGaot(baas)).strip():
        print "baa command conversion: passed"
    else:
        print "baa command conversion: failed"
    
    # test bleet command conversion 
    bleets = ' '.join(['bl'+('e'*i)+'t' for i in range(1,len(BleetCmds))])
    if bleets == ConvertToGaot(ConvertFromGaot(bleets)).strip():
        print "bleet command conversion: passed"
    else:
        print "bleet command conversion: failed"

    # test conversion of random programs
    for i in range(5):
        print "-------"
        gaot = RandomGaotProgram()
        print gaot + '\n'
        forth = ConvertFromGaot(gaot)
        print forth
        gaot2 = ConvertToGaot(forth)
        print gaot2
        if gaot == gaot2.strip():
            print "random program %d conversion: passed" % (i+1)
        else:
            print "random program %d conversion: failed" % (i+1)

