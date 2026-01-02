#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

fact = [1]
for i in range(1, N+10):
    fact.append(fact[-1] * i % MOD)
def rev(x):
    return pow(x, MOD-2, MOD)
def cmb(i, k):
    if(i < k): return 0
    return fact[i] * rev(fact[k]) * rev(fact[i-k]) % MOD

minus = 0
plus = 0

for i, a in enu(A):
    mval = cmb(N-i-1, K-1)
    pval = cmb(i, K-1)
    if i<=K-2:
        pval = 0
    if N-K+1<=i:
        mval = 0
#    print(mval, pval)
    minus -= a*mval
    plus += a*pval

print((plus+minus)%MOD)

 
