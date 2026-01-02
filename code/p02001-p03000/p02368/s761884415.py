def strongly_connected_components(E):
    N = len(E)
    postorder = []
    visited = set([])
    
    def reverse_edge(E):
        result = [[] for _ in range(len(E))]
        for v, neighbor in enumerate(E):
            for n in neighbor:
                result[n].append(v)
        return result

    def dfs(E, s):
        postorder = [] # a dfs postordering of each vertex
        nonlocal visited
        stack = [(s, -1, 0)] # (vertex, parent, status)
        while stack:
            v, p, st = stack.pop()
            if st == 0 and v not in visited: # visited v for the first time
                visited |= {v}
                n_children = 0
                for u in E[v]:
                    if u in visited:
                        continue
                    if n_children == 0:
                        stack += [(v, p, 2), (u, v, 0)]
                        n_children += 1
                    else:
                        stack += [(v, p, 1), (u, v, 0)]
                        n_children += 1
                if n_children == 0: # v is a leaf
                    postorder.append(v)
            elif st == 0 and v in visited: # the edge (v, p) is a back edge
                continue
            elif st == 1: # now searching
                continue
            else: # search finished
                postorder.append(v)
        return postorder

    for v in range(N):
        if v not in visited:
            order = dfs(E, v)
            postorder += order
    
    reverse_E = reverse_edge(E)
    
    scc = [N] * N
    visited = set([])
    k = 0
    while postorder:
        v = postorder.pop()
        if scc[v] == N:
            order = dfs(reverse_E, v)
            for u in order: scc[u] = k
            k += 1
    return scc

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    E[s].append(t)
scc = strongly_connected_components(E)
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    print(1 if scc[u] == scc[v] else 0)
