# Partial implementation of the Noisett programming language
# http://noisett.lang.free.fr/
# https://esolangs.org/wiki/Noisett
import re

def NewNut(name, code = None, messages = None, links = None):
    nut = dict()
    nut['_name'] = name
    if type(messages) == list:
        nut['MAIL'] = messages
    else:
        nut['MAIL'] = list()
    if type(links) == list:
        nut['LINK'] = links
    else:
        nut['LINK'] = list()
    if type(code) == list:
        nut['PROG'] = code
    else:
        nut['PROG'] = list()

    nut['COPY'] = list()
    return nut

# Test nut
test = NewNut("Test",
              [['My name is *', '>', 'Hello $1!'],
               ['* * * *', '<', '$4 $3 $1 $2']
              ],
              ["My name is Anthony"]
             )

def PrintNut(nut):
    print "%s.nut" % nut['_name']
    for section in nut.keys():
        if section != '_name':
            print '  [%s]' % section
            for line in nut[section]:
                print '   ', line
    print

# Global dictionary of nuts; keys are the nut names
NUTS = dict()

# NUTS = {'Test': {'PROG': [['My name is *', '>', 'Hello $1!'], ['* * * *', '<', '$4 $3 $1 $2']], 'MAIL': [], 'COPY': [], 'LINK': [['=', '', 'Starter', '=']], '_name': 'Test'}, 'Starter': {'PROG': [['*', '>', 'My name is Starter']], 'MAIL': ['GO!'], 'COPY': [], 'LINK': [['=', '', 'Test', '=']], '_name': 'Starter'}}

def AddNut(nut, nuts = NUTS):
    nuts[nut['_name']] = nut

def PrintProgram(nuts = NUTS):
    for nut in nuts.values():
        PrintNut(nut)

# Returns None if nut does not exist and create option is False
def GetNutByName(name, createIfNonexistent = False):
    if NUTS.has_key(name):
        return NUTS[name]
    else:
        if createIfNonexistent:
            # create a new nut named name
            nut = NewNut(name)
            NUTS[name] = nut
            return nut
    return None

def SendMessage(message, sender, target, trace = False):
    target['MAIL'].append(message)
    if trace: print sender['_name'], '>', target['_name'], ':', message

# A LINK line is a list of 4 strings that are the names of
# nuts.  A nut can use '=' to reference itself.
#   [Sender, Vector, Target, Table]
#
# "The LINK section of a Nut contains every link involving
# this Nut." (Noisett spec)  So, SendMessageToLinks() should
# only send messages along links when the Sender field of the
# link matches the current nut (or '=').
#
# Messages sent to links SHOULD be sent thru the Vector nut
# to the Target nut instead of directly to the Target, but
# this is not implemented yet.
#
# Returns a count of the number of links messaged.
def SendMessageToLinks(message, sender, trace = False):
    sentcount = 0
    for link in sender['LINK']:
        if link[0] == sender['_name'] or link[0] == '=':
            if link[2] == '=':
                targetname = sender['_name']
            else:
                targetname = link[2]
            target = GetNutByName(link[2], True)
            SendMessage(message, sender, target, trace)
            sentcount += 1
    return sentcount

def ClearMessages(nut):
    nut['MAIL'] = []

# A PROG line can currently only be
#   [pattern, '>', outmessage]
#   [pattern, '<', outmessage]
# where pattern is a string that may contain * as a wildcard
# and outmessage is a string that may contain $1, $2, etc.

def RunCodeLine(nut, code, message, trace = False):
    # convert pattern to a regular expression
    pattern = re.escape(code[0]) # escape all non-alphanumeric chars
    pattern = '^' + pattern.replace('\*', '(.*)') + '$' # convert *'s and match entire message
    pattern = re.compile(pattern)
    matchobj = pattern.match(message)
    if matchobj:
        # replace $n with text captured by wildcards
        # (in reverse order so $1 doesn't match $11, etc.)
        outmsg = code[2]
        n = matchobj.lastindex
        while n > 0:
            outmsg = outmsg.replace('$%d' % n, matchobj.group(n))
            n = n - 1
        if code[1] == '>':
            # send message to links
            numRecipients = SendMessageToLinks(outmsg, nut, trace)
            if trace and numRecipients == 0:
                print nut['_name'], '> [no links] :', outmsg
        elif code[1] == '<':
            # send message to self
            SendMessage(outmsg, nut, nut)
            if trace: print nut['_name'], '<', outmsg

# Returns True if a message was processed, otherwise False.
def ProcessNextMessage(nut, trace = False):
    if len(nut['MAIL']) > 0:
        # remove first message from MAIL 
        message = nut['MAIL'][0]
        nut['MAIL'] = nut['MAIL'][1:]
        if nut['_name'] == 'stdout':
            # special nut that just prints messages to std output
            print message
        else:
            # check if message matches each code line
            for line in nut['PROG']:
                RunCodeLine(nut, line, message, trace)
        return True
    else:
        return False

# Process messages of a single nut in a loop
def RunLoop(nut, showStates = True):
    if showStates: PrintNut(nut)
    while (ProcessNextMessage(nut)):
        print
        if showStates: PrintNut(nut)

# Process messages of all nuts in round robin order
def RunProgram(nuts = NUTS, trace = False):
    runMore = True
    while (runMore):
        runMore = False
        for nut in nuts.values():
            didMessage = ProcessNextMessage(nut, trace)
            runMore = runMore or didMessage


### Examples ###
# RunProgram()

