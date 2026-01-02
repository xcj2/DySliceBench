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
pl = lambda x: print(*x, sep='\n')

N, K = map(int, input().split())

fact = [1]
for i in range(1, N+10):
    fact.append(fact[-1] * i % MOD)
def rev(x):
    return pow(x, MOD-2, MOD)
def cmb(i, k):
    if(i < k): return 0
    return fact[i] * rev(fact[k]) * rev(fact[i-k]) % MOD

for i in range(1, K+1):
    print((cmb(N-K+1, i) * cmb(K-1, i-1))%MOD)

