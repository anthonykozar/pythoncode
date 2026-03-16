suits = "ABCDEFWXYZ"
for card in xrange(60):
    suit6 = suits[(card + card/30) % 6]
    rank6 = card%10 + 1
    suit4 = suits[card%4 + 6]
    rank4 = card%15 + 1
    print card+1, "%d%s" % (rank6, suit6), "%d%s" % (rank4, suit4)

deck6 = []
for card in xrange(60):
    suit6 = suits[(card + card/30) % 6]
    rank6 = card%10 + 1
    deck6.append("%d%s" % (rank6, suit6))
print sorted(deck6)

deck4 = []
for card in xrange(60):
    suit4 = suits[card%4 + 6]
    rank4 = card%15 + 1
    deck4.append("%d%s" % (rank4, suit4))
print sorted(deck4)

# result frequencies for emulating 2d6 with 60 cards
rolls = [(a,b) for a in xrange(1,7) for b in xrange(1,7)]
from collections import defaultdict
counts = defaultdict(int)
for s in map(sum, rolls):
    counts[s] += 1
counts
total = 0
for s in xrange(2,13):
    frq = counts[s]*5.0/3.0
    print s, round(frq), frq
    total += round(frq)
total
