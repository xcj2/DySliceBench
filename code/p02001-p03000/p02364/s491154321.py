import sys
fin = sys.stdin.readline
from heapq import heapify, heappop, heappush


class UnionFind(object):
    def __init__(self, N):
        self.__root = list(range(N))
    

    def root(self, x):
        if self.__root[x] == x:
            return x
        else:
            # root abbreviation
            self.__root[x] = self.root(self.__root[x])
            return self.__root[x]

    
    def same(self, x, y):
        return self.root(x) == self.root(y)


    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return
        self.__root[y] = x
        return


# assuming that the vertices are 0, 1, ..., N - 1
# time complexity: O(ElgE)
# space complexity: O(E)
def prim(adj, w):
    num_vertices = len(adj)
    # initialize
    min_cost = [float('inf')] * num_vertices
    min_cost[0] = 0
    used = [False] * num_vertices
    priority_queue = [(0, 0)]
    total_cost = 0

    while priority_queue:
        cost, vertex = heappop(priority_queue)
        if cost > min_cost[vertex] or used[vertex]:
            continue
        used[vertex] = True
        total_cost += cost

        for neighbor in adj[vertex]:
            cost_v_to_n = w[vertex][neighbor]
            if min_cost[neighbor] > cost_v_to_n:
                min_cost[neighbor] = cost_v_to_n
                heappush(priority_queue, (cost_v_to_n, neighbor))

    return total_cost


# input should be [(s1, t1, cost1), (s2, t2, cost2), ...]
# time complexity: O(ElgV)
# space complexity: O(V)
def kruskal(edges_with_cost, num_vertices):
    # num_edges = len(edges_with_cost)
    edges_with_cost.sort(key=lambda x: x[-1])
    uf = UnionFind(num_vertices)
    total_cost = 0
    for source, target, cost in edges_with_cost:
        if not uf.same(source, target):
            uf.unite(source, target)
            total_cost += cost
    
    return total_cost



V, E = [int(elem) for elem in fin().split()]
edges_with_cost = []
for _ in range(E):
    s, t, w = [int(elem) for elem in fin().split()]
    edges_with_cost.append((s, t, w))

print(kruskal(edges_with_cost, V))

