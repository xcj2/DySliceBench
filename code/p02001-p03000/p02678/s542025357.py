import sys
# from functools import lru_cache, cmp_to_key
# from heapq import merge, heapify, heappop, heappush
from math import sqrt, sin, cos, pi
from collections import defaultdict as dd, deque, Counter as C
# from itertools import combinations as comb, permutations as perm
# from bisect import bisect_left as bl, bisect_right as br, bisect
# from time import perf_counter
# from fractions import Fraction

# sys.setrecursionlimit(pow(10, 6))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
mod = pow(10, 9) + 7
mod2 = 998244353


def data(): return sys.stdin.readline().strip()


def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)


def l(): return list(sp())


def sl(): return list(ssp())


def sp(): return map(int, data().split())


def ssp(): return map(str, data().split())


def l1d(n, val=0): return [val for i in range(n)]


def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


inf = 10 ** 20
n, m = sp()
graph = dd(set)
for i in range(m):
    u, v = sp()
    graph[u].add(v)
    graph[v].add(u)
dist = dd(lambda: inf)
dist[1] = 0
answer = dd(int)
vis = dd(lambda: False)
vis[1] = True
stack = deque()
stack.append(1)
while stack:
    temp = stack.popleft()
    for child in graph[temp]:
        if not vis[child]:
            stack.append(child)
            vis[child] = True
        if dist[child] > dist[temp] + 1:
            dist[child] = dist[temp] + 1
            answer[child] = temp
for i in range(1, n+1):
    if not vis[i]:
        out("No")
        exit()
out("Yes")
for i in range(2, n+1):
    out(answer[i])
