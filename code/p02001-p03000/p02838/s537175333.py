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
a = inpl()
a.sort()
ln = len(bin(a[-1])) - 2
bit = [[0,0] for i in range(ln)]
res = 0
for i in a:
    for j in range(ln):
        tmp = 0
        if (i>>j) % 2:
            tmp += 1
        bit[j][tmp] += 1
for i,j in enumerate(bit):
    c = pow(2,i)
    res += j[0] * j[1] * c
    res %= mod
print(res)