def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in [0]*(n-1)]

    g = [[] for _ in [0]*n]
    [g[a-1].append(b-1) for a, b in ab]
    [g[b-1].append(a-1) for a, b in ab]

    class rerooting():
        # addは頂点iに頂点jを根とする部分木（DPの値：x）をくっつけるときの補正
        def __init__(self, tree, ini, monoid, add):
            # 頂点iについて、jが根のときのDPの値を求める（アクセス時間を考慮してここで定義）
            def calc(i, j):
                root = tree_d[i][j]+1
                try:
                    return monoid(tc_l[i][root-1], tc_r[i][root])
                except:
                    return tc_l[i][root-1]
            size = len(tree)
            dp, order, q, anc = [ini]*size, [], [0], [-1]*n
            oa, qa, qp = order.append, q.append, q.pop
            tree_d = [{k: j for j, k in enumerate(i)} for i in g]
            g_size = [len(i) for i in g]
            tc_l = [[ini]*(i+1) for i in g_size]
            tc_r = [[ini]*i for i in g_size]

            # トポロジカル順序をorderに記録、0を根とする根付き木上のiの祖先をanc[i]とする
            while q:
                i = qp()
                a = anc[i]
                oa(i)
                for j in g[i]:
                    if j != a:
                        qa(j)
                        anc[j] = i

            # dpおよびtree_preに記録
            for i in order[:0:-1]:
                a = anc[i]
                d, t = add(a, i, dp[i]), tree_d[a][i]
                tc_l[a][t+1], tc_r[a][t], dp[a] = d, d, monoid(dp[a], d)

            # 頂点0のみ先に処理
            for j in range(1, g_size[0]+1):
                tc_l[0][j] = monoid(tc_l[0][j], tc_l[0][j-1])
            for j in range(g_size[0]-2, 0, -1):
                tc_r[0][j] = monoid(tc_r[0][j], tc_r[0][j+1])

            # 行きがけ順に処理
            for i in order[1:]:
                a = anc[i]
                d, c, length = tree_d[i][a], add(a, i, calc(a, i)), g_size[i]
                tc_l[i][d+1], tc_r[i][d] = c, c
                for j in range(1, length+1):
                    tc_l[i][j] = monoid(tc_l[i][j], tc_l[i][j-1])
                for j in range(length-2, 0, -1):
                    tc_r[i][j] = monoid(tc_r[i][j+1], tc_r[i][j])
                dp[i] = tc_l[i][-1]

            # アトリビュートに格納
            self.dp, self.tc_l, self.tc_r, self.tree_d, self.monoid = dp, tc_l, tc_r, tree_d, monoid

        # 頂点iについて、jが根のときのDPの値を求める

        def DP_part(self, i, j):
            root = self.tree_d[i][j]+1
            try:
                return self.monoid(self.tc_l[i][root-1], self.tc_r[i][root])
            except:
                return self.tc_l[i][root-1]

    def monoid1(x, y): return x*y % m
    def add1(i, j, x): return x+1

    r1 = rerooting(g, 1, monoid1, add1)
    for i in r1.dp:
        print(i)


main()
