import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush, nlargest, nsmallest
from math import ceil, floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
# sys.setrecursionlimit(pow(10, 6))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(" ".join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]

@lru_cache(None)
def recur(temp, index=0, cost=0):
    if index == n:
        for j in range(m):
            if temp[j] < x:
                return inf
        return cost
    answer = inf
    answer = min(answer, recur(temp, index+1, cost))
    temp = list(temp)
    for j in range(m):
        temp[j] += mat[index][j+1]
    cost += mat[index][0]
    answer = min(answer, recur(tuple(temp), index+1, cost))
    return answer


n, m, x = sp()
mat = []
for i in range(n):
    mat.append(l())
res = recur(tuple([0]*m))
if res == inf:
    out(-1)
    exit()
out(res)
