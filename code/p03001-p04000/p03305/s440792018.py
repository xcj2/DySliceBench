import heapq
from collections import defaultdict

INF = 10 ** 16

class edge:
    def __init__(self, to, yen, snuuk):
        self.to = to
        self.cost = [yen, snuuk]

def main():
    mon = 10 ** 15
    N, M, S, T = (int(_) for _ in input().split())
    E = defaultdict(list)
    for _ in range(M):
        u, v, a, b = (int(_) for _ in input().split())
        E[u].append(edge(v, a, b))
        E[v].append(edge(u, a, b))

    def dijkstra(s, y):
        que = list()
        heapq.heapify(que)
        newd = [INF] * (N+1)
        newd[s] = 0
        heapq.heappush(que, [newd[s], s])

        while que:
            p = heapq.heappop(que)
            v = p[1]
            if newd[v] < p[0]: continue
            for e in E[v]:
                if newd[e.to] > newd[v] + e.cost[y]:
                    newd[e.to] = newd[v] + e.cost[y]
                    heapq.heappush(que, [newd[e.to], e.to])
        return newd

    ds = dijkstra(S, 0)
    dt = dijkstra(T, 1)
    output = []
    ret = -1
    for i in range(1, N+1)[::-1]:
        ret = max(ret, mon - (ds[i] + dt[i]))
        output.append(ret)
    print(*output[::-1], sep='\n')
    return

if __name__ == '__main__':
    main()
