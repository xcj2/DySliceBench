import queue


class Edge:
    def __init__(self, _to, _cost):
        self.to = _to
        self.cost = _cost


def bellman(n, graph, start):
    dist = [0 if i == start else float('inf') for i in range(n)]

    for i in range(n):
        for v in range(n):
            for e in graph[v]:
                if dist[v] == float('inf') or dist[e.to] <= dist[v] + e.cost:
                    continue

                dist[e.to] = dist[v] + e.cost

                if i == n - 1:
                    return None

    return dist


def main():
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        data = list(map(int, input().split()))

        graph[data[0]].append(Edge(data[1], data[2]))

    ans = bellman(n, graph, s)

    if ans is None:
        print("NEGATIVE CYCLE")
    else:
        for i in range(n):
            print(ans[i] if ans[i] != float('inf') else "INF")
        return


if __name__ == '__main__':
    main()

