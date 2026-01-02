class lheapq:
    def __init__(self, p):
        self.l = []
        if p:
            for sp in p:
                self.heappush(sp)

    def heappush(self, a):
        n = len(self.l)
        self.l.append(a)
        t = n
        while t != 0:
            if self.l[t][1] < self.l[(t - 1) // 2][1]:
                self.l[t], self.l[(t - 1) // 2] = self.l[(t - 1) // 2], self.l[t]
                t = (t - 1) // 2
            else:
                break

    def heappop(self):
        n = len(self.l)
        if n == 0:
            return [-1, 0]
        if n == 1:
            return self.l.pop()
        ret = self.l[0]
        self.l[0] = self.l.pop()
        n -= 1
        t = 0
        while t < n:
            child1 = t * 2 + 1
            child2 = t * 2 + 2
            if child1 >= n:
                break
            elif child2 >= n:
                if self.l[t][1] > self.l[child1][1]:
                    self.l[t], self.l[child1] = self.l[child1], self.l[t]
                    t = child1
                else:
                    break
            else:
                if self.l[child2][1] < self.l[child1][1]:
                    child1, child2 = child2, child1
                if self.l[t][1] > self.l[child1][1]:
                    self.l[t], self.l[child1] = self.l[child1], self.l[t]
                    t = child1
                elif self.l[t][1] > self.l[child2][1]:
                    self.l[t], self.l[child2] = self.l[child2], self.l[t]
                    t = child2
                else:
                    break
        return ret

    def isnotblank(self):
        if self.l:
            return True
        else:
            return False


def dijkstra(s, g, n):
    # グラフgの点0から点n-1までの最短距離を求める。
    # グラフは隣接行列で[[[目的地、辺の重み],[目的地、辺の重み]],[],...]
    f = [-1 for _ in range(n)]
    f[s] = 0
    q = lheapq(g[s])
    while True:
        kakutei = q.heappop()
        if kakutei[0] == -1:
            return f
        while f[kakutei[0]] != -1:
            kakutei = q.heappop()
            if kakutei[0] == -1:
                return f
        s = kakutei[0]
        f[s] = kakutei[1]
        for sg, sl in g[s]:
            if f[sg] == -1:
                q.heappush([sg, sl + f[s]])


def main():
    N, X, Y = map(int, input().split())
    g = [[] for _ in range(N)]
    for i in range(N - 1):
        g[i].append([i + 1, 1])
        g[i + 1].append([i, 1])
    g[X - 1].append([Y - 1, 1])
    g[Y - 1].append([X - 1, 1])
    res = [0 for _ in range(N)]
    for i in range(N):
        tres = dijkstra(i, g, N)
        for stres in tres:
            res[stres] += 1

    for i in range(1, N):
        print(res[i] // 2)


main()
