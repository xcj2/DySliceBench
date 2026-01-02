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

def bitcount(a, N):
  return sum((a & (1 << i)) > 0 for i in range(N))

def topbit(a, N):
  return next(i for i in range(N-1, -1, -1) if (a & (1 << i)) > 0)

def swap(x, i, j):
  y = x & ~(1 << i) & ~(1 << j)
  if (x & (1 << i)) > 0:
    y |= 1 << j
  if (x & (1 << j)) > 0:
    y |= 1 << i
  return y

def solve(N, A, B):
  if N == 1:
    ans = [A & 1, B & 1]
    return ans
  C = A ^ B
  t = topbit(C, N)
  AA = swap(A, t, N-1)
  BB = swap(B, t, N-1)
  D = AA ^ 1
  ans = []
  if B & (1 << t) > 0:
    ans.extend(swap(x, t, N-1) for x in solve(N-1, AA, D))
    ans.extend(swap(x, t, N-1) | (1 << t) for x in solve(N-1, D, BB))
  else:
    ans.extend(swap(x, t, N-1) | (1 << t)for x in solve(N-1, AA, D))
    ans.extend(swap(x, t, N-1) for x in solve(N-1, D, BB))
  return ans

N, A, B = reads()
if bitcount(A ^ B, N) % 2 == 0:
  print("NO"); exit()
print("YES")
print(*solve(N, A, B))
