# A constant that generates primes
# see https://youtube.com/watch?v=_gCKX6VMvmU

def calcpk(primes):
  pk = 0
  pprod = 1
  for p in primes:
    pk += (p-1.0)/pprod
    pprod *= p
  return pk

pl = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

pk = calcpk(pl)

# pk = 2.9200509773161341
pn = int(pk)
print pn

for i in range(30):
  pk = pn * (pk-pn+1)
  pn = int(pk)
  print pn

