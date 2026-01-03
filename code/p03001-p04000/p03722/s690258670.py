N, M = map(int, input().split())

INF = 2 << 40
G, dist = [None for i in range(M)], [INF for j in range(N)]


class Edge:
    def __init__(self, f, t, cost):
        self.f = f
        self.t = t
        self.cost = cost


def bellman_ford(s):
    dist[s] = 0
    for i in range(2*N):
        for j in range(M):
            e = G[j]
            if dist[e.f] < INF and dist[e.f] + e.cost < dist[e.t]:
                dist[e.t] = dist[e.f] + e.cost

                if i >= N - 1 and (e.t == N - 1 or e.f == N - 1):
                    return True

    return False


def main():
    for i in range(M):
        a, b, c = map(int, input().split())
        G[i] = Edge(a-1, b-1, -c)

    c = bellman_ford(0)

    if c:
        print("inf")
    else:
        print(-dist[N-1])


if __name__ == '__main__':
    main()
