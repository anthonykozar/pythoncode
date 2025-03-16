# digits.py

# Operations on the (base 10) digits of integers

import operator

def sumdigits(num):
    digits = str(num)
    sum = 0
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            sum += int(dgt)
    return sum

def digitalroot(num):
    while num > 9:
        num = sumdigits(num)
    return num

def digitproduct(num):
    digits = str(num)
    product = 1
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            product *= int(dgt)
    return product

def persistance(num):
    pers = 0
    while num > 9:
        num = digitproduct(num)
        pers += 1
    return pers

def displaypersistance(num):
    pers = 0
    print num,
    while num > 9:
        num = digitproduct(num)
        pers += 1
        print "->", num,
    print
    return pers

def countpersistances(max):
    counts = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in xrange(1,max+1):
        counts[persistance(i)] += 1
    return counts

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

def reversedigits(num):
    digits = str(num)
    rvrs = ""
    for dgt in digits:
        # print dgt,
        rvrs = dgt + rvrs
    return int(rvrs)

def sortdigits(num):
    digits = list(str(num))
    digits.sort()
    inorder = reduce(operator.add, digits)
    return inorder

def digitsalldiff(n):
    sortedstr = sortdigits(n)
    for i in xrange(len(sortedstr) - 1):
        if sortedstr[i] == sortedstr[i+1]:
            return False
    return True
