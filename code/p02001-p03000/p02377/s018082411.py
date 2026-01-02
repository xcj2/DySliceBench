# ノードをtupleで渡す
from collections import defaultdict
from heapq import *
class MinCostFlow:
    def __init__(self):
        self.inf=10**9
        self.to = defaultdict(dict)

    def add_edge(self, u, v, cap, cost):
        self.to[u][v]=[cap, cost]
        self.to[v][u]=[0, -cost]

    # s...source,t...sink,f...flow
    # これが本体
    def cal(self,s,t,f):
        min_cost=0
        pot=defaultdict(int)
        while f:
            dist = {}
            pre_u={}   # 最短距離の遷移元の頂点
            # ダイクストラで最短距離を求める
            hp=[]
            heappush(hp,(0,s))
            dist[s]=0
            while hp:
                d,u=heappop(hp)
                if d>dist[u]:continue
                for v,[cap,cost] in self.to[u].items():
                    if cap==0:continue
                    nd=dist[u]+cost+pot[u]-pot[v]
                    dist.setdefault(v, self.inf)
                    if nd>=dist[v]:continue
                    dist[v]=nd
                    pre_u[v]=u
                    heappush(hp,(nd,v))
            # sinkまで届かなかったら不可能ということ
            if t not in dist:return -1
            # ポテンシャルを更新する
            for u,d in dist.items():pot[u]+=d
            # パスs-t上で最小の容量=流す量を求める
            u=t
            min_cap=f
            while u!=s:
                u,v=pre_u[u],u
                min_cap=min(min_cap,self.to[u][v][0])
            # フローから流す量を減らし、コストを加える
            f-=min_cap
            min_cost+=min_cap*pot[t]
            # パスs-tの容量を更新する
            u=t
            while u!=s:
                u,v=pre_u[u],u
                self.to[u][v][0]-=min_cap
                self.to[v][u][0]+=min_cap
        return min_cost

def main():
    n,m,f=map(int,input().split())
    mc=MinCostFlow()
    for _ in range(m):
        u,v,c,d=map(int,input().split())
        mc.add_edge(u,v,c,d)
    print(mc.cal(0,n-1,f))

main()

