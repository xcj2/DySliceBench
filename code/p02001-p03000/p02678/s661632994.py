from sys import stdin
from collections import deque, Counter, defaultdict
import heapq

INF = int(1e10)
MOD = int(1e9 + 7)

def input():
    return stdin.readline()[:-1]

class Dijkstra:
    def __init__(self, rote_map, start_point, goal_point=None):
        self.rote_map = rote_map
        self.start_point = start_point
        self.goal_point = goal_point

    def execute(self):
        num_of_city = len(self.rote_map)
        dist = [float("inf") for _ in range(num_of_city)]
        prev = [float("inf") for _ in range(num_of_city)]

        dist[self.start_point] = 0
        heap_q = []
        heapq.heappush(heap_q, (0, self.start_point))
        while len(heap_q) > 0:
            prev_cost, src = heapq.heappop(heap_q)

            if dist[src] < prev_cost:
                continue

            for dest, cost in self.rote_map[src].items():
                if cost != float("inf") and dist[dest] > dist[src] + cost:
                    dist[dest] = dist[src] + cost
                    heapq.heappush(heap_q, (dist[dest], dest))
                    prev[dest] = src
        return prev

    def get_path(self, goal, prev):
        path = [goal]
        dest = goal

        while prev[dest] != float("inf"):
            path.append(prev[dest])
            dest = prev[dest]

        return list(reversed(path))

def main():
    from builtins import int, map
    n, m = map(int,input().split())
    route_map = [dict() for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        route_map[u][v] = 1
        route_map[v][u] = 1

    prev = Dijkstra(route_map, 0).execute()
    print("Yes")
    for i in range(1, n):
        print(prev[i] + 1)

if __name__ == '__main__':
    main()