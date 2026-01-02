import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
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
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


n, k = sp()
arr = l()
answer = [1]
s = {1}
index = 1
while True:
    temp = arr[answer[-1]-1]
    if temp in s:
        index = temp
        break
    s.add(temp)
    answer.append(temp)
if k <= len(answer)-1:
    out(answer[k])
    exit()
k -= (len(answer)-1)
temp = answer.index(index)
answer = answer[temp:]
k %= len(answer)
if k == 0:
    k = len(answer)
out(answer[k-1])
