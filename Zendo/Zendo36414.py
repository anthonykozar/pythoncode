# Zendo #36414

HAS = ["0.0", "0.01", "0.0101", "0.010101", "0.0102", "0.010201", "0.012",
       "0.01212", "0.0123", "0.02", "0.3", "3.0", "3.01", "3.02", "3.3",
       "10.3", "210.0101", "102010.0"]

NOT = ["0.001010101", "0.010203", "0.010301", "0.01030301", "0.0123456789",
       "0.030201", "0.06", "0.3132", "0.33", "0.7", "1.0", "1.03", "1.3",
       "1.4153", "2.0", "2.99", "3.001", "3.03", "3.08", "3.1", "3.1415",
       "3.31", "3.3333333", "3.6414", "4.3", "5.0", "6.3", "8.0", "9.0",
       "13.0", "62.5", "200.0", "310.0101"]

NOT4 = ["0.001010101", "0.010203", "0.010301", "0.01030301", 
       "0.030201", "0.3132", "0.33", "1.0", "1.03", "1.3",
       "2.0", "3.001", "3.03", "3.1", 
       "3.31", "3.3333333", 
       "13.0", "200.0", "310.0101"]

# Convert a floating-point number in another base to base 10 float 
def fconvertbase(num, base = 4):
    if type(num) != str:
        num = str(num)

    intstr, fracstr = num.split('.')
    return int(intstr, base) + float(int(fracstr, base)) / base**len(fracstr)

def evall(fn, haslist = HAS, hasnot = NOT):
    print "HAS"
    print "---"
    map(fn, haslist)
    print "\nHAS NOT"
    print "-------"
    map(fn, hasnot)
    print

def printbase4_10(n):
    print "%-12s   " % n, fconvertbase(n)

evall(printbase4_10, HAS, NOT4)
print

# Apply a "string substitution" to strin using dictionary subtable.
# (i.e. replace each character in strin with its corresponding string
# in subtable).
def strsubstitute(strin, subtable):
    charlist = list(strin)
    sublist = map(lambda x: subtable[x], charlist)
    return "".join(sublist)

# convert base 4 to base 2 with a string substitution
base4to2 = {'0':'00', '1':'01', '2':'10', '3':'11', '.':'.'}
def printbase4_2(n):
    print "%-12s   " % n, strsubstitute(n, base4to2)

evall(printbase4_2, HAS, NOT4)
