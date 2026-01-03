from collections import defaultdict


class Graph(object):
    """
    隣接リストによる無向グラフ
    重み無しで距離は１
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst):
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def get_nodes(self):
        return self.graph.keys()


def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    g = Graph()
    for e in ab:
        g.add_edge(e[0], e[1])

    for i in range(N):
        print(len(g.graph[i+1]))


if __name__ == "__main__":
    main()
