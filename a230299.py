# https://oeis.org/A230299

# A230299
# Define a sequence b_s by b_s(1)=s, b_s(k+1)=b_s(k)+(sum of digits of b_s(k)); a(n) is the number of steps needed for b_n to reach a term in one of b_0, b_1, b_3 or b_9, or a(n) = -1 if b_n never joins one of these four sequences.

# sequence values from OEIS (starting with a(0))
A230299 = [0, 0, 0, 0, 0, 52, 0, 11, 0, 0, 51, 50, 0, 49, 10, 0, 0, 48, 0, 9, 50, 0, 49, 0, 0, 47, 48, 0, 0, 8, 0, 49, 46, 0, 47, 48, 0, 45, 0, 0, 7, 46, 7, 47, 6, 0, 45, 44, 6, 0, 46, 0, 5, 5, 0, 45, 44, 0, 43, 4, 5, 4, 0, 0, 4, 44, 4, 43, 3, 0, 0, 42, 0, 3, 3, 4, 43, 0]

def sumdigits(num):
    digits = str(num)
    sum = 0
    for dgt in digits:
        # print dgt,
        if dgt.isdigit():
            sum += int(dgt)
    return sum

def digitalroot(num, sumdigits = sumdigits):
    while num > 9:
        num = sumdigits(num)
    return num

# The digital roots of b_0, b_1, b_3 and b_9 each repeat a cycle of values:
# b_0  [0, 0, ...]
# b_1  [1, 2, 4, 8, 7, 5, 1, 2, 4, 8, 7, 5, ...]
# b_3  [3, 6, 3, 6, ...]
# b_9  [9, 9, ...]
# The digital roots of all other b_s sequences repeat one of the above cycles starting with the digital root of s ?

def makeb_s(s, numterms = 100, maxnum = None, sumdigits = sumdigits):
    b = [s]
    i = 1
    while i < numterms and (maxnum == None or s < maxnum):
        s += sumdigits(s)
        b.append(s)
        i += 1
    return b

def makeA230299(maxs, maxnum, maxterms = 1000000, makeb_s = makeb_s):
    # make a set with all of the values in b_0, b_1, b_3 and b_9
    b0139vals = set([0])
    b1 = makeb_s(1, maxterms, maxnum)
    b3 = makeb_s(3, maxterms, maxnum)
    b9 = makeb_s(9, maxterms, maxnum)
    b0139vals = b0139vals.union(b1)
    b0139vals = b0139vals.union(b3)
    b0139vals = b0139vals.union(b9)
    # return b0139vals
    
    # find a(s) for each s up to maxs
    a = [0,0]
    for s in xrange(2, maxs+1):
        b_s = makeb_s(s, maxterms, maxnum)
        foundmatch = False
        for i in xrange(len(b_s)):
            if b_s[i] in b0139vals:
                foundmatch = True
                a.append(i)
                break
        if not foundmatch:
            # Note: any -1 values are tentative since we are only checking a finite range of each sequence
            a.append(-1)
    return a
