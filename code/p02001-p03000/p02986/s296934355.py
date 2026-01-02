def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.buffer.readline

    # クエリは0-indexedで[l, r)
    class SparseTable():
        def __init__(self, A):
            # A: 処理したい数列
            self.N = len(A)
            self.K = self.N.bit_length() - 1
            self.table = [[0] * (self.K + 1) for _ in range(self.N)]
            for i, a in enumerate(A):
                self.table[i][0] = a
            for k in range(1, self.K + 1):
                for i in range(self.N):
                    j = i + (1 << (k - 1))
                    if j <= self.N - 1:
                        self.table[i][k] = STfunc(self.table[i][k - 1], self.table[j][k - 1])
                    else:
                        self.table[i][k] = self.table[i][k - 1]

        def query(self, l, r):
            # [l, r)の最小値を求める
            k = (r - l).bit_length() - 1
            return STfunc(self.table[l][k], self.table[r - (1 << k)][k])

    # adj[0] must be empty list
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

        return ret, depth

    N, Q = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    E = {}
    for _ in range(N - 1):
        a, b, c, d = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        E[a * (N + 1) + b] = (c, d)
        E[b * (N + 1) + a] = (c, d)

    et, depth = EulerTour(adj, 1)
    left = [-1] * (N + 1)
    right = [-1] * (N + 1)
    dist_from_root = [-1] * (N+1)
    dist_from_root[1] = 0
    color_info = [[] for _ in range(N)]
    color_d = [[] for _ in range(N)]
    for i, v in enumerate(et):
        if left[v] < 0:
            left[v] = i
        right[v] = i
        if i != 0:
            u = et[i-1]
            c, d = E[v*(N+1)+u]
            if dist_from_root[v] < 0:
                dist_from_root[v] = dist_from_root[u] + d
            if depth[u] < depth[v]:
                color_info[c].append(i)
                if not color_d[c]:
                    color_d[c].append((1, d))
                else:
                    prev_num, prev_d = color_d[c][-1]
                    color_d[c].append((prev_num+1, prev_d+d))
            else:
                color_info[c].append(i)
                prev_num, prev_d = color_d[c][-1]
                color_d[c].append((prev_num - 1, prev_d - d))

    # min
    def STfunc(a, b):
        if depth[a] < depth[b]:
            return a
        else:
            return b

    ST = SparseTable(et)
    for _ in range(Q):
        x, y, u, v = map(int, input().split())
        lca = ST.query(min(left[u], left[v]), max(right[u], right[v])+1)
        if color_info[x]:
            le = len(color_info[x])
            iu = bisect_left(color_info[x], left[u]+1) - 1
            if iu == -1:
                du = dist_from_root[u]
            else:
                num_u, dist_u = color_d[x][iu]
                du = dist_from_root[u] + num_u * y - dist_u
            
            iv = bisect_left(color_info[x], left[v]+1) - 1
            if iv == -1:
                dv = dist_from_root[v]
            else:
                num_v, dist_v = color_d[x][iv]
                dv = dist_from_root[v] + num_v * y - dist_v

            ilca = bisect_left(color_info[x], left[lca]+1) - 1
            if ilca == -1:
                dlca = dist_from_root[lca]
            else:
                num_lca, dist_lca = color_d[x][ilca]
                dlca = dist_from_root[lca] + num_lca * y - dist_lca

            print(du + dv - 2*dlca)
        else:
            print(dist_from_root[u] + dist_from_root[v] - 2 * dist_from_root[lca])


if __name__ == '__main__':
    main()
