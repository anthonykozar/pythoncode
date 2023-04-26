# Binary operations represented by "multiplication" tables

# ReadOpTable() parses a multiline table of symbols representing a
# binary operation where the values in the table are the result of
# op(row,col).  The table is assumed to have column and row headings.
def ReadOpTable(tablestr):
    lines = tablestr.splitlines()
    havesymbollist = False
    symbollist = []
    opmap = dict()
    for row in lines:
        symbols = ReadRow(row)
        if len(symbols) > 0:
            # Assume that the first nonempty row is a list a column headings
            # (one per symbol in set).
            if not havesymbollist:
                symbollist = symbols
                havesymbollist = True
            else:
                # Assume that the first symbol in each subsequent nonempty row
                # is the row heading (the left symbol in the operation x*y).
                rowkey = symbols[0]
                opvalues = symbols[1:]
                # require that each row have a complete list of operation values
                if len(opvalues) != len(symbollist):
                    raise ValueError, "Table row has too few values: " + row
                # map each symbol in symbollist to a value in opvalues
                rowmap = dict(zip(symbollist,opvalues))
                # add the row mapping to the operation mapping
                opmap[rowkey] = rowmap
    return opmap

# ReadRow() parses a list of symbols from a string.  Symbols are
# any number of consecutive alphanumeric characters.  All other
# characters are treated as part of a separator (any number of such
# characters delimiting two symbols). 
def ReadRow(rowstr):
    symbols = []
    cursymbol = ""
    it = iter(rowstr)
    try:
        c = it.next()
        while True:
            if c.isalnum():
                cursymbol += c
                c = it.next()
            else:
                if cursymbol != "":
                    # have a complete symbol
                    symbols.append(cursymbol)
                    cursymbol = ""
                # find the beginning of the next symbol
                while not c.isalnum():
                    c = it.next()
    except StopIteration:
        if cursymbol != "":
            # have a complete symbol
            symbols.append(cursymbol)

    return symbols

# ReorderTable() prints an operation's table with the columns and
# rows in arbitrary order.  Rows are printed in the same order as
# the columns if no row order is given.  colorder and roworder can
# be subsets of the full set of symbols for op.
def ReorderTable(op, colorder, roworder = None):
    # print column headings
    colwidth = max(map(len, colorder)) + 1
    line = ' '*colwidth + '| '
    for sym in colorder:
        line += sym.ljust(colwidth)
    print line

    # print horizontal divider
    linewidth = len(line)
    print '-' * linewidth

    # print operation rows
    if roworder == None:  roworder = colorder
    for row in roworder:
        line = row.ljust(colwidth) + '| '
        for col in colorder:
            val = op[row][col]
            line += val.ljust(colwidth)
        print line
    print


# BindSymbols() binds each item in a list of strings (or a
# single string which is treated as a list of chars) as the name of
# a new variable in the global namespace.  The value assigned to
# each name is the same string used for the name.
def BindSymbols(symbollist):
    g = globals()
    for sym in symbollist:
        g[sym] = sym

