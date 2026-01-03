from heapq import *
from collections import defaultdict
INF = float('inf')
class Prim:

    def __init__(self,N):#Nはグラフのノード数
        self.N = N
        self.cost = defaultdict(list)
        self.used = [False for _ in range(N)]
    
    def setcost(self,u,v,w):
        self.cost[u].append((v,w))
        self.cost[v].append((u,w))
    
    def prim(self):
        que = []
        heapify(que)
        used = self.used
        for e in self.cost[0]:
            heappush(que,[e[1],e[0]])
        used[0] = True
        res = 0
        while que:
            p = heappop(que)
            cos,v = p
            if used[v]:continue
            self.used[v] = True
            for e in self.cost[v]:
                if not used[e[0]]:
                    heappush(que,[e[1],e[0]])      
            res += cos
        return res

def main():
    N = int(input())
    cost = []
    for i in range(N):
        x,y = map(int,input().split())
        cost.append((x,y,i))
    prim = Prim(N)
    x = tuple(sorted(cost,key=lambda x: x[0]))
    y = tuple(sorted(cost,key=lambda x: x[1]))
    for i in range(N-1):
        a,b,u = x[i]
        c,d,v = x[i+1]
        w = min(abs(a-c),abs(b-d))
        prim.setcost(u,v,w)
        e,f,s = y[i]
        g,h,t = y[i+1]
        u = min(abs(e-g),abs(f-h))
        prim.setcost(s,t,u)
    ans = prim.prim()
    print(ans)
if __name__ == "__main__":
    main()