# From <https://www2.stetson.edu/~efriedma/mathmagic/0211.html>:

# "Evert Stenlund invented and then analyzed a game similar to this. In his game,
# both players start with cards 1 through n, and each turn choose a card of
# theirs. If both cards are the same, they are both discarded. If they are not the
# same, the lower is discarded, unless it is 1 less than the other card, in which
# case the higher card is discarded.
# 
# "For n=1, the game is trivial. For n=2, both players can insure a draw by
# choosing "1". For n=3, this is game is equivalent to "rock-scissors-paper",
# since the outcome of the game is decided by the first turn. For n>3, the game is
# more interesting, including some surprises!"

# March 13, 2019

def StartGame(n):
    p1 = range(1, n+1)
    p2 = range(1, n+1)
    MakeMove(p1, p2, "")

def MakeMove(p1, p2, movestr):
    for p1move in p1:
        for p2move in p2:
            # copy the player's hands
            newp1 = p1[:]
            newp2 = p2[:]
            # add moves to current list 
            newmovestr = movestr + ("%d/%d " % (p1move, p2move))
            # determine result & discard card(s)
            if p1move == p2move:
                newp1.remove(p1move)
                newp2.remove(p2move)
            elif p1move == (p2move+1):
                newp1.remove(p1move)
            elif (p1move+1) == p2move:
                newp2.remove(p2move)
            elif p1move < p2move:
                newp1.remove(p1move)
            elif p1move > p2move:
                newp2.remove(p2move)
            # check end game conditions
            if len(newp1) == 0 and len(newp2) == 0:
                print newmovestr + "Draw"
                continue
            elif len(newp1) == 0:
                print newmovestr + "P2 wins"
                continue
            elif len(newp2) == 0:
                print newmovestr + "P1 wins"
                continue
            # otherwise continue playing
            MakeMove(newp1, newp2, newmovestr)


# StartGame(4)
