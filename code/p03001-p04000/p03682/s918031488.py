import sys
fin = sys.stdin.readline
from heapq import heappop, heappush


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
# if V^2 >> E, use a hashmap representation of w
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
            cost_v_to_n = w[(vertex, neighbor)]
            if min_cost[neighbor] > cost_v_to_n:
                min_cost[neighbor] = cost_v_to_n
                heappush(priority_queue, (cost_v_to_n, neighbor))

    return total_cost


# input should be [(s1, t1, cost1), (s2, t2, cost2), ...]
# time complexity: O(ElgV)
# space complexity: O(E)
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


N = int(fin())
coords = [[int(elem) for elem in fin().split()] + [i] for i in range(N)]

edges_with_cost = []
# sort coords in increasing order of x
coords.sort(key=lambda x: x[0])
for i, (x, _, vertex) in enumerate(coords[:-1]):
    next_x, _, next_vertex = coords[i + 1]
    weight = next_x - x
    edges_with_cost.append((vertex, next_vertex, weight))
    edges_with_cost.append((next_vertex, vertex, weight))


# sort coods in increasing order of y
coords.sort(key=lambda x: x[1])
for i, (_, y, vertex) in enumerate(coords[:-1]):
    _, next_y, next_vertex = coords[i + 1]
    weight = next_y - y
    edges_with_cost.append((vertex, next_vertex, weight))
    edges_with_cost.append((next_vertex, vertex, weight))

print(kruskal(edges_with_cost, N))

# adj = [set() for _ in range(N)]
# w = {}
# # sort coords in increasing order of x
# coords.sort(key=lambda x: x[0])
# for i, (x, _, vertex) in enumerate(coords[:-1]):
#     next_x, _, next_vertex = coords[i + 1]
#     adj[vertex].add(next_vertex)
#     adj[next_vertex].add(vertex)
#     weight = next_x - x
#     if (vertex, next_vertex) not in w or w[(vertex, next_vertex)] > weight:
#         w[(vertex, next_vertex)] = weight
#     if (next_vertex, vertex) not in w or w[(next_vertex, vertex)] > weight:
#         w[(next_vertex, vertex)] = weight

# # sort coods in increasing order of y
# coords.sort(key=lambda x: x[1])
# for i, (_, y, vertex) in enumerate(coords[:-1]):
#     _, next_y, next_vertex = coords[i + 1]
#     adj[vertex].add(next_vertex)
#     adj[next_vertex].add(vertex)
#     weight = next_y - y
#     if (vertex, next_vertex) not in w or w[(vertex, next_vertex)] > weight:
#         w[(vertex, next_vertex)] = weight
#     if (next_vertex, vertex) not in w or w[(next_vertex, vertex)] > weight:
#         w[(next_vertex, vertex)] = weight

# print(prim(adj, w))

