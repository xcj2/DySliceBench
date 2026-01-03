def add_adj(adj, k, v):
    if k not in adj:
        adj[k] = set()
    adj[k].add(v)


def all_visited(N):
    x = 0
    for i in range(N):
        x += 1 << i
    return x


def dfs(adj, cur, visited, N):
    if visited == all_visited(N):
        return 1
    cnt = 0
    for nex in adj[cur]:
        if (visited >> (nex - 1)) & 1 == 1:
            continue
        cnt += dfs(adj, nex, (visited | (1 << (nex - 1))), N)
    return cnt


def main():
    N, M = map(int, input().split())
    adj = {}
    for i in range(M):
        a, b = map(int, input().split())
        add_adj(adj, a, b)
        add_adj(adj, b, a)
    print(dfs(adj, 1, 1, N))

if __name__ == '__main__':
    main()
