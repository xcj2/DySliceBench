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
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
        return self.d
h,w=map(int,input().split())
war=WarshallFloyd(10)
for i in range(10):
    s=list(map(int,input().split()))

    for j in range(10):
        war.path(i,j,s[j])
dis=war.build()
from collections import Counter as co
l=[list(map(int,input().split())) for i in range(h)]
l=sum(l,[])
var=co(l).items()
print(sum([0]+[v*dis[k][1] for k,v in var if k!=-1]))