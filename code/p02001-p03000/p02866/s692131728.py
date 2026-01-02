
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 998244353
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()
DD = inpl()
cnts = defaultdict(int)
for d in DD:
    cnts[d] += 1

m = max(DD)

if DD[0] != 0 or cnts[0] != 1:
    print(0)
else:
    ans = 1
    for i in range(1,m+1):
        if cnts[i] == 0:
            print(0)
            sys.exit()
        ans *= pow(cnts[i-1],cnts[i],mod)
        ans %= mod

    print(ans%mod)
