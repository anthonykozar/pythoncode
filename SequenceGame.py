# SequenceGame.py
#
# A game of inductive logic where the player(s) try to guess the next
# number in a integer sequence that follows some rule/pattern.  If the
# guess is incorrect, the next number is revealed and the player(s) get
# additional chances to guess the following numbers until they are able
# to determine the rule.  Players are given a score based on how many
# numbers in the sequence were revealed to them before they solved the
# rule (lower numbers are better).  Additional rounds with new
# sequences/rules are played as desired and the scores from each round
# are summed together.  The game can be played competitively or
# cooperatively with a fixed group of players or could be implemented
# as a web/mobile game with asynchronous play, leaderboards, and a
# regularly updated list of sequences.

# The in-person version would need a moderator for each round who chooses
# the sequence/rule and reveals successive numbers to the other players.
# For the purposes of playing with a computer or web-based moderator
# where it is not possible for the moderator to interpret verbal
# statements of the rule, a player is considered to have solved a
# sequence if they can guess the next five numbers in a single turn.

# This Python program is a simple, interactive implementation of the
# sequence game for a single player.

import random

# Returns the player's score or False if they cannot solve the sequence.
def PlaySequence(seq, initiallength):
    print("Here is a new sequence for you to solve:")
    lenrevealed = initiallength
    solved = False
    while not solved:
        print("")
        print(seq[0:lenrevealed])
        line = raw_input("\nWhat is your guess for the next 1-5 numbers? ")
        # These lines are needed if using input() instead of raw_input():
        # if type(guess) == int:
        #    guess = [guess]
        try:
            guess = map(int, line.split(','))
        except ValueError:
            print("You must enter a comma-separated list of integers.")
            continue

        # check if the guess is correct
        seqmatch = seq[lenrevealed:(lenrevealed + len(guess))]
        # FIXME? if lenrevealed + len(guess) > len(seq) then this check is always False
        if guess == seqmatch:
            print("That's correct!")
            if len(guess) >= 5:
                print("Congratulations, you win!")
                solved = True
                score = lenrevealed - initiallength
                print("Your score is %d." % score)
                return score
            else:
                lenrevealed += len(guess)
        else:
            print("Sorry, that is incorrect.")
            nextnum = seq[lenrevealed]
            print("The next number in the sequence is %d." % nextnum)
            lenrevealed += 1
    
        if lenrevealed >= len(seq) - 5:
            print("\nSorry, you failed to guess the next 5 numbers before I ran out of numbers to reveal.")
            print("The complete sequence that I have is:")
            print("")
            print(seq)
            break

    return False

### These functions define various random sequences
def MakeArithmeticSequence(length = 100):
    start = int(random.triangular(-100.0, 100.0))
    stepsign = random.choice([1, -1])
    rand = random.random()
    # favor smaller intervals
    step = stepsign * int(101.0*rand*rand)
    end = start + length*step
    return range(start, end, step)

def fibrecurrence(a1, a2, terms = 20):
    out=[a1,a2]
    for i in xrange(2,terms):
        out.append(out[i-2]+ out[i-1])
    return out

PowersOf2 = [2**n for n in range(7)]

PlaySequence(MakeArithmeticSequence(), 3)
