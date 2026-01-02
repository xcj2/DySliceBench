from sys import exit, setrecursionlimit, stderr, stdin
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect

setrecursionlimit(10**7)

M = 10 ** 9 + 7

def input():
  return stdin.readline().strip()

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

def solve():
  N = read()
  C = [-1] * N
  p = 0
  for i in range(N):
    c = read() - 1
    if C[p-1] != c:
      C[p] = c
      p += 1
  N = p
  del C[N:]

  dp = [0] * (N+1)
  dp[0] = 1
  last = [0] * (2 * 10**5 + 10)
  for i in range(N):
    c = C[i]
    last[c] = (last[c] + dp[i]) % M
    dp[i+1] = last[c]
  # print('dp', dp)
  print(dp[-1])

solve()