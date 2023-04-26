# Determine the best value N for the following Zendo rule:

# A koan (could be integers only or any real with a finite decimal expansion)
# HTBN iff the sum of its digits is not more than N times the number of digits.
# (no leading or trailing zeros: 1.20 treated as 1.2; 0.12 treated as .12?)

def sumdigits(num):
    digits = str(num)
    sum = 0
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            sum += int(dgt)
    return sum

def countdigits(numberOrString):
    # if numberOrString is 
    digits = str(numberOrString)
    founddecimalpt = False
    leading = True
    trailingzerocount = 0
    count = 0
    for dgt in digits:
        # 0 requires special handling
        if dgt == '0':
            # ignore leading zeros before the decimal point
            if not leading:
                count += 1
                if founddecimalpt:
                    # count number of consecuetive zeros after the decimal point
                    trailingzerocount += 1
        # digits other than 0
        elif dgt.isdigit():
            count += 1
            leading = False
            trailingzerocount = 0
        elif dgt == '.':
            founddecimalpt = True
            leading = False
            trailingzerocount = 0
        elif dgt == '+' or dgt == '-':
            pass # ignore
        else:
            print "Invalid character: %s" % dgt
    # ignore trailing zeros after the decimal point
    if trailingzerocount > 0:
        count -= trailingzerocount
    return count

# Since koans do not have leading or trailing zeros,
# the unique koans of length k have the forms
#     [1-9][0-9]{k-1}
#     [1-9][0-9]{k-2}.[1-9]
#     [1-9][0-9]{k-3}.[0-9][1-9]
#     ...
#     .[0-9]{k-1}[1-9]

def testintrange(numdigits, Nfactor):
    smallest = 10**(numdigits-1)
    largest = 10**(numdigits) - 1
    print smallest, "...", largest
    HAVEcount = HAVENOTcount = 0
    maxsum = numdigits * Nfactor
    for num in range(smallest, largest+1):
        if sumdigits(num) <= maxsum:
            HAVEcount += 1
        else:
            HAVENOTcount += 1
    print "HAVEs: ", HAVEcount
    print "NOTs: ", HAVENOTcount
    return HAVEcount, HAVENOTcount

def testuptodigits(maxdigits, Nfactor):
    HAVEtotal = NOTtotal = 0
    for numdigits in range(1, maxdigits+1):
        have, havenot = testintrange(numdigits, Nfactor)
        HAVEtotal += have
        NOTtotal += havenot
    print "TOTALS:"
    print "HAVEs: ", HAVEtotal
    print "NOTs: ", NOTtotal

def testNfactors(maxdigits):
    for Nfactor in range(1,10):
        print "NFACTOR: ", Nfactor
        testuptodigits(maxdigits, Nfactor)
        print
        print
