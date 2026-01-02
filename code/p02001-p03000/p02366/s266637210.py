import sys
readline = sys.stdin.readline


sys.setrecursionlimit(10**7)
class LowLinks:
    def __init__(self, edges, edges_num:int):
        """edges[u]: all vertexes connected with vertex 'u'
        edges_num: number of edges of graph
        the root of DFS-tree is vertex 0
        """
        self.edges = edges
        self.V = len(edges)
        self.order = [-1]*V
        self.low = [float('inf')]*V
        self.bridges = []
        # if degreee(root) > 1 and graph is tree: root is articulation
        self.articulations = []
        if len(edges[0]) > 1 and edges_num == self.V-1:
            self.articulations.append(0)
        self.k = 0

    def build(self):
        self.dfs(0, 0)

    def get_bridges(self)->tuple:
        return self.bridges

    def get_articulations(self)->tuple:
        return self.articulations

    def dfs(self, v:int, prev:int):
        self.order[v] = self.k
        self.k += 1
        self.low[v] = self.order[v]
        is_articulation = False
        for to in self.edges[v]:
            if self.order[to] < 0: # not visited
                self.dfs(to, v)
                self.low[v] = min(self.low[v], self.low[to])
                if self.low[v] < self.low[to]:
                    self.bridges.append((v, to))
                is_articulation |= self.order[v] <= self.low[to]
            elif to != prev:
                self.low[v] = min(self.low[v], self.order[to])
        if v>0 and is_articulation:
            self.articulations.append(v)

if __name__ == "__main__":
    V,E = map(int, readline().split())
    edges = [[] for _ in range(V)]
    for _ in range(E):
        s,t = map(int, readline().split())
        edges[s].append(t)
        edges[t].append(s)
    lowlinks = LowLinks(edges, E)
    lowlinks.build()
    articulations = lowlinks.get_articulations()
    if articulations:
        print(*sorted(articulations), sep="\n")

