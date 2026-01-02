import sys
input = sys.stdin.readline

def dfs(edges, s):
    use = {s}
    stack = [s]
    while stack:
        v = stack.pop()
        for w in edges[v]:
            if w in use: continue
            use.add(w)
            stack.append(w)
    return use

def bellmanford(num_v, edges, source):
    inf = float('inf')
    dist = [inf] * num_v
    dist[source] = 0
    for i in range(num_v):
        flag = False
        for s, t, cost in edges:
            if dist[s] == inf: continue
            if dist[s] + cost < dist[t]:
                dist[t] = dist[s] + cost
                flag = True
        if not flag: break
    else:
        return False
    return dist

def main():
    N, M, P = map(int, input().split())
    G = [[] for _ in range(N)]
    G_rev = [[] for _ in range(N)]
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G_rev[b].append(a)
        edges.append((a, b, P-c))
    
    use = dfs(G_rev, N-1)
    edges = [(a, b, c) for a, b, c in edges if a in use and b in use]
    dist = bellmanford(N, edges, 0)
    if dist:
        print(max(0, -dist[N-1]))
    else:
        print(-1)

if __name__ == '__main__':
    main()