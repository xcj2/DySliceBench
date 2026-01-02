import sys
from math import log2,floor,ceil,sqrt
# import bisect
# from collections import deque

Ri = lambda : [int(x) for x in sys.stdin.readline().split()]
ri = lambda : sys.stdin.readline().strip()
 
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10**9+7

n = int(ri())
s  = set([i**5 for i in range(1001)])
f,l = -1,-1
sign = 1
for i in s:
    if n+i in s:
        f = i
        l = n+i
        break
    if n-i in s:
        sign = -1
        f = i
        l = n-i
        break
print(int(pow(l,1/5)),int(sign*pow(f,1/5)))