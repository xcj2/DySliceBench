from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
M = mod = 10**9 +7
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
def li4():return [float(i) for i in input().rstrip('\n').split(' ')]


def dfs(root):
    global ans,g
    if ans[root]:return 

    temp = 0
    for j in g[root]:dfs(j)
    if len(g[root]):temp = max(ans[j] for j in g[root])
    ans[root] = 1 + temp

n,m = li()
g = defaultdict(set)
for i in range(m):
    a,b = li()
    g[a].add(b)

ans = [0]*(n + 1)

for j in range(1,n + 1):
    if not ans[j]:dfs(j)

print(max(ans) - 1)