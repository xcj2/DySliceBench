import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,M,L = LI()

class WarshallFloyd():
    def __init__(self,N):  # Nは頂点の個数
        self.N = N
        self.d = [[float('inf')]*N for _ in range(N)]  # d[i][j] = iからjへの最短距離,0-indexed
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
        for i in range(self.N):
            self.d[i][i] = 0
        return self.d

G1 = WarshallFloyd(N)

for i in range(M):
    a,b,c = LI()
    G1.add(a-1,b-1,c,directed=False)

G1.WarshallFloyd_search()

G2 = WarshallFloyd(N)

for i in range(N-1):
    for j in range(i+1,N):
        if G1.d[i][j] <= L:
            G2.add(i,j,1,directed=False)

G2.WarshallFloyd_search()

Q = I()
for i in range(Q):
    s,t = LI()
    if G2.d[s-1][t-1] == float('inf'):
        print(-1)
    else:
        print(G2.d[s-1][t-1]-1)

