import heapq
import collections

INF = 10 ** 16

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

class edge:
    def __init__(self, to, cost): self.to, self.cost = to, cost

def main():
    N = Z()
    E = collections.defaultdict(list)
    for _ in range(N-1):
        a, b, c = ZZ()
        E[a].append(edge(b, c))
        E[b].append(edge(a, c))
    Q, K = ZZ()

    def dijkstra(s):
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
                if newd[e.to] > newd[v] + e.cost:
                    newd[e.to] = newd[v] + e.cost
                    heapq.heappush(que, [newd[e.to], e.to])
        return newd

    dist = dijkstra(K)
    output = []

    for _ in range(Q):
        x, y = ZZ()
        output.append(dist[x] + dist[y])
    print(*output, sep='\n')

    return

if __name__ == '__main__':
    main()
