from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

N = read()
S = input()

former = defaultdict(lambda: 0)
latter = defaultdict(lambda: 0)

def power(n):
  return chain(*(combinations(range(n), r) for r in range(n+1)))

def solve(N, S):
  for p in power(N):
    bs1 = []; rs1 = []; bs2 = []; rs2 = []
    for i in range(N):
      if i in p:
        rs1.append(S[i])
        rs2.append(S[-1-i])
      else:
        bs1.append(S[i])
        bs2.append(S[-1-i])
    former["".join(rs1), "".join(bs1)] += 1
    latter["".join(bs2), "".join(rs2)] += 1

  ans = 0
  for k, v in former.items():
    if k in latter:
      ans += v * latter[k]

  return ans

print(solve(N, S))