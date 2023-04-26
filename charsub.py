def subst(s, tr):
    out=""
    for c in s:
        out+=tr[c]
    return out

fb={'0':'01','1':'0'}
sq={'1':'1','2':'4','3':'9','4':'16','5':'25','6':'36','7':'49','8':'64','9':'81','0':'0'}

z='5'
while len(z)<40:
    print z
    z=subst(z,sq)

# This produces strings with lengths 
# (n+1) * 2**n or T(0)=1, T(n)=2*T(n-1) + 2^n
# when the start string is '1'
a={'0':'00','1':'1010'}

z='1'
while len(z)<100:
    print z
    z=subst(z,a)

z='1'
while len(z)<100000:
    print len(z), 
    z=subst(z,a)
print
