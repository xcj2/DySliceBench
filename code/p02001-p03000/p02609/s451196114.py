import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
X = input()

def bitcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''
    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)
    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

def popcount(n):
    cnt = 0
    while n:
        n %= bitcount(n)
        cnt += 1
    return cnt

pl = [0]*(N+1)
for i in range(N+1):
    pl[i] = popcount(i)
bn = X.count("1")

modp = [0]*N
modm = [0]*N

for i in range(N):
    if X[i] == "1":
        modp[i] = pow(2, N-1-i, bn+1)
        if not bn == 1:
            modm[i] = pow(2, N-1-i, bn-1)

sp = sum(modp)
sm = sum(modm)
ans = [0]*N
for i in range(N):
    if X[i] == "1":
        if bn == 1:
            ans[i] = 0
            continue
        s = sm
        s -= modm[i]
        s %= bn-1
        ans[i] = pl[s]+1
    else:
        s = sp
        s += pow(2, N-1-i, bn+1)
        s %= bn+1
        ans[i] = pl[s]+1

print(*ans, sep="\n")
