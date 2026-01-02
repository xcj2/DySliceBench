n=int(input())
l=[[j for j,k in enumerate(input())if k=="1"]for i in range(n)]
import sys
sys.setrecursionlimit(10**9)
color=[0]*n
def nibu(v,c):
    #True->nibugrahu
    color[v]=c
    for i in l[v]:
        if color[i]==c:return False
        elif color[i]==0 and not nibu(i,-c):
            return False
    return True
if not nibu(0,1):
    print(-1)

else:
    class WarshallFloyd:
        #O(V^3)で任意２頂点の最短距離
        def __init__(self,n,_first_index=0):
            self.v = n
            self._first_idx=_first_index
            self.d = [[float("INF")]*(n) for _ in range(n)]
            for i in range(n):
                self.d[i][i] = 0
    
        def path(self,x,y,c):
            if x == y:
                return False
            f=self._first_idx
            self.d[x-f][y-f] = c
            self.d[y-f][x-f] = c
            return True
    
        def build(self):
            for k in range(self.v):
                for i in range(self.v):
                    for j in range(self.v):
                        self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
            return self.d
    w=WarshallFloyd(n)
    for x in range(n):
        for j in l[x]:
            w.path(x,j,1)
    d=w.build()
    ans=0
    for i in range(n):
        ans=max(ans,max(d[i]))
    print(ans+1)