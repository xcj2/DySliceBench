from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
s = input()
res = 0
for i in range(n):
    cnt = 0
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for j in range(0,i):
        d1[s[j]] += 1
    for j in range(i,n):
        d2[s[j]] += 1
    for key in d1.keys():
        if d2[key] > 0:
            cnt += 1
    res = max(res, cnt)
print(res)
