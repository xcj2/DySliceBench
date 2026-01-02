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
# 問題:N問、ジャッジ:M人
# M人のジャッジがそれぞれV問を選び、問題のスコアを１ずつあげる
# M人の投票の後、大きい方からP問が選ばれる
# 問題セットに選ばれる可能性があるのは何問あるか

M人全員が投票すれば選ばれやすくなる
選ばれるとは？
可能性がないものを数えた方が早いのでは
P番目以内にあれば無条件で通過
現在のP番目 <= A[i] + M
V <= Pなら
上からP - 1番目までのどれか + A[i]を加算させることでA[i]を強くできる　
V > Pなら？
上からP - 1番目までとA[i]を強化するとして、残りのV - P個は小さいものから順に選ぶ
A[i]を抜かせないようにしたい
A[i]より大きい数字も一緒に足される場合にはP以内に入れない
"""
N, M, V, P = getNM()
A = getList()
A.sort(reverse = True)

def judge(x):
    if x < P:
        return True
    if A[P - 1] > A[x] + M:
        return False
    # P - 1番目まで + 自身以降の数字についてはM個足す
    left = (V - (P - 1) - (N - x)) * M
    # P個目からx-1まで A[x] + Mを超えない分足す
    for i in range(P - 1, x):
        left -= A[x] + M - A[i]

    return left <= 0

ok = -1
ng = N

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok + 1)