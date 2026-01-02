import sys
from collections import OrderedDict

input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)


class Graph():
    def __init__(self):
        self.adjacency_dict = {}
        self.counter_dict = OrderedDict()

    def add_vertex(self, v):
        self.adjacency_dict[v] = set()
        self.counter_dict[v] = 0

    def add_edge(self, v1, v2):
        self.adjacency_dict[v1].add(v2)
        self.adjacency_dict[v2].add(v1)

    def add_count(self, v, count):
        self.counter_dict[v] += count

    def dfs_stack(self, start):
        stack = [start]
        visited = set()

        parent_vertex = 0
        while stack:
            current_vertex = stack.pop()
            visited.add(current_vertex)
            for v in self.adjacency_dict[current_vertex]:
                if v not in visited and v != parent_vertex:
                    self.counter_dict[v] += self.counter_dict[current_vertex]
                    stack.append(v)
            parent_vertex = current_vertex

    def dfs_rec(self, v, pv):
        for nv in self.adjacency_dict[v]:
            if nv != pv:
                self.counter_dict[nv] += self.counter_dict[v]
                self.dfs_rec(nv, v)

    def print_counters(self):
        print(*self.counter_dict.values())


def main():
    n, q = map(int, input().split())
    tree = Graph()
    for v in range(1, n+1):
        tree.add_vertex(v)
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree.add_edge(a, b)
    for _ in range(q):
        p, x = map(int, input().split())
        tree.add_count(p, x)
    tree.dfs_stack(1)
    # tree.dfs_rec(1, 0)
    tree.print_counters()


if __name__ == "__main__":
    main()
