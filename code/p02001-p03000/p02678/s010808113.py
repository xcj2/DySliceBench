from collections import OrderedDict, defaultdict, deque
from enum import Enum
from typing import Dict, Optional


class State(Enum):
    UNVISITED = 0
    VISITED = 1


class Node(object):
    def __init__(self, key: int) -> None:
        self.adj_nodes: Dict[int, Node] = {}  # node key: node
        self.key: int = key
        self.state = State.UNVISITED

    def __repr__(self):
        return "<Node {}>".format(self.key)

    def add_adj_node(self, key) -> None:
        if key not in self.adj_nodes.keys():
            self.adj_nodes[key] = Node(key)


class Graph:
    def __init__(self) -> None:
        self.nodes: Dict[int, Node] = {}

    def add_node(self, key) -> None:
        if key not in self.nodes.keys():
            self.nodes[key] = Node(key)

    def add_edge(self, source: int, dest) -> None:
        if not self.get_node(source):
            self.add_node(source)
        if not self.get_node(dest):
            self.add_node(dest)

        self.get_node(source).add_adj_node(dest)

    def get_node(self, key) -> Optional[Node]:
        try:
            return self.nodes[key]
        except KeyError:
            return None


class BFS:
    def __init__(self, g: Graph, start_key: int):
        self.graph = g
        self.start_key = start_key
        self.history: Dict[int, int] = {}

    def solve(self):
        n = self.graph.get_node(self.start_key)
        n.state = State.VISITED
        queue = deque()
        queue.append(n.key)
        while queue:
            n_key = queue.popleft()
            n = self.graph.get_node(n_key)

            for adj_node_key in n.adj_nodes:
                adj_node = self.graph.get_node(adj_node_key)
                if adj_node.state == State.UNVISITED:
                    self.history[adj_node_key] = n.key
                    adj_node.state = State.VISITED
                    self.visit_func(adj_node_key)
                    queue.append(adj_node_key)

    def visit_func(self, node_key):
        raise NotImplementedError


class Ans(BFS):
    def __init__(self, g, n, start_key=1):
        super().__init__(g, start_key)
        self.n = n
        self.dist = {x: -1 for x in range(1, n + 1)}
        self.dist[self.start_key] = 0

    def visit_func(self, node_key):
        if node_key != self.start_key:
            prev_dist = self.dist[self.history[node_key]]
            self.dist[node_key] = prev_dist + 1

    def show_results(self, n):
        if -1 in set(self.dist.values()):
            print("No")
            return
        print("Yes")
        for i in range(2, n + 1):
            print(self.history[i])


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    G = Graph()
    for i in range(n):
        G.add_node(i + 1)

    for _ in range(m):
        a, b, = map(int, input().split(" "))
        # print(a, b)
        G.add_edge(a, b)
        G.add_edge(b, a)

    a = Ans(G, n)
    a.solve()
    # a.show_results()
    a.show_results(n)
