import heapq
class Dijkstra:
    INF = 10**18
    threshold = 10**9

    def __init__(self, N):
        self.MAX_V = N + 1
        self.dist = [self.INF] * self.MAX_V
        self.G = [[] for _ in range(self.MAX_V)]

    def insert(self, X, Y, cost): self.G[X].append(cost * self.threshold + Y)

    def dijkstra(self, st):
        q = []
        heapq.heappush(q, st)
        self.dist[st] = 0

        while len(q):
            p = heapq.heappop(q)
            cost = p // self.threshold
            node = p - cost * self.threshold
            if cost > self.dist[node]: continue
            for to in self.G[node]:
                to_cost = to // self.threshold
                to_node = to - to_cost * self.threshold
                to_cost += self.dist[node]
                if self.dist[to_node] > to_cost:
                    self.dist[to_node] = to_cost
                    heapq.heappush(q, to_cost * self.threshold + to_node)

def main():
    h, w = map(int, input().split())
    sh, sw = map(int, input().split())
    eh, ew = map(int, input().split())

    sh -= 1
    sw -= 1
    eh -= 1
    ew -= 1

    S = [input() for _ in range(h)]

    di = Dijkstra(h*w)
    for x in range(h):
        for y in range(w):
            if S[x][y] == '#': continue
            for i in range(-2, 3):
                for j in range(-2, 3):
                    X = x + i
                    Y = y + j
                    if X < 0 or Y < 0 or X >= h or Y >= w or S[X][Y] == '#': continue
                    D = abs(i) + abs(j)

                    if D == 1: di.insert(x * w + y, X * w + Y, 0)
                    if D >= 2: di.insert(x * w + y, X * w + Y, 1)

    di.dijkstra(sh * w + sw)
    ans = di.dist[eh * w + ew]
    if ans == 10**18: print(-1)
    else: print(ans)

main()