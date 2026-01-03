import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)]
                  for i in range(N)]  # d[u][v] : 辺uvのコスト(存在しないときは'inf')

    def add(self, u, v, c, directed=False):
        """
        0-indexedであることに注意
        u = from, v = to, c = cost
        directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search(self):
        # これを d[i][j]: iからjへの最短距離 にする
        # 本来無向グラフでのみ全域木を考えるが、二重辺なら有向でも行ける
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        for i in range(self.N):
            self.d[i][i] = 0
        return self.d

n,m = na()
g = WarshallFloyd(n)
abc = []

for i in range(m):
    a,b,c = na()
    g.add(a-1,b-1,c)
    abc.append([a-1,b-1,c])

dp = g.WarshallFloyd_search()

ans = 0
for a,b,c in abc:
    if dp[a][b] < c:
        ans += 1

print(ans)