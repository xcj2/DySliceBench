from itertools import permutations
import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def SI(): return sys.stdin.readline()[:-1]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
int1 = lambda x: int(x) - 1
def MI1(): return map(int1, sys.stdin.readline().split())
def LI1(): return list(map(int1, sys.stdin.readline().split()))
p2D = lambda x: print(*x, sep="\n")
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    inf=10**9
    n,m=MI()
    kk=[]
    aa=[]
    for _ in range(m):
        k=0
        a,b=MI()
        aa.append(a)
        cc=LI1()
        for c in cc:k|=1<<c
        kk.append(k)
    dp=[inf]*(1<<n)
    dp[0]=0
    for bit in range(1<<n):
        pre=dp[bit]
        if pre==inf:continue
        for a,k in zip(aa,kk):
            nb=bit|k
            dp[nb]=min(dp[nb],pre+a)
    ans=dp[-1]
    if ans==inf:print(-1)
    else:print(ans)

main()
