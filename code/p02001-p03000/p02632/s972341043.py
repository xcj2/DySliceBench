def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

"""
dp[i][j]を
「i文字目まででj回Sの文字を使ったか」とする

K = 5
S = 'oof'
dp = [[0] * (len(S) + 1) for i in range(K + len(S) + 1)]
dp[0][0] = 1

for i in range(1, K + len(S) + 1):
    for j in range(len(S) + 1):
        if j < len(S):
            dp[i][j] += dp[i - 1][j] * 25
        else:
            dp[i][j] += dp[i - 1][j] * 26 # j回使い切るともうSは関係なくなるので *= 26になる
        if j >= 1:
            dp[i][j] += dp[i - 1][j - 1]

l_s = len(S)
どのタイミングで「この先ずっと*= 26」になるか
後ろからi文字目にSを使い切る: pow(25, K - k, mod) * cmb(N + K - k - 1, N - 1) * pow(26, k, mod)
...
"""

lim = 2 * (10 ** 6) + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    if r == 0:
        return 1
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

K = getN()
S = input()
N = len(S)

ans = 0
# l_s + i文字目に文字を使い切る
# 次から *= 26
for k in range(K + 1):
    # 逆からやってる
    ans += cmb(N + K - k - 1, N - 1) * pow(26, k, mod) * pow(25, K - k, mod) % mod
    ans %= mod

print(ans)