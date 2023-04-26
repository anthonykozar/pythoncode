# A new integer sequence

def seq(numterms):
    a=[1,2]
    i=2
    while i<numterms:
        if i%2==0:
            a.append(a[i-1] + a[i-2])
        else:
            a.append(a[i-1] + a[i-3])
        i+=1
    return a
