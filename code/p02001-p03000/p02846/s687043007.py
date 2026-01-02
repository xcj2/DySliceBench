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
mod = 998244353

#############
# Main Code #
#############

T1, T2 = getNM()
A1, A2 = getNM()
B1, B2 = getNM()

# グラフにして考える
# 周期は同じT1, T2
# T1の時とT2の時とで順位が入れ替わっているなら出会っている
t1_diff = (A1 - B1) * T1
t2_diff = (A1 - B1) * T1 + (A2 - B2) * T2
if t1_diff == 0 or t2_diff == 0: # 無限に出会う
    print('infinity')
    exit()
if t1_diff * t2_diff > 0: # ずっとどちらかが前にいる
    print(0)
    exit()

# t2_diff分ずつずれていく

# 順位が逆転する場合
# クロスする時とちょうど接する時を考える
if abs(t1_diff) % abs(t2_diff) == 0:
    # 最後の１回は１回しかクロスしない
    print((abs(t1_diff) // abs(t2_diff)) * 2)
else:
    print((abs(t1_diff) // abs(t2_diff)) * 2 + 1)