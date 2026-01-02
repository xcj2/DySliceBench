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


n = int(data())
a = L()
b = L()
i = 0
temp = 0
r = True
for j in range(n):
    if temp != a[j]:
        i = 0
    if a[j] == b[j]:
        while i < n:
            if a[i] != a[j] and b[i] != a[j]:
                b[i], b[j] = b[j], b[i]
                break
            i += 1
        if a[j] == b[j]:
            out("No")
            exit()
    temp = a[j]
out("Yes")
outa(*b)
