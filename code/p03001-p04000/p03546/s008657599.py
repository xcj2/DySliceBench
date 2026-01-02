from heapq import heappop, heappush
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


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


def main():
    h, w = input_int_list()

    G = defaultdict(dict)
    for i in range(10):
        line = input_int_list()
        for j in range(10):
            G[j][i] = line[j]

    # 1へ変換するコストをダイクストラ法で求める
    dijkstra = Dijkstra(G, 10)
    costs = dijkstra.calculate(1)

    cnts = defaultdict(int)
    for _ in range(h):
        line = input_int_list()
        for n in line:
            cnts[n] += 1

    ans = 0
    for k, v in cnts.items():
        if k == -1 or k == 1:
            continue
        ans += costs[k] * v

    print(ans)
    return


if __name__ == "__main__":
    main()
