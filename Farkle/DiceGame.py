import operator
import re

def sortletters(koan):
    return reduce(operator.concat, sorted(koan))

# print combinations as strings of dice values
# (probably not useful if facesPerDie > 9)
def PrintAllDiceCombinations(numdice, facesPerDie):
    if numdice < 1 or facesPerDie < 2: return
    finished = False
    roll = list('1'*numdice)
    dice = xrange(numdice-1, -1, -1)
    while (not finished):
        print reduce(operator.concat, roll)
        for die in dice:
            if (int(roll[die]) < facesPerDie):
                roll[die] = str(int(roll[die]) + 1)
                # reset dice with higher indices to new roll[die] value
                for i in range(die+1, numdice):
                    roll[i] = roll[die]
                break
            # if all of the dice equal facesPerDie, we are done
            if (die == 0): finished = True

# generate combinations as integer arrays
def GenerateAllDiceCombinations(numdice, facesPerDie):
    if numdice < 1 or facesPerDie < 2: return list()
    finished = False
    combos = list()
    roll = map(int, list('1'*numdice))
    dice = xrange(numdice-1, -1, -1)
    while (not finished):
        combos.append(list(roll)) # append a copy of roll
        for die in dice:
            if (roll[die] < facesPerDie):
                roll[die] = roll[die] + 1
                # reset dice with higher indices to new roll[die] value
                for i in range(die+1, numdice):
                    roll[i] = roll[die]
                break
            # if all of the dice equal facesPerDie, we are done
            if (die == 0): finished = True
    return combos

# RollToString() takes an integer array and returns a string
# that is the concatenation of the array's values.
def RollToString(roll):
    return reduce(operator.concat, map(str, roll))

# count how often each combination occurs among all dice permutations
def FindDiceComboFrequencies(numdice, facesPerDie):
    if numdice < 1 or facesPerDie < 2: return dict()
    finished = False
    freqs = dict() # map of rolls (strings) -> counts (int)
    roll = map(int, list('1'*numdice))
    dice = xrange(numdice-1, -1, -1)
    while (not finished):
        # make a sorted copy of roll
        combo = list(roll)
        combo.sort()
        # increment the count for combo
        key = reduce(operator.concat, map(str, combo))
        if freqs.has_key(key):
            freqs[key] = freqs[key] + 1
        else:
            freqs[key] = 1
        # print roll, combo, freqs[key]
        # generate the next roll (permutation)
        for die in dice:
            if (roll[die] < facesPerDie):
                roll[die] = roll[die] + 1
                # reset dice with higher indices to 1
                for i in range(die+1, numdice):
                    roll[i] = 1
                break
            # if all of the dice equal facesPerDie, we are done
            if (die == 0): finished = True
    return freqs


rolls6d6 = GenerateAllDiceCombinations(6,6)
rolls5d6 = GenerateAllDiceCombinations(5,6)
rolls4d6 = GenerateAllDiceCombinations(4,6)
rolls3d6 = GenerateAllDiceCombinations(3,6)
rolls2d6 = GenerateAllDiceCombinations(2,6)
rolls1d6 = GenerateAllDiceCombinations(1,6)

combosForNd6 = [[],rolls1d6,rolls2d6,rolls3d6,rolls4d6,rolls5d6,rolls6d6]
numCombosForNd6 = map(len, combosForNd6)

freqs6d6 = FindDiceComboFrequencies(6,6)
freqs5d6 = FindDiceComboFrequencies(5,6)
freqs4d6 = FindDiceComboFrequencies(4,6)
freqs3d6 = FindDiceComboFrequencies(3,6)
freqs2d6 = FindDiceComboFrequencies(2,6)
freqs1d6 = FindDiceComboFrequencies(1,6)

freqsForNd6 = [[],freqs1d6,freqs2d6,freqs3d6,freqs4d6,freqs5d6,freqs6d6]


def NumCombosByNumDice(facesPerDie, maxNumDice):
    return [len(GenerateAllDiceCombinations(i, facesPerDie)) for i in range(maxNumDice+1)]

def FindMatchingCombos(frequencyMap, pattern, echo = True):
    pat = re.compile(pattern)
    matches = dict()
    for key in frequencyMap.keys():
        if pat.search(key):
            matches[key] = frequencyMap[key]
            if echo:
                print key, frequencyMap[key]
    return matches

def FindMatchingCombosMultiplePatterns(frequencyMap, patterns, echo = True):
    pats = map(re.compile, patterns)
    matches = dict()
    for key in frequencyMap.keys():
        for pat in pats:
            if pat.search(key):
                matches[key] = frequencyMap[key]
                if echo:
                    print key, frequencyMap[key]
                break
    return matches

# Some regular expression patterns to match scoring combos
p111    = r'(?<!1)1{3}(?!1)'  # matches exactly three 1's
p1111   = r'(?<!1)1{4}(?!1)'  # matches exactly four 1's
p11111  = r'(?<!1)1{5}(?!1)'  # matches exactly five 1's
p111111 = r'(?<!1)1{6}(?!1)'  # matches exactly six 1's

p222    = r'(?<!2)2{3}(?!2)'  # matches exactly three 2's
p2222   = r'(?<!2)2{4}(?!2)'  # matches exactly four 2's
p22222  = r'(?<!2)2{5}(?!2)'  # matches exactly five 2's
p222222 = r'(?<!2)2{6}(?!2)'  # matches exactly six 2's

p333    = r'(?<!3)3{3}(?!3)'  # matches exactly three 3's
p3333   = r'(?<!3)3{4}(?!3)'  # matches exactly four 3's
p33333  = r'(?<!3)3{5}(?!3)'  # matches exactly five 3's
p333333 = r'(?<!3)3{6}(?!3)'  # matches exactly six 3's

