from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, acos, asin, atan, sqrt, tan, cos, pi
from operator import mul
from functools import reduce
from pprint import pprint
from copy import deepcopy


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 998244353


n, k = LI()
A = LI()
D = defaultdict(list)
for i in range(n):
    D[A[i]] += [i]


nxt_idx = [0] * n
for idx_list in D.values():
    for j in range(len(idx_list)):
        nxt_idx[idx_list[j]] = idx_list[(j + 1) % len(idx_list)]



ret = 0
now = 0
L = []
visited = set()
while now not in visited:
    visited.add(now)
    nxt = nxt_idx[now]
    diff = (nxt - now) % n if nxt != now else n
    now = (nxt + 1) % n
    ret += diff + 1
    L += [[ret - 1, nxt]]


ans = []
if (n * k - 1) < ret:
    ss = set()
    for i in range(n * k):
        a = A[i % n]
        if a in ss:
            while a in ss:
                ss.remove(ans.pop())
        else:
            ans += [a]
            ss.add(a)
    print(*ans)
    exit()


ll = (n * k - 1) % ret
bb = bisect_right(L, [ll, INF]) - 1
cc, last_idx = L[bb]
ss = set()
for i in range(ll - cc):
    a = A[(last_idx + i + 1) % n]
    if a in ss:
        while a in ss:
            ss.remove(ans.pop())
    else:
        ans += [a]
        ss.add(a)



print(*ans)

