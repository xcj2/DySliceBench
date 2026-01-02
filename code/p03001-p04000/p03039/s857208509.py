import sys
sys.setrecursionlimit(100000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
N, M, K = map(int, input().split())
L = N*M
mod = 10**9+7
def factrial(N):
    fc = [1, 1] + [None] * N
    inv = [0, 1] + [None] * N
    fcInv = [1, 1] + [None] * N
    for i in range(2, N+1):
        fc[i] = i*fc[i-1]%mod
        inv[i] = mod-(inv[mod%i]*(mod//i))%mod
        fcInv[i] = fcInv[i-1]*inv[i]%mod
    return fc, fcInv
fc, fcInv = factrial(L)
def modCom(n, k):
    return 0 if n < k else fc[n] * fcInv[k] * fcInv[n-k] % mod
ans = 0
for d in range(1, N):
    ans += d*(N-d)*M*M*modCom(L-2, K-2)
    ans %= mod
for d in range(1, M):
    ans += d*(M-d)*N*N*modCom(L-2, K-2)
    ans %= mod
print(ans)
