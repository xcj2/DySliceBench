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

# N <= 300 O(n ** 3)まで
# 何通り dp or combo
N = getN()
# 1つ目の譜面
B = []
for i in range(N):
    q = list(input())
    B.append(q * 2)
B += B
# 2つ目にはなにも書かれてない
# 2つ目の盤面に縦にi、横にjずらして数字を記入する

# 対角線に対して線対称なものの数を求める
# 整数a, bの選び方が何通りあるか

def judge(a, b):
    """
    res = [[''] * N for i in range(N)]
    # 盤面１のB[i][j]を盤面2に書き込む
    for i in range(N):
        for j in range(N):
            res[(i + a) % N][(j + b) % N] = B[i][j]
    """

    for i in range(N):
        for j in range(i, N):
            if B[i + a][j + b] != B[j + a][i + b]:
                return 0
        else:
            continue
        break
    else:
        return 1

# 全てのa, bについて調べるなら１つの(a, b)についてO(N)で求める必要がある
# 判定する際、節約出来ないか？

# N * N のゾーンをずらしていく
# a [b  a] b
# c [a  c] a
# a  b  a  b
# c  a  c  a 対称軸がずれる 軸は2N - 1本ある
# 良い盤面になる条件

# 斜めにずらしていくことで前の結果を利用できる
# 1本の軸について判定した時、1つの盤面が良い盤面なら他全ても良い盤面
# 軸に刺さっている盤面の数を求めればいい

# 軸は2N - 1本ある
# 縦に対角線をずらす
ans = 0
for i in range(N):
    # 軸(0, i)にはN - i本の盤面が連なっている
    # 連なっている全ての盤面は全てTrueか全てFalse
    ans += (N - i) * judge(i, 0)

# 横に対角線をずらす
for i in range(1, N):
    ans += (N - i) * judge(0, i)
print(ans)