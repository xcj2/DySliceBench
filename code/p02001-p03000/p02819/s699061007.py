def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret

def isPrime(N):
    if N <= 1: return False
    return sum(primeFactor(N).values()) == 1

def findPrime(N):
    if N < 0: return -1
    i = N
    while True:
        if isPrime(i):
            return i
        i += 1

N = int(input())
print(findPrime(N))