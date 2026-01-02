
# 全方位木DP

def resolve():
    def dfs1(r_topo, par):
        for idx in reversed(r_topo):
            for (to, cost) in G[idx]:
                if to == par[idx]:
                    continue
                dist[idx] = max(dist[idx], dist[to] + cost)

    def dfs2(idx, d_par, par):
        stack = [(idx, d_par, par)]
        while stack:
            idx, d_par, par = stack.pop()
            d_child = []
            d_child.append((0, -1))
            for (to, cost) in G[idx]:
                if to == par:
                    d_child.append((d_par + cost, to))
                else:
                    d_child.append((dist[to] + cost, to))
            d_child.sort(reverse=True)
            ans[idx] = d_child[0][0] + d_child[1][0]
            for (to, cost) in G[idx]:
                if to == par:
                    continue
                nx_d_par = d_child[d_child[0][1] == to][0]
                stack.append((to, nx_d_par, idx))

    N = int(input())
    if N == 1:
        return print(0)

    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))

    topo = []
    P = [-1] * N
    node = [0]
    while node:
        s = node.pop()
        topo.append(s)
        for (to, cost) in G[s]:
            if to == P[s]:
                continue
            P[to] = s
            node.append(to)

    dist = [0] * N
    ans = [0] * N
    dfs1(topo, P)
    dfs2(0, 0, -1)
    print(max(ans))


if __name__ == '__main__':
    resolve()
