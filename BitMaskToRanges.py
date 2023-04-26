# Convert a bit mask to a list of ranges indicating which bits are set.
# E.g. 215 = 0b11010111 has bits '0-2,4,6-7' set.
# lowestbitnum allows the bits to be numbered starting from any value. 
def BitMaskToRanges(mask, lowestbitnum = 0):
    out = ""
    testbit = 1
    bitnum = lowestbitnum
    first = lowestbitnum - 2
    haveFirst = False
    haveHyphen = False
    while mask:
        if (mask & testbit):
            if not haveFirst:
                # this is the first # in a new range
                out += str(bitnum)
                haveFirst = True
                first = bitnum
            elif not haveHyphen:
                if bitnum == (first+1):
                    # this range has 2+ consecutive values
                    out += "-"
                    haveHyphen = True
                else:
                    print "Logic error 1"
            # elif haveHyphen: range is expanding
            # remove testbit from mask
            mask -= testbit
        else:
            # testbit not present
            if haveHyphen:
                # output end of range value
                out += str(bitnum-1) + ","
            elif haveFirst:
                # this is a single-value range
                out += ","
            # else: was not in a range
            # reset to no range state
            haveFirst = False
            haveHyphen = False            
        
        # next bit
        testbit <<= 1
        bitnum += 1

    # finish last range if hyphenated
    if haveHyphen:
        out += str(bitnum-1)
    
    return out
