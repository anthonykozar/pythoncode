# Generative music experiments
# inspired by my laundry machine sims.

# Anthony Kozar
# August 10, 2013

import heapq
import random
import time

##############################################################
# First experiment
#
# This system will have two groups of notes where each note
# has its own repeat period (classic "Eno ambient") but the
# notes in the second group ("followers") will always be
# paired with a note from the first group ("leaders") so that
# performance of the followers is delayed until a leader is
# available for them to follow.  Whenever a leader is ready
# to play, the queue of followers is checked to see if any
# are ready to play.  If so, the follower that has been
# waiting the longest is chosen; if not, the leader plays
# without a follower.
#
# The follower notes will have significantly longer periods
# than the leaders and if there are few of them, then the
# leaders may often play by themselves.

LEADER_PITCHES   = [ 'g3', 'bf3', 'd4', 'f4', 'e4', 'a3' ]
FOLLOWER_PITCHES = [ 'a3', 'd4', 'd3', 'g4' ]

PITCHNAMES_TO_OCTPCH = { 'd3':7.02, 'g3':7.07, 'a3':7.09, 'bf3':7.10,
                         'd4':8.02, 'e4':8.04, 'f4':8.05, 'g4':8.07 }

# this global saves the random state
lastseed = None

# Going to try selecting random periods that increase 
# with the order of pitches in the above arrays. First play
# time also will increase in the order above.
#
# This method does NOT work well as it often gives lots of
# values near the maximum:
#       while starttime <= laststart:
#           starttime = random.uniform(minstart, maxstart)
#
# Better to generate a list of random values then sort them.
def GetSortedRandomList(numvalues, minval, maxval):
    values = [random.uniform(minval, maxval) for i in range(numvalues)]
    values.sort()
    return values
                      
# Notes are lists of 3 values: [nextplay, pitch, period]
# These constants are their indices:
NEXTPLAY = 0
PITCH = 1
PERIOD = 2

# Each note group is a minheap array which will be sorted
# by the first member of the tuple (nextplay)
def MakeNoteHeap(pitches, minstart, maxstart, minperiod, maxperiod, firstZero):
    # should the first note should start at time zero?
    if firstZero:
        starttimes = [0.0] + GetSortedRandomList(len(pitches)-1, minstart, maxstart)
    else:   starttimes = GetSortedRandomList(len(pitches), minstart, maxstart)
    periods = GetSortedRandomList(len(pitches), minperiod, maxperiod)
    notes = map(list, zip(starttimes, pitches, periods))
    # make the note array a minheap so that we can easily get next to play
    heapq.heapify(notes)
    return notes

def MakeAllNotes():
    global lastseed
    # set and print random seed so that we can repeat this generation
    random.seed()
    lastseed = random.getstate()

    # make the leaders
    leaders = MakeNoteHeap(LEADER_PITCHES, 0.0, 20.0, 4.0, 10.0, True)
    # make the followers
    followers = MakeNoteHeap(FOLLOWER_PITCHES, 20.0, 32.0, 16.0, 25.0, False)

    return leaders, followers

def PrintyPrintNotes(leaders, followers):
    print "; Starttime  Pitch  Period"
    print "; --------------------------"
    print "; LEADERS:"
    for note in leaders:
        print "; %8.4f   %4s   %7.4f" % tuple(note)
    print
    print "; FOLLOWERS:"
    for note in followers:
        print "; %8.4f   %4s   %7.4f" % tuple(note)
    print

# Note events are triples: (time, duration, pitch)
EVTIME = 0
EVDUR = 1
EVPITCH = 2

# notestart can be a time value or None to use the note's
# NEXTPLAY value.
def AddNewNoteToSeq(seq, notequeue, notedur, notestart = None):
    # dequeue the first note, create an event, and add to seq
    curNote = heapq.heappop(notequeue)
    if notestart == None:
        notestart = curNote[NEXTPLAY]
    newEvent = (notestart, notedur, curNote[PITCH])
    seq.append(newEvent)
    # update the note's next play time and requeue it
    curNote[NEXTPLAY] = notestart + curNote[PERIOD]
    heapq.heappush(notequeue, curNote)
    return newEvent

# Event sequences are just lists of note events
def GenerateNoteEventSeq(notedur, totaldur, leaders, followers):
    seqdur = 0.0
    eventSeq = []
    while seqdur < totaldur:
        # if the first leader is not beyond the seqenece end,
        if leaders[0][NEXTPLAY] <= totaldur:
            # add it to the sequence
            leaderEvent = AddNewNoteToSeq(eventSeq, leaders, notedur)
            # and if first follower is ready to play,
            leaderEndTime = leaderEvent[EVTIME] + leaderEvent[EVDUR]
            if followers[0][NEXTPLAY] <= leaderEndTime:
                # add it to the sequence
                followerEvent = AddNewNoteToSeq(eventSeq, followers, notedur, leaderEndTime)
                followerEndTime = followerEvent[EVTIME] + followerEvent[EVDUR]
            else:   followerEndTime = 0.0
            # update the sequence duration
            seqdur = max(seqdur, leaderEndTime, followerEndTime)
        else:
            # no notes left to play, so advance seqdur to end
            seqdur = totaldur
    return eventSeq

def PrintyPrintEvents(seq):
    print "Time        Duration    Pitch"
    print "------------------------------"
    for event in seq:
        print "%9.4f   %9.4f   %4s" % event
    print


def MakeCsoundScore(seq):
    print "; Score generated by MusicForLaundromats1.py"
    print time.strftime('; %b %d %Y %H:%M:%S %Z')
    print
    print "; ins   time      duration  pitch"
    print "; --------------------------------------"
    for event in seq:
        print "i1      %-9.4f %-9.4f %4.2f" % (event[EVTIME], event[EVDUR],
                                               PITCHNAMES_TO_OCTPCH[event[EVPITCH]])
    print "e"


# The 'splat' operator (*) unpacks the 'notes' tuple from MakeAllNotes()
# as individual arguments to PrintyPrintNotes() and GenerateNoteEventSeq().
# AWESOME!  ^_^
notes = MakeAllNotes()
PrintyPrintNotes(*notes)
# Splat can only be used at the end of the arg list; this doesn't work:
#        GenerateNoteEventSeq(*notes, 1.0, 300.0)
events = GenerateNoteEventSeq(1.0, 300.0, *notes)
events.sort()
MakeCsoundScore(events)
