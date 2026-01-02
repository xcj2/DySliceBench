from collections import deque

def read():
    return [int(i) for i in input().split()]

visited = []

def bfs(e, G):
    """ 連結じゃなければtrue. """
    n = len(G)
    visited = [False for i in range(n)]
    q = deque([0])
    visited[0] = True

    while len(q) > 0:
        cur = q.popleft()
        for dst in G[cur]:
            if sorted([cur,dst]) == sorted(e):
                continue
            if visited[dst]:
                continue
            q.append(dst)
            visited[dst] = True
    
    return sum(visited) != n


def main():
    n, m = read()
    G = [[] for j in range(n)]
    edge = []
    for i in range(m):
        a, b = read()
        a -= 1; b -= 1
        edge.append([a,b])
        G[a].append(b)
        G[b].append(a)

    cnt = 0
    for e in edge:
        cnt += bfs(e,G)
    print(cnt)

main()