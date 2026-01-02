import sys
from heapq import *

sys.setrecursionlimit(10 ** 6)

def main():
    def judge(u=0,b=False):
        bt[u]=b
        res=False
        for ku in range(n):
            if not to[u][ku]:continue
            if bt[ku]==b:
                return True
            if bt[ku]==None:
                res|=judge(ku,not b)
        return res

    def bfs(u):
        hp=[]
        heappush(hp,(0,u))
        while hp:
            d,u=heappop(hp)
            for v in range(n):
                if not to[u][v]:continue
                if dis[v]!=-1:continue
                dis[v]=d+1
                heappush(hp,(d+1,v))

    n = int(input())
    to = [[c == "1" for c in input()] for _ in range(n)]
    bt=[None]*n
    if judge():
        print(-1)
        exit()
    ans=0
    for u in range(n):
        dis=[-1]*n
        dis[u]=0
        bfs(u)
        ans=max(ans,max(dis)+1)
    print(ans)
main()
