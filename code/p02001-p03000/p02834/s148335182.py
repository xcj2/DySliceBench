from collections import deque

def read():
    N, u, v = list(map(int, input().strip().split()))
    G = [list() for i in range(N+1)]
    for i in range(N-1):
        a, b = list(map(int, input().strip().split()))
        G[a].append(b)
        G[b].append(a)
    return N, u, v, G

def bfs(N, G, start):
    depth = [-1 for i in range(N+1)]
    depth[start] = 0
    q = deque()
    q.append(start)
    while(len(q) > 0):
        s = q.popleft()
        for t in G[s]:
            if depth[t] == -1:
                depth[t] = depth[s] + 1
                q.append(t)
    return depth

def solve(N, u, v, G):
    depth_u = bfs(N, G, u)
    depth_v = bfs(N, G, v)
    most_deepest_node = u
    for i in range(1, N+1):
        if depth_u[i] < depth_v[i]:
            if depth_v[i] > depth_v[most_deepest_node]:
                most_deepest_node = i
    neighbor_node = G[most_deepest_node][0]
    step_u = depth_u[neighbor_node]
    step_v = depth_v[neighbor_node]
    return step_v

if __name__ == '__main__':
    inputs = read()
    print('%d' % solve(*inputs))
