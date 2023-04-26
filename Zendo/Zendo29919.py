def num2digitarray(num):
    return map(int, str(num))

def sumdigits(num):
    return sum(num2digitarray(num))

def countNumsThatPassTest(low, high, test):
    count = 0
    for i in range(low, high+1):
        if test(i):
            count += 1
    return count

def onlyevendigits(num):
    digits = num2digitarray(num)
    onlyeven = True
    for d in digits:
        if (d % 2) != 0:
            onlyeven = False
    return onlyeven

def onlyodddigits(num):
    digits = num2digitarray(num)
    onlyodd = True
    for d in digits:
        if (d % 2) == 0:
            onlyodd = False
    return onlyodd

def oneevenandoneodd(num):
    digits = num2digitarray(num)
    even = odd = 0
    for d in digits:
        if (d % 2) == 0:
            even += 1
        else:
            odd += 1
    return ((even==1) and (odd==1))

def digitsumlessthan10(num):
    dsum = sumdigits(num)
    return (dsum < 10)

def exactlytwodigits(num):
    return ((num>9) and (num<100))

def exactly2digits2nddigit1(num):
    return (exactlytwodigits(num) and (num%10) == 1)

def firstdigiteven2nddigit9minus1st(num):
    digits = num2digitarray(num)
    if len(digits) != 2:
        return False
    return ((digits[0]%2)==0 and digits[1]==(9-digits[0]))

def firstdigitodd2nddigit0(num):
    digits = num2digitarray(num)
    if len(digits) < 2:
        return False
    return ((digits[0]%2)==1 and digits[1]==0)
