def primeFactor(N):
    i = 2
    ret = {}
    n = N
    if n < 0:
        ret[-1] = 1
        n = -n
    if n == 0:
        ret[0] = 1
    while i**2 <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
            ret[i] = k
        i += 1
    if n > 1:
        ret[n] = 1
    return ret

def isPrime(N):
    if N <= 1:
        return False
    return sum(primeFactor(N).values()) == 1

def findPrime(N):
    if N < 0:
        return -1
    i = N
    while True:
        if isPrime(i):
            return i
        i += 1

def divisor(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)
    
N, M = map(int, input().split(" "))

for i in divisor(M):
    if i >= N:
        print (M//i)
        break