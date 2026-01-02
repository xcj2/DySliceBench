"""
                            pppppppppppppppppppp
                         ppppp  ppppppppppppppppppp
                      ppppppp    ppppppppppppppppppppp
                      pppppppp  pppppppppppppppppppppp
                      pppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppppp
       ppppppppppppppppppppppppppppppppppppppppppppppp  pppppppppppppppppppp
      pppppppppppppppppppppppppppppppppppppppppppppppp  ppppppppppppppppppppp
     ppppppppppppppppppppppppppppppppppppppppppppppppp  pppppppppppppppppppppp
    ppppppppppppppppppppppppppppppppppppppppppppppp    pppppppppppppppppppppppp
   pppppppppppppppppppppppppppppppppppppppppppppp     pppppppppppppppppppppppppp
  ppppppppppppppppppppppppppppppppppppppppppppp      pppppppppppppppppppppppppppp
  pppppppppppppppppppppppppppppppp               pppppppppppppppppppppppppppppppp
  pppppppppppppppppppppppppppp     pppppppppppppppppppppppppppppppppppppppppppppp
  ppppppppppppppppppppppppppp    pppppppppppppppppppppppppppppppppppppppppppppppp
    pppppppppppppppppppppppp  pppppppppppppppppppppppppppppppppppppppppppppppppp
     ppppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppppppp
      pppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppppp
       ppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppppp
                              pppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppp  pppppppp
                              ppppppppppppppppppppp    ppppppp
                                 ppppppppppppppppppp  ppppp
                                    pppppppppppppppppppp
"""


import sys
from functools import lru_cache, cmp_to_key
from collections import defaultdict as dd, deque, Counter as C
from bisect import bisect_left as bl, bisect_right as br, bisect
from heapq import heapify, heappop, heappush
from math import ceil, log, floor, sqrt
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(var, end="\n"): sys.stdout.write(str(var)+end)
def outa(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


# def valid(a, b):
#     return 0 <= a < n and 0 <= b < m
#
#
# n, m = sp()
# sx, sy = sp()
# ex, ey = sp()
# sx -= 1
# sy -= 1
# ex -= 1
# ey -= 1
# mat = [list(data()) for i in range(n)]
# answer = 10 ** 10
# q = deque()
# q.append([sx, sy, 0])
# x, y = [-1, 1, 0, 0], [0, 0, -1, 1]
# vis = [[0] * m for _ in range(n)]
# vis[sx][sy] = 1
# while q:
#     sx, sy, jm = q.popleft()
#     if sx == ex and sy == ey:
#         answer = min(answer, jm)
#         continue
#     cnt = 0
#     for i in range(4):
#         tx, ty = sx + x[i], sy + y[i]
#         if valid(tx, ty) and mat[tx][ty] == ".":
#             if tx == ex and ty == ey:
#                 answer = min(answer, jm)
#                 cnt += 1
#             elif not vis[tx][ty]:
#                 q.append([tx, ty, jm])
#                 vis[tx][ty] = 1
#                 cnt += 1
#     if cnt == 0:
#         jm += 1
#         for i in range(-2, 3):
#             for j in range(-2, 3):
#                 tx, ty = sx + i, sy + j
#                 if valid(tx, ty) and mat[tx][ty] == ".":
#                     if tx == ex and ty == ey:
#                         answer = min(answer, jm)
#                     elif not vis[tx][ty]:
#                         q.append([tx, ty, jm])
#                         vis[tx][ty] = 1
# if answer == 10 ** 10:
#     print(-1)
#     exit()
# print(answer)
n, m, b = sp()
c1, c2 = [0] * n, [0] * m
s = set()
for i in range(b):
    x, y = sp()
    x -= 1
    y -= 1
    c1[x] += 1
    c2[y] += 1
    s.add((x, y))
answer = 0
m1, m2 = max(c1), max(c2)
l1, l2 = [], []
for i in range(n):
    if c1[i] == m1:
        l1.append(i)
for i in range(m):
    if c2[i] == m2:
        l2.append(i)
answer = m1 + m2 - 1
for i in l1:
    for j in l2:
        if (i, j) not in s:
            out(answer + 1)
            exit()
out(answer)
