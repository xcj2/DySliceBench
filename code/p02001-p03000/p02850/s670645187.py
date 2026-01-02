from collections import deque

def read():
    N = int(input().strip())
    G = [list() for _ in range(N+1)]
    H = [list() for _ in range(N+1)]
    pairs = []
    for i in range(N-1):
        a, b = list(map(int, input().strip().split()))
        G[a].append(b)
        G[b].append(a)
        H[a].append(i)
        H[b].append(i)
    return N, G, H

def paint_edges(N, G, max_edges, H):
    C = [-1 for _ in range(N-1)]
    q = deque()
    q.appendleft((1, -1))
    while(len(q) > 0):
        s, c = q.pop()
        for i in range(len(G[s])):
            t = G[s][i]
            idx = H[s][i]
            if C[idx] == -1:
                c = (c + 1) % max_edges
                C[idx] = c
                q.append((t, c))
    return C


def solve(N, G, H):
    max_edges = 0
    for i in range(N):
        max_edges = max(max_edges, len(G[i]))
    C = paint_edges(N, G, max_edges, H)
    return max_edges, C

if __name__ == '__main__':
    inputs = read()
    max_edges, C = solve(*inputs)
    print(max_edges)
    for c in C:
        print(c+1)