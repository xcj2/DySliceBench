import sys
readline = sys.stdin.readline

MOD = 10**9+7
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
        frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci
frac, fraci = frac(2341398)
def comb(a, b):
    if not a >= b >= 0:
        return 0
    return frac[a]*fraci[b]*fraci[a-b]%MOD

def accumulate2d(X2):
    X = X2
    N = len(X)
    M = len(X[0])
    
    for i in range(N):
        for j in range(1, M):
            X[i][j] += X[i][j-1]
    
    for j in range(M):
        for i in range(1, N):
            X[i][j] += X[i-1][j]
    
    return X

r1, c1, r2, c2 = map(int, readline().split())

def calc(R, C):
    if min(R, C) == 0:
        return 1
    res = R
    for i in range(1, C):
        res = (res + comb(R+i, i+1)) % MOD
    return res
r2 += 1
c2 += 1
print((calc(r2, c2)-calc(r2, c1)-calc(r1, c2)+calc(r1, c1))%MOD)