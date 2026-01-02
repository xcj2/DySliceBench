import sys
input = sys.stdin.readline


def max2(x,y):
    return x if x > y else y

class DiGraph:
    def __init__(self, n, decrement=True, edges=[]):
        """
        incs[p]: 頂点 p に流入するリンク数
        """
        self.n = n
        self.decrement = decrement
        self.edges = [set() for _ in range(self.n)]
        self.incs = [0]*self.n
        for _from, _to in edges:
            self.add_edge(_from,_to)

    def add_edge(self, _from, _to):
        if self.decrement:
            _from -= 1
            _to -= 1
        self.edges[_from].add(_to)
        self.incs[_to] += 1

    def topological_sort_depth(self):
        """
        :return 各作業に１日かかると仮定したときに、最短で何日かかるかを返す
        """
        next_set = {p for p, inc in enumerate(self.incs) if inc == 0}
        res = []
        depth = [1]*self.n
        while next_set:
            p = next_set.pop()
            d = depth[p] + 1
            res.append(p+self.decrement)
            for q in self.edges[p]:
                self.incs[q] -= 1
                depth[q] = max2(d, depth[q])
                if self.incs[q] == 0:
                    next_set.add(q)
        if len(res) == self.n:
            return max(depth)
        else:
            return -1

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

N = int(input())
graph = DiGraph(N*N, decrement=True)
visited = set()
for i in range(1,N+1):
    p0 = -1
    for j in map(int, input().split()):
        p = i*N + j if j > i else j*N + i
        if p0 != -1:
            graph.add_edge(p0, p)
        p0 = p
print(graph.topological_sort_depth())