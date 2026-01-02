import heapq


class Dijkstra:

    def __init__(self, rote_map, start_point, goal_point=None):
        self.rote_map = rote_map
        self.start_point = start_point
        self.goal_point = goal_point

    def execute(self):
        """
        :param rote_map:
        :param start_point:
        :param distance:
        :return:
        """
        num_of_city = len(self.rote_map)
        dist = [float("inf") for _ in range(num_of_city)]
        prev = [float("inf") for _ in range(num_of_city)]

        dist[self.start_point] = 0
        heap_q = []
        heapq.heappush(heap_q, (0, self.start_point))
        while len(heap_q) != 0:
            prov_cost, src = heapq.heappop(heap_q)

            if dist[src] < prov_cost:
                continue

            for dest, cost in self.rote_map[src].items():
                if cost != float("inf") and dist[dest] > dist[src] + cost:
                    dist[dest] = dist[src] + cost
                    heapq.heappush(heap_q, (dist[dest], dest))
                    prev[dest] = src
        if self.goal_point is not None:
            return self.get_path(self.goal_point, prev)
        else:
            return dist

    def get_path(self, goal, prev):
        path = [goal]
        dest = goal

        while prev[dest] != float("inf"):
            path.append(prev[dest])
            dest = prev[dest]

        return list(reversed(path))


n, m, s, t = map(int, input().split())
yen_route_map = [dict() for _ in range(n)]
snuuk_route_map = [dict() for _ in range(n)]

for i in range(m):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1
    yen_route_map[u][v] = yen_route_map[v][u] = a
    snuuk_route_map[u][v] = snuuk_route_map[v][u] = b
yen_dijkstra = Dijkstra(yen_route_map, s-1).execute()
snuuk_dijkstra = Dijkstra(snuuk_route_map, t-1).execute()

from itertools import accumulate
ans = list(accumulate([y+s for y, s in zip(yen_dijkstra, snuuk_dijkstra)][::-1],min))
[print(10**15-ans[i]) for i in range(n-1,-1,-1)]


