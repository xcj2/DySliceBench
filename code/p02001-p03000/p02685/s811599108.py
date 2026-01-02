#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 998244353
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

def main():
    N, M, K = map(int, input().split())

    fact = [1]
    for i in range(1, N+3):
        fact.append(fact[-1] * i % MOD)
    def rev(x):
        return pow(x, MOD-2, MOD)
    def cmb(i, k):
        if(i < k): return 0
        return fact[i] * rev(fact[k]) * rev(fact[i-k]) % MOD

    def count(m, k):
        combo = cmb(N-1, k)
        col = m * pow(m-1, N-k-1, MOD)
        val = (combo*col)%MOD
        return val

    cnt = 0
    for k in range(0, K+1):
        addval = count(M, k)
        cnt += addval
        cnt %= MOD

    print(cnt)
if __name__=='__main__':
    main()