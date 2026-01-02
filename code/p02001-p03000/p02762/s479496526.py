import collections


def dfs(graph, start):
    visited = set()
    stack = [start]
 
    while stack:
        v = stack.pop()
        if v not in visited:
            stack.extend(graph[v])
            visited.add(v)
            yield v

def read_graph(nodes, edges):
    graph = [set() for _ in range(nodes)]
    for _ in range(edges):
        a, b = (int(x) - 1 for x in input().split())
        graph[a].add(b)
        graph[b].add(a)
 
    return graph

N, M, K = map(int, input().split())

friends = read_graph(N, M)
blockings = read_graph(N, K)

candidates = [None for _ in range(N)]
for i in range(N):
    if candidates[i] is not None:
        continue

    s = set()
    for j in dfs(friends, i):
        s.add(j)
        candidates[j] = s

def num_suggestions(i):
    return len(candidates[i]) - len(friends[i]) - len(blockings[i].intersection(candidates[i])) - 1

print(
    " ".join(
        str(num_suggestions(i)) for i in range(N)
    )
)
