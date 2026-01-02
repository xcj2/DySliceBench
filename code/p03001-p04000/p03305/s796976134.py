from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


class Dijkstra:
    def __init__(self):
        self.edge = defaultdict(list)

    def add(self, u, v, d):
        self.edge[u].append([v, d])
        self.edge[v].append([u, d])

    def search(self, start):
        distance = defaultdict(lambda: float("inf"))
        distance[start] = 0
        queue = []
        heappush(queue, (0, start))
        seen = set()
        while queue:
            k, u = heappop(queue)
            if u in seen:
                continue
            seen.add(u)

            for v, d in self.edge[u]:
                if v in seen:
                    continue
                new_d = k + d
                if distance[v] > new_d:
                    distance[v] = new_d
                    heappush(queue, (new_d, v))
        return distance


n, m, s, t = map(int, input().split())
uvab = [list(map(int, input().split())) for _ in range(m)]
graph1 = Dijkstra()
graph2 = Dijkstra()

for u, v, a, b in uvab:
    graph1.add(u, v, a)
    graph2.add(u, v, b)

result_a = graph1.search(s)
result_b = graph2.search(t)
ans_list = [float('inf')]

for i in range(n, 0, -1):
    cur = result_a[i] + result_b[i]
    if cur > ans_list[-1]:
        cur = ans_list[-1]
    ans_list.append(cur)

for ans in ans_list[n:0:-1]:
    print(10 ** 15 - ans)
