# A problem from this YouTube video:
#
# 6 Mind-Bending Puzzles That Test Your Logic Skills
# https://m.youtube.com/watch?v=oZC5QIaelzo

# Anthony Kozar
# Sept. 15, 2025

# The essence of the problem is to partition
# the set S = [1, 2, ... 49] into 7 parts,  
# each with seven numbers and equal sums.

# First, note that the sum of S is 49*50/2,
# so each part should sum to 175. Also, there
# are 24 pairs that sum to 50 -- (1,49), (2,48), etc. -- with 25 left over.
# We can get close to a solution by putting the numbers 22 to 28 in different parts
# and then distributing three pairs to each part.

shares = [[n] for n in xrange(22,29)]
for n in xrange(1,22):
    son = (n%7)-1
    shares[son].append(n)
    shares[son].append(50-n)

[sum(sh) for sh in shares]

# This gives the sums 
#   [172, 173, 174, 175, 176, 177, 178]
# Now we could try swapping numbers between parts to change their sums by the amounts 
#   [+3, +2, +1, 0, -1, -2, -3].
# I don't think this is possible given the way that the 50-sum pairs were distributed above. 
