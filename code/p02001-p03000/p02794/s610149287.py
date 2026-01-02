def main():
    import sys
    from collections import defaultdict, deque
    input = sys.stdin.readline

    class SegTree():
        def __init__(self, N):
            # N:  処理する区間の長さ
            self.N0 = 2 ** (N - 1).bit_length()
            self.INF = 2 ** 31 - 1
            self.seg_min = [self.INF] * (2 * self.N0)

        def update(self, index, value):
            index += self.N0 - 1
            self.seg_min[index] = value
            while index > 0:
                index = (index - 1) // 2
                self.seg_min[index] = min(self.seg_min[index * 2 + 1], self.seg_min[index * 2 + 2])

        def query(self, first, last):
            first += self.N0 - 1
            last += self.N0 - 1
            ret = self.INF
            while first <= last:
                if not first & 1:
                    ret = min(ret, self.seg_min[first])
                if last & 1:
                    ret = min(ret, self.seg_min[last])
                first = first // 2
                last = last // 2 - 1
            return ret

    def EulerTour(adj, root):
        st = [root]
        ret = []
        seen = [0] * len(adj)
        par = [0] * len(adj)
        depth = [0] * len(adj)
        while st:
            v = st.pop()
            if seen[v]:
                ret.append(v)
                continue
            ret.append(v)
            seen[v] = 1
            if par[v] != 0:
                st.append(par[v])
            for u in adj[v]:
                if seen[u] == 0:
                    st.append(u)
                    par[u] = v
                    depth[u] = depth[v] + 1

        return ret, depth, par

    def f(a, b):
        return a*100+b

    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    et, depth, par = EulerTour(adj, 1)
    segtree = SegTree(len(et) + 1)
    left = [-1] * (N + 1)
    right = [-1] * (N + 1)
    for i, v in enumerate(et):
        segtree.update(i + 1, depth[v])
        if left[v] < 0:
            left[v] = i
        right[v] = i

    M = int(input())
    edge2cond = defaultdict(int)
    for j in range(M):
        a, b = map(int, input().split())
        lca_depth = segtree.query(min(left[a], left[b]) + 1, max(right[a], right[b]) + 1)
        prev = a
        for i in range(depth[a] - lca_depth):
            parent = par[prev]
            edge2cond[parent*100+prev] += 2**j
            prev = parent
        prev = b
        for i in range(depth[b] - lca_depth):
            parent = par[prev]
            edge2cond[parent*100+prev] += 2**j
            prev = parent

    que = deque()
    que.append(1)
    seen = [-1] * (N+1)
    seen[1] = 0
    par = [0] * (N+1)
    child = [[] for _ in range(N+1)]
    seq = []
    while que:
        v = que.popleft()
        seq.append(v)
        for u in adj[v]:
            if seen[u] == -1:
                seen[u] = seen[v] + 1
                par[u] = v
                child[v].append(u)
                que.append(u)
    seq.reverse()
    dp = [[0] * (2**M) for _ in range(N)]
    dp[0][0] = 1
    for i, v in enumerate(seq):
        if v == 1:
            continue
        for mask in range(2**M):
            u = par[v]
            mask_new = edge2cond[u*100+v]

            dp[i+1][mask] += dp[i][mask]
            dp[i+1][mask | mask_new] += dp[i][mask]
    print(dp[-1][-1])
    #print(dp)
    #print(edge2cond)


if __name__ == '__main__':
    main()
