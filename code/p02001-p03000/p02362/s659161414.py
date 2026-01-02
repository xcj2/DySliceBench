V, E, r = map(int, input().split())

INF = 2 << 21
G, dist = [None for i in range(E)], [INF for j in range(V)]


class Edge:
    def __init__(self, f, t, cost):
        self.f = f
        self.t = t
        self.cost = cost


def bellman_ford(s):
    dist[s] = 0
    for i in range(V):
        for j in range(E):
            e = G[j]
            if dist[e.f] < INF and dist[e.f] + e.cost < dist[e.t]:
                dist[e.t] = dist[e.f] + e.cost

                if i == V - 1:
                    return True

    return False


def main():
    for i in range(E):
        s, t, d = map(int, input().split())
        G[i] = Edge(s, t, d)

    c = bellman_ford(r)

    if c:
        print("NEGATIVE CYCLE")
    else:
        for i in range(V):
            if dist[i] == INF:
                print("INF")
            else:
                print(dist[i])


if __name__ == '__main__':
    main()

