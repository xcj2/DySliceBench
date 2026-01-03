import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict
from heapq import heappop, heappush


class Dijkstra:
    """Graph input:
    {
    node:{node:cost,node:cost...},
    node:{node:cost,node:cost...},
    ...
    }
    """

    def __init__(self, graph: dict, N: int):
        self.graph = graph
        self.costs = [float("inf")] * N

    def calculate(self, start):
        queue = list()

        # step1: push the start point into the priority queue
        self.costs[start] = 0
        heappush(queue, (0, start))  # (cost,node)

        while queue:
            # step2: get the minimum cost node from unfixed node and fix the cost
            cost_from_start, min_node = heappop(queue)

            # step3: update the direct connected nodes
            for link, cost in self.graph[min_node].items():
                if cost_from_start + cost < self.costs[link]:
                    self.costs[link] = cost_from_start + cost
                    heappush(queue, (self.costs[link], link))

        return self.costs


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    graph = defaultdict(dict)
    for _ in range(n - 1):
        a, b, c = input_int_list()
        graph[a][b] = c
        graph[b][a] = c
    # dp = warshall_floyd(graph, n + 1) O(n**3) => TLD

    q, k = input_int_list()

    solver = Dijkstra(graph, n + 1)
    costs = solver.calculate(k)

    ans = []
    for _ in range(q):
        x, y = input_int_list()
        ans.append(costs[x] + costs[y])
    for i in ans:
        print(i)

    return


if __name__ == "__main__":
    main()
