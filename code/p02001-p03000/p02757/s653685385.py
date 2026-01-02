from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,p = inpl()
s = input()[::-1]
res = 0
if p == 2 or p == 5:
    s = s[::-1]
    for i,t in enumerate(s):
        if int(t)%p == 0: 
            res += i+1
    print(res)
    quit()
now = 0
d = [0] * p
d[0] = 1
for i,t in enumerate(s):
    now += int(t) * pow(10,i,p)
    now %= p
    d[now] += 1
for i in range(p):
    v = d[i]
    res += v*(v-1)//2
print(res)