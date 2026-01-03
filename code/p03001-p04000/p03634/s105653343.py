from collections import deque


def main():
    n = int(input())
    tree = AdjacentListGraph([Vertex() for _ in range(n)])
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        tree.add_edge(a - 1, b - 1, c)
        tree.add_edge(b - 1, a - 1, c)
    q, k = map(int, input().split())
    distances = distances_from(tree, k - 1)
    # print(distances)
    answers = []
    for _ in range(q):
        x, y = map(int, input().split())
        answers.append(distances[x - 1] + distances[y - 1])
    print("\n".join(map(str, answers)))


def distances_from(
    graph: "Graph", from_: int, break_if=lambda node: False
) -> "List[int]":
    distances = [None for _ in range(graph.size)]
    distances[from_] = 0
    queue = deque([from_])
    while queue:
        node = queue.popleft()
        if break_if(node):
            break
        curDist = distances[node]
        for edge in graph.edges_from(node):
            if distances[edge.to] is not None:
                continue
            delta = edge.weight if edge.weight else 0
            distances[edge.to] = curDist + delta
            queue.append(edge.to)
    return distances


class Vertex:
    def __init__(self, data=None):
        self.data = data
        self.edges = []

    def add_edge(self, to, weight=None):
        self.edges.append(Edge(to, weight))

    def remove_edge(self, to: int) -> bool:
        for i, edge in enumerate(self.edges):
            if edge.to == to:
                del self.edges[i]
                return True
        return False


class Edge:
    def __init__(self, to, weight=None):
        self.to = to
        self.weight = weight


class AdjacentListGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.size = len(vertices)

    def get_weight(self, from_: int, to: int):
        for edge in self.vertices[from_].edges:
            if edge.to == to:
                return edge.weight
        return None

    def edges_from(self, from_: int):
        return self.vertices[from_].edges

    def add_edge(self, from_: int, to: int, weight=None) -> bool:
        return self.vertices[from_].add_edge(to, weight)

    def remove_edge(self, from_: int, to: int) -> bool:
        return self.vertices[from_].remove_edge(to)

    def is_adjacent(self, from_: int, to: int) -> bool:
        return to in {edge.to for edge in self.edges_from(from_)}


if __name__ == "__main__":
    main()
