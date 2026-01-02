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

N, K = getNM()
X = getList()

pos = sorted(v for v in X if v >= 0)
neg = sorted(-v for v in X if v < 0)

# 全てのXの要素を使うなら答えは自明
if N == K:
    ans = 1
    for x in X:
        ans *= x
        ans %= mod
    print(ans % mod)
    exit()

ok = False  # True: ans>=0, False: ans<0
if pos:
    #正の数があるとき
    ok = True
else:
    #全部負-> Kが奇数なら負にならざるをえない。
    ok = (K % 2 == 0)

ans = 1
if ok:
    # ans >= 0
    if K % 2 == 1:
        #Kが奇数の場合初めに1つ正の数を掛けておく
        #こうすれば後に非負でも負でも2つずつのペアで
        #考えられる
        ans = ans * pos.pop() % mod

    # 答えは非負になる→二つの数の積は必ず非負になる．
    cand = []
    while len(pos) >= 2:
        x = pos.pop() * pos.pop()
        cand.append(x)

    while len(neg) >= 2:
        x = neg.pop() * neg.pop()
        cand.append(x)

    cand.sort(reverse = True) # ペアの積が格納されているので必ず非負
    # ペア毎に掛けていく
    for i in range(K // 2):
        ans = ans * cand[i] % mod
else:
    # ans <= 0
    cand = sorted(X, key=lambda x: abs(x))
    for i in range(K):
        ans = ans * cand[i] % mod

print(ans)