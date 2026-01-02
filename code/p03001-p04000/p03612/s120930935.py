from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
res = 0
for i in range(n):
    if a[i] == i + 1:
        res += 1
        if i != n-1:
            a[i],a[i+1] = a[i+1],a[i]
print(res)
        