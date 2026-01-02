class lheapq():
    # 最小値を取り出す優先度付きキュー
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
            if self.l[t][1] < self.l[(t-1)//2][1]:
                self.l[t], self.l[(t-1)//2] = self.l[(t-1)//2], self.l[t]
                t = (t-1)//2
            else:
                break

    def heappop(self):
        n = len(self.l)
        if n == 0:
            return (-1, 0)
        if n == 1:
            return self.l.pop()
        ret = self.l[0]
        self.l[0] = self.l.pop()
        n -= 1
        t = 0
        while t < n:
            child1 = t*2+1
            child2 = t*2+2
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


def dijkstra(s, N, e):
    INF = "INF"
    res = [INF for _ in range(N)]
    q = lheapq([(s, 0)])
    while q.isnotblank():
        while q.isnotblank():
            des, dis = q.heappop()
            if res[des] == INF:
                res[des] = dis
                break
        for se in e[des]:
            if res[se[0]] == INF:
                q.heappush((se[0], se[1]+res[des]))
    return res


N, M, S = map(int, input().split())
g = [[] for _ in range(N)]
for j in range(M):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
print("\n".join(map(str, dijkstra(S, N, g))))

