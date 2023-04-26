def nextvalue(prevvalue):
    # print "Called nextvalue with %s" % prevvalue
    # print len(prevvalue)
    curch = prevvalue[0]
    count = 0
    result = ""
    for ch in prevvalue:
        if ch == curch:
            count = count + 1
        else:
            result = result + str(count) + str(curch)
            curch = ch
            count = 1
    # add the final character sequence
    result = result + str(count) + str(curch)
    # print "result = %s" % result
    return result

val = "1"
for x in xrange(10):
    print val
    val = nextvalue(val)
