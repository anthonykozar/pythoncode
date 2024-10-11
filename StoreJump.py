# Interpreter for the Store-Jump esolang
# 
# Anthony Kozar
# Oct. 9-10, 2024

import sys
from collections import defaultdict

# Memory is represented as a dict indexed by 
# non-negative integers so that it can be discontiguous.
Memory = defaultdict()

# I/O port addresses
kInputInteger = 102
kOutputInteger = 107
kInputChar = 112
kOutputChar = 117

def readmemory(address, mem):
    val = mem[address]
    return val

# Returns True if the memory location is changed or if writing to an output port.
def writememory(address, val, mem):
    if address == kOutputChar:
        sys.stdout.write(unichr(val))
        return True
    elif address == kOutputInteger:
        sys.stdout.write(str(val))
    else:
        oldval = mem[address]
        mem[address] = val
        return oldval != val

def runprogram(mem):
    pc = 0
    running = True
    while running:
        # read all operands before executing!
        data = readmemory(pc, mem)
        storeaddr = readmemory(pc+1, mem)
        jumpaddr = readmemory(pc+2, mem)
        # execute the instruction
        changed = writememory(storeaddr, data,  mem)
        # check for an infinite loop
        # (FIXME: this is too simplistic)
        if not changed and pc == jumpaddr:
            running = False
        pc = jumpaddr

def makehelloworld(message = 'Hello World!\n'):
    prog = []
    jumpaddr = 3
    for c in message:
        prog.append(ord(c))
        prog.append(kOutputChar)
        prog.append(jumpaddr)
        jumpaddr += 3
    # create an infinite loop to halt
    jumpaddr -= 3
    prog += [0, jumpaddr, jumpaddr]
    return prog

def list2memory(vals, startaddr = 0):
    d = {i+startaddr:vals[i] for i in xrange(len(vals))}
    return defaultdict(int, d)

# Memory = list2memory(makehelloworld())
printints = [1, kOutputInteger, 3, 22, kOutputInteger, 6, 333, kOutputInteger, 9, 4444, kOutputInteger, 12, 0, 12, 12]
Memory = list2memory(printints)

runprogram(Memory)
