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


MAX = 1000001
factor = [0] * (MAX + 1)


def generatePrimeFactors():
    factor[1] = 1
    for i in range(2, MAX):
        factor[i] = i
    for i in range(4, MAX, 2):
        factor[i] = 2
    i = 3
    while i * i < MAX:
        if factor[i] == i:
            j = i * i
            while j < MAX:
                if factor[j] == j:
                    factor[j] = i
                j += i
        i += 1


def calculateNoOFactors(n):
    if n == 1:
        return 1
    ans = 1
    dup = factor[n]
    c = 1
    j = int(n / factor[n])
    while j > 1:
        if factor[j] == dup:
            c += 1
        else:
            dup = factor[j]
            ans = ans * (c + 1)
            c = 1
        j //= factor[j]
    ans = ans * (c + 1)
    return ans


sq = set()
i = 1
while True:
    sq.add(i * i)
    if i * i > 10 ** 6:
        break
    i += 1
number = int(data())
generatePrimeFactors()
answer = 0
for i in range(1, number):
    fact = calculateNoOFactors(i)
    answer += fact
out(answer)
