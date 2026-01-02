
def findpath(v, t, edges, flow, visited):
    visited.add(v)
    for u in edges[v]:
        if u in visited:
            continue
        if flow[(v, u)] == 1:
            continue
        if u == t:
            return [v, t]
        path = findpath(u, t, edges, flow, visited)
        if path:
            return [v] + path
    return None

def max_match(R, B, edges):
    s, t = 'S', 'T'
    flow = {}
    for b in B:
        flow[(b, t)] = 0
        edges[b].append(t)  # add edge b -> t

    for r in R:
        flow[(s, r)] = 0
        for b in edges[r]:
            flow[(r, b)] = 0
            flow[(b, r)] = 1

    for r in R:
        if flow[(s, r)] == 1:
            continue
        path = findpath(r, t, edges, flow, set())
        if not path:
            continue
        path = [s] + path
        for u, v in zip(path, path[1:]):
            flow[(u, v)] = 1
            flow[(v, u)] = 0
    return flow

def solve(R, B, edges):
    flow = max_match(R, B, edges)
    match = 0
    for r in R:
        for b in edges[r]:
            match += flow[(r, b)]
    return match

N = int(input())
R = [tuple([int(x) for x in input().split()]) for _ in range(N)]
B = [tuple([int(x) for x in input().split()]) for _ in range(N)]
edges = {r:[] for r in R+B}

for r in R:
    rx, ry = r
    for b in B:
        bx, by = b
        if rx < bx and ry < by:
            edges[r].append(b)
            edges[b].append(r)

print(solve(R, B, edges))
