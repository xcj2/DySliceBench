import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10 ** 9 + 7

def cumprod(A, MOD = MOD):
    L = len(A); Lsq = int(L**.5+1)
    A = np.resize(A, Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        A[:,n] *= A[:,n-1]; A[:,n] %= MOD
    for n in range(1,Lsq):
        A[n] *= A[n-1,-1]; A[n] %= MOD
    return A.ravel()[:L]


def make_fact(U, MOD = MOD):
    x = np.arange(U, dtype = np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    fact.flags.writeable = False
    fact_inv.flags.writeable = False
    return fact,fact_inv

fact, fact_inv = make_fact(2 * 10**6 + 10)

def F(i,j):
    return fact[i+j+2] * fact_inv[i+1] % MOD * fact_inv[j+1] % MOD

a,b,c,d = map(int,read().split())

answer = F(c,d) - F(a-1,d) - F(c,b-1) + F(a-1,b-1)
answer %= MOD
print(answer)
