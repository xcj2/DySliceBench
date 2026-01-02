import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
MAX = 2 * 10 ** 5 + 5
MOD = 10 ** 9 + 7

fac = [0 for i in range(MAX)]
finv = [0 for i in range(MAX)]
inv = [0 for i in range(MAX)]

def comInit(mod):
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def com(n, r, mod):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod

def p(n, r, mod):
    return fac[n] * finv[n - r] % mod
    
comInit(MOD)

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt_a = Counter(A)
AA = sorted(list(set(A)))
f_max = 0
f_min = 0

acc = 0
for a in AA:
    cnt = cnt_a[a]
    f_min += (com(N - acc, K, MOD) - com(N - acc - cnt, K, MOD)) * a
    f_min %= MOD
    acc += cnt

acc = 0
for a in AA[::-1]:
    cnt = cnt_a[a]
    f_max += (com(N - acc, K, MOD) - com(N - acc - cnt, K, MOD)) * a
    f_max %= MOD
    acc += cnt
print((f_max - f_min) % MOD)
