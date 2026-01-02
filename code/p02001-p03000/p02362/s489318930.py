import sys
fin = sys.stdin.readline


MAX_NUM = float('inf')

def initialize_int(adj, s):
    """
    assume that all vertex in {0, 1, 2, ..., N - 1}
    """
    N = len(adj)
    d = [MAX_NUM] * N
    d[s] = 0
    parent = [None] * N
    return d, parent


def relax(d, w, source_v, target_v, parent):
    new_cost = d[source_v] + w[source_v][target_v]
    if new_cost < d[target_v]:
        d[target_v] = new_cost
        parent[target_v] = source_v


# Even if a negative weight exists, bellman-ford can find shortest paths.
# it also detects negative cycles,
# but not every edges that consist the negative cycles is stored.
# time complexity: O(VE + (V^2))
def bellman_ford(adj, w, s):
    d, parent = initialize_int(adj, s)

    # calculate shortest paths
    for _ in range(len(adj)):
        for vertex in range(len(adj)):
            for neighbor in adj[vertex]:
                relax(d, w, vertex, neighbor, parent)

    # detects negative cycles if exist
    negative_cycle_edges = set()
    for vertex in range(len(adj)):
        for neighbor in adj[vertex]:
            if d[neighbor] > d[vertex] + w[vertex][neighbor]:
                negative_cycle_edges.add((vertex, neighbor))
    return d, parent, negative_cycle_edges



V, E, r = [int(elem) for elem in fin().split()]
adj = [[] for _ in range(V)]
w = [[None] * V for _ in range(V)]
for _ in range(E):
    s, t, d = [int(elem) for elem in fin().split()]
    adj[s].append(t)
    w[s][t] = d

d, parent, negative_cycle_edges = bellman_ford(adj, w, r)
if len(negative_cycle_edges) > 0:
    print("NEGATIVE CYCLE")
else:
    for i in range(V):
        print("INF") if d[i] == MAX_NUM else print(d[i])


