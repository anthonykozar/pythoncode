def digitset(n):
    s=str(n)
    ds=""
    for d in xrange(10):
        if str(d) in s:
            ds += str(d)
    return ds

