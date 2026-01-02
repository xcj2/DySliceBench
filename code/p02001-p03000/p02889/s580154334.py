import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,M,L = MI()


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
for i in range(M):
    a,b,c = MI()
    W.add(a-1,b-1,c,directed=False)
d = W.WarshallFloyd_search()

d2 = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if d[i][j] <= L:
            d2[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            d2[i][j] = min(d2[i][j],d2[i][k]+d2[k][j])

Q = I()
for i in range(Q):
    s,t = MI()
    if d2[s-1][t-1] == float('inf'):
        print(-1)
        continue
    print(d2[s-1][t-1]-1)
