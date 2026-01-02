# coding: utf-8
import sys
sys.setrecursionlimit(1000000)

N = int(input())

MAX_N=10**6
MOD=10**9+7

fac=[None for i in range(MAX_N)]
finv=[None for i in range(MAX_N)]
inv=[None for i in range(MAX_N)]

def COMinit(num):
    global fac
    global finv
    global inv
    fac[0]=1
    fac[1]=1
    finv[0]=1
    finv[1]=1
    inv[1]=1

    for i in range(2,num):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

def COM(n,k):
    if n<k:
        return 0
    elif n<0 or k<0:
        return 0
    else:
        return int(fac[n] * (finv[k] * finv[n - k] % MOD) % MOD)


#a**n mod p を再帰的に求める
def modPow(a,n,p):

    if n==0:
        return 1
        
    if n == 1:
        
        #n=1ならaを返す
        return a % p

    elif n % 2 == 1:
        #nが奇数ならば a * modPow(a,n-1(偶数),p)を返す
        return a * modPow(a,n-1,p) % p

    else:
        #nが偶数なら modPow(a,n//2,p) * modPow(a,n//2,p)とすると速い
        t = modPow(a,n//2,p)
        return t * t % p

COMinit(MAX_N)

if N>2:
    ans = (modPow(10,N,MOD) - 2*modPow(9,N,MOD) + modPow(8,N,MOD))%MOD
elif N == 1:
    ans = 0
elif N == 2:
    ans = 2

print(ans)
