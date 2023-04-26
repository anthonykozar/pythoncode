def tripledigit(n):
  s = str(n)
  for c in range(2, len(s)):
    if s[c] == s[c-2] and s[c] == s[c-1]:
      return True
  return False


for n in xrange(10,1000):
  if tripledigit(n*n):
    print n*n
