#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n):
  res = [None] * n
  for i in range(n):
    res[i] = II()
  return res
def LIR(n):
  res = [None] * n
  for i in range(n):
    res[i] = LI()
  return res
def FR(n):
  res = [None] * n
  for i in range(n):
    res[i] = IF()
  return res
def LIR(n):
  res = [None] * n
  for i in range(n):
    res[i] = IF()
  return res
def LIR_(n):
  res = [None] * n
  for i in range(n):
    res[i] = LI_()
  return res
def SR(n):
  res = [None] * n
  for i in range(n):
    res[i] = S()
  return res
def LSR(n):
  res = [None] * n
  for i in range(n):
    res[i] = LS()
  return res
mod = 1000000007
inf = float('INF')

#solve
def solve():
  def f(n, c):
    tmp = n % c
    t = tmp
    b = 0
    while tmp:
      if tmp & 1:
        b += 1
      tmp //= 2
    if t:
      return f(t, b) + 1
    else:
      return 1
  n = II()
  a = S()
  b = 0
  for ai in a:
    if ai == "1":
      b += 1
  a = a[::-1]
  bp = 0
  bm = 0
  if b != 1:
    for i, ai in enumerate(a):
      if ai == "1":
        bp += pow(2, i, b + 1)
        bm += pow(2, i, b - 1)
        bp %= b + 1
        bm %= b - 1
    ans = []
    for i, ai in enumerate(a):
      if ai == "1":
        tmpbm = bm - pow(2, i, b - 1)
        tmpbm %= b - 1
        ans.append(f(tmpbm, b - 1))
      else:
        tmpbp = bp + pow(2, i, b + 1)
        tmpbp %= b + 1
        ans.append(f(tmpbp, b + 1))
    for ai in ans[::-1]:
      print(ai)
    return
  else:
    for i, ai in enumerate(a):
      if ai == "1":
        bp += pow(2, i, b + 1)
        bp %= b + 1
    ans = []
    for i, ai in enumerate(a):
      if ai == "1":
        ans.append(0)
      else:
        tmpbp = bp + pow(2, i, b + 1)
        tmpbp %= b + 1
        ans.append(f(tmpbp, b + 1))
    for ai in ans[::-1]:
      print(ai)
    return


#main
if __name__ == '__main__':
  solve()
