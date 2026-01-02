from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
xy = [[] for i in range(n)]
for i in range(n):
    for j in range(inp()):
        a,b = inpl()
        a -= 1
        xy[i].append([a,b])

def check(h):
    t = [0] * n
    for i,j in enumerate(h):
        t[i] = j
    for i,j in enumerate(h):
        if j:
            for k in xy[i]:
                if t[k[0]] != k[1]:
                    return False
    return True

def dfs(h):
    if len(h) == n:
        if check(h):
            return sum(h)
        else:
            return 0
    return max(dfs(h + [True]), dfs(h + [False]))
print(dfs([]))