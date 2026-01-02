import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dfs(u=0,pu=-1):
        w,b=1,1
        for v in to[u]:
            if v==pu:continue
            dfs(v,u)
            vw,vb=dp[v]
            w*=(vw+vb)
            b*=vw
        dp[u]=[w%md,b%md]

    md=10**9+7
    to=defaultdict(list)
    n=int(input())
    for _ in range(n-1):
        x,y=map(int1,input().split())
        to[x].append(y)
        to[y].append(x)
    dp=[[0]*2 for _ in range(n)]
    dfs()
    print(sum(dp[0])%md)

main()