def digitmanip(n,length=4):
    digits=list(str(n))
    while len(digits) < length:
        digits.append('0')
    digits.sort()
    asc=int("".join(digits))
    digits.reverse()
    desc=int("".join(digits))
    return desc-asc

last=0
curnum=1729
while last != curnum:
    last=curnum
    curnum= digitmanip(curnum)
    print curnum

for n in xrange(1000,10000):
    last=0
    curnum=n
    while last != curnum:
        last=curnum
        curnum= digitmanip(curnum)
    if curnum != 6174:
        print n

for n in xrange(100,1000):
    last=0
    curnum=n
    while last != curnum:
        last=curnum
        curnum= digitmanip(curnum,3)
    if curnum != 495:
        print n

previous=[]
curnum=91
while not curnum in previous:
    previous.append(curnum)
    curnum= digitmanip(curnum,2)
    print curnum
