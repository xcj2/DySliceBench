import sys
fin = sys.stdin.readline


def initialize_int(adj, s):
    """
    assume that all vertex in {0, 1, 2, ..., N - 1}
    """
    N = len(adj)
    MAX_NUM = float('inf')
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


N, M = [int(elem) for elem in fin().split()]
adj = [[] for _ in range(N)]
w = [[None] * N for _ in range(N)]

for _ in range(M):
    a, b, c = [int(elem) for elem in fin().split()]
    a -= 1
    b -= 1
    c *= -1
    adj[a].append(b)
    w[a][b] = c

d, parent, negative_cycle_edges = bellman_ford(adj, w, 0)
if len(negative_cycle_edges) > 0:
    # see if there's a path from 0 to this edge via DFS
    stack = [0]
    visited = set()
    visited.add(0)
    reachable_edges = set()
    while stack:
        source = stack.pop()
        for neighbor in adj[source]:
            if (source, neighbor) in negative_cycle_edges:
                reachable_edges.add((source, neighbor))
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    # see if there is a path to N - 1
    for _, target in reachable_edges:
        stack = [target]
        visited = set()
        visited.add(target)
        while stack:
            source = stack.pop()
            for neighbor in adj[source]:
                if neighbor == N - 1:
                    print("inf")
                    exit(0)
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    else:
        print(-d[N - 1])
else:
    print(-d[N - 1])
