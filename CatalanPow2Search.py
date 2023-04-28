# See intro to this Mathologer video for 
# questions about powers of 2 in the Catalan numbers
# https://m.youtube.com/watch?v=4AuV93LOPcE

pow2 = [2**i for i in xrange(257)]

def PartialSums(seq):
    psum = seq[0]
    sums = [psum]
    for i in range(1, len(seq)):
        psum += seq[i]
        sums.append(psum)
    return sums

# Catalan numbers are c[4]
numSequences = 10
seqLength = 1024 # tried up to 1000000 for c[2-4] but didn't find any more powers of 2
c0 = [1]*seqLength
c = [c0] + [None]*(numSequences-1)
for i in range(1, numSequences):
    c[i] = [1] + PartialSums(c[i-1])

# find the indices of powers of 2 in all sequences
for j in xrange(2, numSequences):
  for i in xrange(1,len(c[j])):
    if c[j][i] in pow2:
      print j, i, c[j][i]
