from itertools import permutations


class Graph():
    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, v):
        self.adjacency_dict[v] = []

    def add_edge(self, v1, v2):
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)

    def exists(self, path):
        for i in range(len(path)-1):
            if not path[i+1] in self.adjacency_dict[path[i]]:
                return False
        return True


def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    graph = Graph()
    for v in range(1, N+1):
        graph.add_vertex(v)
    for e in edges:
        graph.add_edge(e[0], e[1])

    count = 0
    for path in permutations(range(2, N+1)):
        path = list(path)
        path.insert(0, 1)
        if graph.exists(path):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
