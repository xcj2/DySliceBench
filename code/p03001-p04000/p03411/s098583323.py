#!python3

INF = 10 ** 15


# input
N = int(input())
a, b, c, d = [None] * N, [None] * N, [None] * N, [None] * N
for i in range(N):
    a[i], b[i] = list(map(int, input().split()))
for i in range(N):
    c[i], d[i] = list(map(int, input().split()))


class MaxFlow():

    def __init__(self, n):
        self.n = n
        self.c = [[0] * n for _ in range(n)]
        self.visit = [False] * n

    def add_link(self, x, y, capa):
        self.c[x][y] += capa
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        self.visit[v] = True
        
        for i in range(self.n):
            if self.visit[i] or self.c[v][i] == 0:
                continue
            d = self.dfs(i, t, min(f, self.c[v][i]))
            if d > 0:
                self.c[v][i] -= d
                self.c[i][v] += d
                return d
                
        return 0

    
    def max_flow(self, s, t):
        ans = 0
        while True:
            f = self.dfs(s, t, INF)
            self.visit = [False] * self.n
            if f == 0:
                return ans
            else:
                ans += f
        

def main():
    w = MaxFlow(2 * N + 2)
    for i in range(N):
        w.add_link(0, i + 1, 1)
        w.add_link(N + i + 1, 2 * N + 1, 1)
        for j in range(N):
            if a[i] < c[j] and b[i] < d[j]:
                w.add_link(i + 1, N + j + 1, 1)
    
    ans = w.max_flow(0, 2 * N + 1)
    print(ans)


if __name__ == "__main__":
    main()
