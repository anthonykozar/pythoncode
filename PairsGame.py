import random

class PairsGame(object):
    
    def __init__(self, numplayers):
        self.numplayers = numplayers
    
    def initdeck(self):
        import random # work around Pyonic bug
        self.deck = [1]
        for i in xrange(2,11):
            self.deck += [i]*i
        random.shuffle(self.deck)
    
    def initplayers(self):
        self.players = []
        for i in xrange(self.numplayers):
            self.players.append(list())
    
    def initialdeal(self, removecards = 0):
        for i in xrange(removecards):
            self.deck.pop()
        for p in self.players:
            p.append(self.deck.pop())
    
    def start(self):
        self.initdeck()
        self.initplayers()
        self.initialdeal()
        self.whoseturn = 0
        print self.players
        print self.deck
    
    def nextturn(self, printinfo = True):
        p = self.players[self.whoseturn]
        if printinfo:
            print "Player", self.whoseturn
            print "Hand:", p
            #print "Odds:",
            print
        
        p.append(self.deck.pop())
        self.whoseturn = (self.whoseturn+1) % self.numplayers
        