p444    = r'(?<!4)4{3}(?!4)'  # matches exactly three 4's
p4444   = r'(?<!4)4{4}(?!4)'  # matches exactly four 4's
p44444  = r'(?<!4)4{5}(?!4)'  # matches exactly five 4's
p444444 = r'(?<!4)4{6}(?!4)'  # matches exactly six 4's

p555    = r'(?<!5)5{3}(?!5)'  # matches exactly three 5's
p5555   = r'(?<!5)5{4}(?!5)'  # matches exactly four 5's
p55555  = r'(?<!5)5{5}(?!5)'  # matches exactly five 5's
p555555 = r'(?<!5)5{6}(?!5)'  # matches exactly six 5's

p666    = r'(?<!6)6{3}(?!6)'  # matches exactly three 6's
p6666   = r'(?<!6)6{4}(?!6)'  # matches exactly four 6's
p66666  = r'(?<!6)6{5}(?!6)'  # matches exactly five 6's
p666666 = r'(?<!6)6{6}(?!6)'  # matches exactly six 6's

pThreePairs = r'^(11)?(22)?(33)?(44)?(55)?(66)?$' # matches any three distinct pairs
pTwoTriples = r'^(111)?(222)?(333)?(444)?(555)?(666)?$' # matches any two distinct triples (three of a kind)
pStraight = '123456'

pSixNothings = r'^2{1,2}3{1,2}4{1,2}6{1,2}$' # "six sweet nothings"; matches all 6d6 rolls with no scoring combos
pNoPoints = r'^2{0,2}3{0,2}4{0,2}6{0,2}$'    # matches non-scoring combos with less than 6 dice

def TotalFreqMatchingCombos(frequencyMap, pattern):
    return sum(FindMatchingCombos(frequencyMap, pattern, False).values())


# Ex. FindMatchingCombos(freqs6d6, p222)
# Ex. TotalFreqMatchingCombos(freqs6d6, p222)

# arrays of similar patterns
paAny3ofaKind = [p111, p222, p333, p444, p555, p666]
paAny4ofaKind = [p1111, p2222, p3333, p4444, p5555, p6666]
paAny5ofaKind = [p11111, p22222, p33333, p44444, p55555, p66666]
paAny6ofaKind = [p111111, p222222, p333333, p444444, p555555, p666666]

def TestNofaKindFreqs():
    totalwithdups = lambda pa : sum(map(lambda p : TotalFreqMatchingCombos(freqs6d6,p), pa))
    totalwithoutdups = lambda pa : sum(FindMatchingCombosMultiplePatterns(freqs6d6, pa, False).values())
    print "Three of a kind: ", totalwithdups(paAny3ofaKind), totalwithoutdups(paAny3ofaKind)
    print "Four of a kind: ", totalwithdups(paAny4ofaKind), totalwithoutdups(paAny4ofaKind)
    print "Five of a kind: ", totalwithdups(paAny5ofaKind), totalwithoutdups(paAny5ofaKind)
    print "Six of a kind: ", totalwithdups(paAny6ofaKind), totalwithoutdups(paAny6ofaKind)

def ChanceOfNoPoints(numdice):    
    if numdice == 6:
        return TotalFreqMatchingCombos(freqs6d6, pSixNothings) / float(6**6)
    elif (1 <= numdice <= 5):
        return TotalFreqMatchingCombos(freqsForNd6[numdice], pNoPoints) / float(6**numdice)
    else:
        print "ChanceOfNoPoints: numdice outside range [1,6]"
        return 0.0

# map(ChanceOfNoPoints, range(1,7))

def TableOfNoPoints():
    print "Chances of getting no points:\n"
    print "num dice   percent"
    print "------------------"
    for n in range(1,7):
        print "%s          %4.2f%%" % (n, ChanceOfNoPoints(n) * 100.0)

def FreqOfNoPoints(numdice):    
    if numdice == 6:
        return (TotalFreqMatchingCombos(freqs6d6, pSixNothings), 6**6)
    elif (1 <= numdice <= 5):
        return (TotalFreqMatchingCombos(freqsForNd6[numdice], pNoPoints), 6**numdice)
    else:
        print "ChanceOfNoPoints: numdice outside range [1,6]"
        return 0.0

def TableOfSomeVsNoPoints():
    print "Chances of getting:\n"
    print "num dice   odds(Pts) percent(Pts)    odds(None) percent(None)"
    print "-----------------------------------------------------------"
    for n in range(1,7):
        oddsNone = FreqOfNoPoints(n)
        oddsPts = (oddsNone[1] - oddsNone[0], oddsNone[1])
        pcnt = lambda odds : 100.0 * float(odds[0]) / float(odds[1])
        print "%s          %s    %4.2f%%          %s    %4.2f%%" % (n, oddsPts, pcnt(oddsPts), oddsNone, pcnt(oddsNone))

# CountValues() returns histogram-like list containing the number of
# occurences in alist of each value between 0 and maxval.
# Eg. CountValues([1,0,1], 2) => [1, 2, 0]
def CountValues(alist, maxval):
    # initialize a list of length maxval+1 with all zero values
    counts = map(int, list('0'*(maxval+1)))
    for n in alist:
        counts[n] = counts[n] + 1
    return counts

# ScoreRoll() calculates the point total for one or more scoring combos.
# 'roll' can be a string of dice values ('123456'), a list of numerical
# strings (['1', '2', '3']) or a list of integers.
def ScoreRoll(roll):
    # convert roll to an integer list
    if isinstance(roll, list):
        roll = map(int, roll)
    elif isinstance(roll, str):
        roll = map(int, list(roll))

    counts = CountValues(roll)
    
