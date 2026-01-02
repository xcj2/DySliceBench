from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
d = defaultdict(int)
for i in range(n):
    s = list(input())
    s.sort()
    tmp = ''.join(s)
    d[tmp] += 1
res = 0
for key in list(d):
    v = d[key]
    res += v*(v-1)//2
print(res)