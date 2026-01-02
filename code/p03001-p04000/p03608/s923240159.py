import collections

class WarshallFloyd():
    def __init__(self,N):  #Nは頂点の個数
        self.N = N
        self.d = [[float('inf')]*N for i in range(N)]  #d[i][j] = iからjへの最短距離,0-indexed
    def add(self,u,v,c,directed = False):
        if directed is False:  #無向グラフの場合
            self.d[u][v] = c
            self.d[v][u] = c
        else:  #有向グラフの場合
            self.d[u][v] = c
    def WarshallFloyd_search(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(self.d[i][j],self.d[i][k] + self.d[k][j])
        for i in range(self.N):
            self.d[i][i] = 0
        return self.d

N,M,R = map(int,input().split())
r = list(map(int,input().split()))
data = [list(map(int,input().split())) for i in range(M)]

G = WarshallFloyd(N)

for u,v,c in data:
    G.add(u-1,v-1,c,directed=False)

d = G.WarshallFloyd_search()

A = [i for i in range(R)]

ans = float('inf')

from itertools import permutations

for i in permutations(A,R):
    a = 0
    for j in range(R-1):
        a += d[r[i[j]]-1][r[i[j+1]]-1]
    ans = min(ans,a)

print(ans)