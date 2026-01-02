import collections


def bfs(u, n):
    global level, network
    level = [-1] * n
    deq = collections.deque()
    level[u] = 0
    deq.append(u)
    while deq:
        v = deq.popleft()
        for w, c, l in network[v]:
            if c > 0 and level[w] < 0:
                level[w] = level[v] + 1
                deq.append(w)


def dfs(u, t, f):
    global it, level, network
    if u == t:
        return f
    for i in range(it[u], len(network[u])):
        v, c, l = network[u][i]
        if c <= 0 or level[u] >= level[v]:
            continue
        d = dfs(v, t, min(f, c))
        if d <= 0:
            continue
        network[u][i][1] -= d
        network[v][l][1] += d
        it[u] = i
        return d
    it[u] = len(network[u])
    return 0


def max_flow(s, t, n):
    global it, level
    flow = 0
    while True:
        bfs(s, n)
        if level[t] < 0:
            return flow
        it = [0] * n
        while True:
            f = dfs(s, t, 1e10)
            if f > 0:
                flow += f
            else:
                break
    return flow


n, m = map(int, input().split())

network = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    network[u].append([v, c, len(network[v])])
    network[v].append([u, 0, len(network[u]) - 1])

level = [-1] * n
it = [0] * n

print(max_flow(0, n - 1, n))

