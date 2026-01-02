import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dfs(i=-1,s=0,cnt=1):
        if cnt==rn:return s
        if i==-1:
            return min(dfs(j) for j in range(rn))
        vis[i]=True
        ri=rr[i]
        res=inf
        for j in range(rn):
            if vis[j]:continue
            rj=rr[j]
            res=min(res,dfs(j,s+dist[ri][rj],cnt+1))
        vis[i]=False
        return res


    inf=10**9
    n, m, rn = MI()
    rr = LI()
    to = defaultdict(list)
    dist=[[inf]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = MI()
        a, b = a - 1, b - 1
        to[a].append((b, c))
        to[b].append((a, c))
        dist[a][b]=dist[b][a]=c
    for w in range(n):
        distw=dist[w]
        for u in range(n):
            for v in range(n):
                duv=distw[u]+distw[v]
                if duv<dist[u][v]:dist[u][v]=dist[v][u]=duv
    vis=[False]*rn
    print(dfs())

main()
