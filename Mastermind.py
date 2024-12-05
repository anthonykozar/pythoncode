# Mastermind.py
#
# Search for all remaining solutions for a given Mastermind game state.
#
# Anthony Kozar
# December 2, 2024


class MastermindGuess(object):
    def __init__(self, pegColors, correctPositions, correctColors):
        self.pegColors = pegColors
        self.correctPositions = correctPositions
        self.correctColors = correctColors

class MastermindGame(object):
    def __init__(self, numColors, numPegs, guesses, colorNames = None):
        self.numColors = numColors
        self.numPegs = numPegs
