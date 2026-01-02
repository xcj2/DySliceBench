import sys
fin = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush


class Vertex(object):
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance


    def __lt__(self, other_vertex):
        return self.distance < other_vertex.distance
    

    def __le__(self, other_vertex):
        return self.distance <= other_vertex.distance
    

    def __gt__(self, other_vertex):
        return self.distance > other_vertex.distance
    

    def __ge__(self, other_vertex):
        return self.distance >= other_vertex.distance


def initialize(adj, s):
    MAX_NUM = float('inf')
    parent = {s: None}
    d = {vertex: MAX_NUM for vertex in adj.keys()}
    d[s] = 0
    return d, parent


# Dijkstra can work using a minheap which does not have decrease_key.
# and also we do not have to implement Vertex class.
# Instead, we can use (distance, vertex).
# in this case, the time it takes is O(ElgE).
# E is at most O(V^2), thus O(ElgE) = O(ElgV).
def dijkstra_simple(adj, w, s):
    d, parent = initialize(adj, s)
    priority_queue = []
    heappush(priority_queue, (d[s], s))
    while priority_queue:
        distance, source = heappop(priority_queue) 
        for neighbor in adj[source]:
            new_distance = distance + w[(source, neighbor)]
            if new_distance < d[neighbor]:
                d[neighbor] = new_distance
                parent[neighbor] = source
                heappush(priority_queue, (new_distance, neighbor))
    return d


n, m, s, t = [int(elem) for elem in fin().split(' ')]
adj = defaultdict(list)
yen_weights = dict()
snuuk_weights = dict()
for _ in range(m):
    u, v, a, b = [int(elem) for elem in fin().split(' ')]
    for v1, v2 in [(u, v), (v, u)]:
        adj[v1].append(v2)
        yen_weights[(v1, v2)] = a
        snuuk_weights[(v1, v2)] = b

d_yen = dijkstra_simple(adj, yen_weights, s)
d_snuuk = dijkstra_simple(adj, snuuk_weights, t)
min_cost = float('inf')
min_cost_after_each_year_reversed = []
for vertex in range(n, 0, -1):
    min_cost = min(min_cost, d_yen[vertex] + d_snuuk[vertex])
    min_cost_after_each_year_reversed.append(min_cost)

initial_money = 10**15
print(*(initial_money - cost for cost in reversed(min_cost_after_each_year_reversed)), sep='\n')
