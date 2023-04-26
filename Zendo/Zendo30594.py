def pfactorlist(num):
    # primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    factors = []
    for p in range(2,num+1):
        if num < 2:
            break
        while num % p == 0:
            factors.append(p)
            num = num / p
    return factors

def isprime(num):
    return (num > 1) and (len(pfactorlist(num)) == 1)

# from <https://stackoverflow.com/questions/16628088/euclidean-algorithm-gcd-with-multiple-numbers>
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def GCDofList(nums):
    return reduce(GCD, nums)

def HTBN(koan):
    return (GCDofList(koan) == 1) and isprime(sum(koan))


Zendo30594Has = [
[1, 1, 1], 
[1, 1, 3], 
[1, 1], 
[1, 2, 2, 2, 2, 2, 2], 
[1, 2], 
[1, 6], 
[1, 10], 
[1, 16], 
[1, 1600], 
[1, 47292], 
[1,1,1,1,3], 
[1,2,4], 
[2, 2, 3], 
[2, 2, 7], 
[2, 3], 
[2, 5], 
[4, 7], 
[4, 9], 
[6, 11], 
[6, 13], 
[8, 15], 
[10, 19], 
[10, 21], 
[12, 25], 
[22, 45], 
[32, 65], 
[34, 67], 
[100, 101, 200], 
[100, 199, 200], 
[100, 501], 
[3141, 5926], 
[4444, 8887], 
]

Zendo30594HasNot = [
[1], 
[1, 1, 1, 1, 5], 
[1, 1, 1, 1], 
[1, 1, 1, 3], 
[1, 1, 1, 4], 
[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10], 
[1, 1, 2], 
[1, 2, 2, 2, 2, 2, 2, 2, 2], 
[1, 2, 2, 2, 2], 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23], 
[1, 2, 3], 
[1, 2, 4, 8], 
[1, 3], 
[1, 5], 
[1, 7], 
[1, 512], 
[1, 1024], 
[2, 2, 2, 2, 2, 2, 3], 
[2, 2, 2, 2, 7], 
[2, 2, 2, 3], 
[2, 2, 4], 
[2, 2, 5], 
[2, 2, 6], 
[2, 2, 7, 7, 7], 
[2, 2, 2011], 
[2, 2], 
[2, 3, 4, 5], 
[2, 4, 8], 
[2, 7], 
[3, 3, 3, 3, 3], 
[3, 3, 3], 
[3, 3, 4], 
[3, 9], 
[4, 4, 6, 10], 
[4, 7, 9], 
[4, 11], 
[6, 9], 
[7, 7], 
[7, 9], 
[7, 10, 22, 22], 
[8, 9, 10, 11, 524288], 
[8, 17], 
[12, 23], 
[16, 33], 
[18, 37], 
[20], 
[22, 43], 
[26, 51], 
[28, 57], 
[30, 61], 
[32, 63], 
[100, 101, 199], 
[100, 101, 201], 
[100, 101], 
[100, 103, 200], 
[100, 151, 200], 
[100, 510], 
[500, 999, 1000], 
[666, 667, 669], 
[763, 1729, 99999, 100000, 100001], 
[1024], 
[1234, 2469], 
[2718, 3141],
[3333, 6665], 
[4444, 8889], 
[32768, 65535, 65536], 
]

### Runs this code when loaded

# check BN of each list of koans
print "\nPredicted nature of the HAS koans:\n"
print map(HTBN, Zendo30594Has)
print "\n\nPredicted nature of the HAS NOT koans:\n"
print map(HTBN, Zendo30594HasNot)

# find exceptions among the HAS NOTs
print "\n\nHAS NOT koans that contradict theory:\n"
print filter(HTBN, Zendo30594HasNot)
