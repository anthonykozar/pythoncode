# numbases.py

# convert an integer to a string in base 2-26
def baseconvert(val,base):
    if base > 26:
        return "Error: base > 26"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basestr = ""
    while val > 0:
        rmndr = val % base
        val = val // base
        basestr = digits[rmndr] + basestr
    if basestr == "":
        basestr = "0"
    return basestr

# reinterpret an integer or numeric string as another base and return an integer
def base16to10(hexnumstr):
    return int(str(hexnumstr), 16)

def base12to10(num):
    return int(str(num), 12)

def rebase(num, base):
    return int(str(num), base)

# interpret an integer or numeric string as "base -2" and convert to base 10
def baseneg2to10(num):
    digits = list(str(num))
    digits.reverse()
    placevals = [int(digits[i])*((-2)**i) for i in range(len(digits))]
    return sum(placevals)
