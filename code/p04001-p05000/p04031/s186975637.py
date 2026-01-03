from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
min_a = min(a)
max_a = max(a)
res = mod
for i in range(min_a, max_a + 1):
    cost = 0
    for j in a:
        cost += abs(i-j) ** 2
    res = min(res, cost)
print(res)