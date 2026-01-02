import sys
input = sys.stdin.buffer.readline


class DiGraph:
    def __init__(self, n, decrement=True, destroy=False, edges=[]):
        """
        incs[p]: 頂点 p に流入するリンク数
        """
        self.n = n
        self.decrement = decrement
        self.destroy = destroy
        self.edges = [set() for _ in range(self.n)]
        self.incs = [0]*self.n
        for x, y in edges:
            self.add_edge(x,y)

    def add_edge(self, x, y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add(y)
        self.incs[y] += 1

    def topological_sort(self):
        next_set = {p for p, inc in enumerate(self.incs) if inc == 0}
        res = []
        while next_set:
            p = next_set.pop()
            res.append(p+self.decrement)
            for q in self.edges[p]:
                self.incs[q] -= 1
                if self.incs[q] == 0:
                    next_set.add(q)
        return res

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.DiGraph()
        for x in range(self.n):
            for y in self.edges[x]:
                G.add_edge(x + self.decrement, y + self.decrement)

        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        plt.axis("off")
        plt.show()


################################################################################

def main():
    N, M = map(int, input().split())

    M = N - 1 + M
    graph = DiGraph(N, decrement=True, destroy=True)
    for _ in range(M):
        A, B = map(int, input().split())
        graph.add_edge(A, B)

    res = [0]*N
    for p in graph.topological_sort():
        for q in graph.edges[p-1]:
            res[q] = p
    print(*res, sep="\n")

if __name__ == '__main__':
    main()
