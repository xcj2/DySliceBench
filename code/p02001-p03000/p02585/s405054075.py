class Unionfind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root (self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def connect(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def isConnect(self, x):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]

def solve():
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x) - 1, input().split()))
    C = list(map(int, input().split()))
    INF = 10 ** 18
    dp = [[-INF] * (N + 1) for i in range(N)]
    ans = -INF
    uf = Unionfind(N)
    for i in range(N):
        dp[i][0] = 0
        now = i
        for j in range(min(N, K)):
            now = P[now]
            uf.connect(i, now)
            dp[i][j + 1] = dp[i][j] + C[now]
            ans = max(ans, dp[i][j + 1])
    for i in range(N):
        M = uf.size(i)
        if dp[i][M] < 0:
            continue
        roop = K // M
        move = K % M
        if move == 0:
            roop -= 1
            move = M
        for j in range(move):
            ans = max(ans, dp[i][M] * roop + dp[i][j + 1])
    return ans

print(solve())
