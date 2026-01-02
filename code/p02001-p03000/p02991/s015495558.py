import heapq


class Dijkstra:

    def __init__(self, rote_map, start_point, goal_point=None):
        self.rote_map = rote_map
        self.start_point = start_point
        self.goal_point = goal_point

    def execute(self):
        num_of_city = 3 * 10 ** 5 + 10
        dist = [float("inf") for _ in range(num_of_city)]
        prev = [float("inf") for _ in range(num_of_city)]

        dist[self.start_point] = 0
        heap_q = []
        heapq.heappush(heap_q, (0, self.start_point))
        route_count = [0 for _ in range(num_of_city)]
        route_count[self.start_point] = 1
        while len(heap_q) != 0:
            prev_cost, src = heapq.heappop(heap_q)

            if dist[src] < prev_cost:
                continue

            for dest, cost in self.rote_map[src].items():
                if cost != float("inf") and dist[dest] > dist[src] + cost:
                    dist[dest] = dist[src] + cost
                    heapq.heappush(heap_q, (dist[dest], dest))
                    prev[dest] = src
                if dist[dest] == dist[src] + cost:
                    route_count[dest] += route_count[src]

        if self.goal_point is not None:
            return self._get_path(self.goal_point, prev)
        else:
            return dist, route_count

    def _get_path(self, goal, prev):
        path = [goal]
        dest = goal

        while prev[dest] != float("inf"):
            path.append(prev[dest])
            dest = prev[dest]

        return list(reversed(path))


N, M = map(int, input().split())
from collections import defaultdict

graph = defaultdict(dict)
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v + N] = 1
    graph[u + N][v + 2 * N] = 1
    graph[u + 2 * N][v] = 1
S, T = map(int, input().split())
S -= 1
T -= 1
dj = Dijkstra(graph, S)

dist, _ = dj.execute()
if dist[T] % 3 == 0:
    print(dist[T] // 3)
else:
    print(-1)
