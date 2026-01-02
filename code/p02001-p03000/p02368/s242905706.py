mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    from collections import deque

    # compressed[v]: 縮約後のグラフで縮約前のvが属する頂点
    # num: 縮約後のグラフの頂点数
    def SCC(adj, adj_rev):
        N = len(adj) - 1
        seen = [0] * (N + 1)
        compressed = [0] * (N + 1)
        order = []

        for v0 in range(1, N + 1):
            if seen[v0]:
                continue
            st = deque()
            st.append(v0)
            while st:
                v = st.pop()
                if v < 0:
                    order.append(-v)
                else:
                    if seen[v]:
                        continue
                    seen[v] = 1
                    st.append(-v)
                    for u in adj[v]:
                        st.append(u)

        #print(order)
        seen = [0] * (N + 1)
        num = 0
        for v0 in reversed(order):
            if seen[v0]:
                continue
            num += 1
            st = deque()
            st.append(v0)
            seen[v0] = 1
            compressed[v0] = num
            #print(v0, num)
            while st:
                v = st.pop()
                for u in adj_rev[v]:
                    if seen[u]:
                        continue
                    #print([v, u])
                    seen[u] = 1
                    compressed[u] = num
                    st.append(u)

        return num, compressed

    # 縮約後のグラフを構築
    # 先にSCC()を実行してnum, compressedを作っておく
    def construct(adj, num, compressed):
        N = len(adj) - 1
        adj_compressed = [set() for _ in range(num + 1)]
        for v in range(1, N + 1):
            v_cmp = compressed[v]
            for u in adj[v]:
                u_cmp = compressed[u]
                if v_cmp != u_cmp:
                    adj_compressed[v_cmp].add(u_cmp)
        return adj_compressed

    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    adj_rev = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        a += 1
        b += 1
        adj[a].append(b)
        adj_rev[b].append(a)

    NN, compress = SCC(adj, adj_rev)
    ans = []
    Q = int(input())
    query = []
    for _ in range(Q):
        u, v = map(int, input().split())
        query.append((u, v))
        if compress[u+1] == compress[v+1]:
            ans.append(1)
        else:
            ans.append(0)
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()

