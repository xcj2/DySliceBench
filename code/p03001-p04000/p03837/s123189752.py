import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()


class WarshallFloyd():
    def __init__(self,N):  # Nは頂点の個数
        self.N = N
        self.d = [[float('inf')]*N for i in range(N)]  # d[i][j] = iからjへの最短距離,0-indexed
    def add(self,u,v,c,directed = False):
        if directed is False:  # 無向グラフの場合
            self.d[u][v] = c
            self.d[v][u] = c
        else:  # 有向グラフの場合
            self.d[u][v] = c
    def WarshallFloyd_search(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(self.d[i][j],self.d[i][k] + self.d[k][j])
        return self.d


W = WarshallFloyd(N)
edges = [0]*M
for i in range(M):
    a,b,c = MI()
    W.add(a-1,b-1,c,directed=False)
    edges[i] = (a-1,b-1,c)
for i in range(N):
    W.add(i,i,0)

W.WarshallFloyd_search()

ans = 0
for i in range(M):
    a = 0
    for j in range(N):
        if W.d[edges[i][0]][edges[i][1]] == edges[i][2]:
            a = 1
    if a == 0:
        ans += 1

print(ans)
