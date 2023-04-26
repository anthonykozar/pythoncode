# SDG Zendo game #30289

Zendo30289Has = ["3330", "3331", "3332", "3333", "3334", "3338", "3339", "3535", "3538",
                 "3636", "3835", "3838", "4548", "4845", "4845", "5445", "544f", "7875"]

Zendo30289HasNot = ["0000", "0001", "1000", "206d", "2528", "279a", "3223", "332f",
                    "333a", "333f", 
                    "3344", "3345", "4321", "4333", "4444", "4545", "4664", "4745", "4844",
                    "4846", "4f54", "5448", "544c", "544e", "5484", "5558", "655f", "6666",
                    "7845", "9994", "e333", "ffff"]

def base16to10(hexnumstr):
    return int(str(hexnumstr), 16)

def baseconvert(val,base):
    if base > 26:
        return "Error: base > 26"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basestr = ""
    while val > 0:
        rmndr = val % base
        val = val // base
        basestr = digits[rmndr] + basestr
    return basestr

def PrintBase16andBase10(hexnumstr):
    print hexnumstr, '    ', base16to10(hexnumstr)

def PrintBase16_10_8_2(hexnumstr):
    base10 = base16to10(hexnumstr)
    print hexnumstr, '\t', base10, '\t', baseconvert(base10,8), '\t', baseconvert(base10,2)

def PrintNumAndFactors(num):
    print num, '    ',
    pfactor(num)
    print

def MapHas_HasNot(fn, has = Zendo30289Has, hasnot = Zendo30289HasNot):
    print 'HAS'
    print '-------'
    map(fn, has)
    print ''
    print 'HAS NOT'
    print '-------'
    map(fn, hasnot)

# execute when module is loaded
MapHas_HasNot(PrintBase16_10_8_2)
