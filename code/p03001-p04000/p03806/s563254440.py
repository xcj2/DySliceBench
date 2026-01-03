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
    n,ma,mb=MI()
    vv=[]
    cc=[]
    for _ in range(n):
        a,b,c=MI()
        vv.append(a*mb-b*ma)
        cc.append(c)
    dp=[[inf]*8005 for _ in range(n+1)]
    for i in range(n):
        v,c=vv[i],cc[i]
        dp[i + 1][4000+v] = min(dp[i + 1][4000+v], c)
        for j in range(8005):
            pre=dp[i][j]
            if pre==inf:continue
            dp[i + 1][j] = min(dp[i + 1][j], pre)
            dp[i + 1][j + v] = min(dp[i + 1][j + v], pre + c)
    ans=dp[-1][4000]
    if ans==inf:print(-1)
    else:print(ans)

main()
